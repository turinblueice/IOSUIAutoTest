#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 用户中心-我的贴纸-我的tab

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import table_view
from gui_widgets.basic_widgets import table_cell
from gui_widgets.basic_widgets import button

from gui_widgets.custom_widgets import search_bar
from UIAWindows import windows
from UIAWindows.user_center_sub_windows.user_paster_windows import user_paster_window

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


class MyOwnPasterTabWindow(user_paster_window.UserPasterWindow):

    """
        Summary:
            用户中心-我的贴纸-我的tab页

        Attributes:

    """

    def __init__(self, parent):
        super(MyOwnPasterTabWindow, self).__init__(parent)
        self.__scroll_view = table_view.UIATableView(self.parent, type='UIATableView')
        self.__size = self.base_parent.get_window_size()

    @property
    def add_paseter_button(self):
        """
            Summary:
                添加贴纸按按钮
        """
        xpath_ = '//UIATableView[1]/UIATableCell[4]'
        cell = table_cell.UIATableCell(self.base_parent, xpath=xpath_)
        return button.UIAButton(cell, type='UIAButton')  # cell下第一个button就是

    @property
    def add_template_button(self):
        """
            Summary:
                添加模板按钮
        """
        xpath_ = '//UIATableView[1]/UIATableCell[6]'
        cell = table_cell.UIATableCell(self.base_parent, xpath=xpath_)

        return button.UIAButton(cell, type='UIAButton')

    @property
    def used_recently_paster_list(self):
        """
            Summary:
                最近使用贴纸列表
        :return:
        """
        xpath_ = '//UIATableView[1]/UIATableCell[2]'
        cell = table_cell.UIATableCell(self.base_parent, xpath=xpath_)

        return button.UIAButtonList(cell, type='UIAButton').button_list

    @property
    def my_custom_paster_list(self):
        """
            Summary:
                我的自定义贴纸列表
        """
        xpath_ = '//UIATableView[1]/UIATableCell[4]'
        cell = table_cell.UIATableCell(self.base_parent, xpath=xpath_)
        # 第一个元素为按钮，移出列表
        button_list = button.UIAButtonList(cell, type='UIAButton').button_list[1:]
        button_list = [m_button for m_button in button_list if not m_button.text == 'new']
        return button_list

    @property
    def new_paster_icon(self):
        """
            Summary:
                新添加第贴纸标记
        """
        return button.UIAButton(self.parent, name='new')

    @property
    def my_keep_template_list(self):
        """
            Summary:
                收藏的模板列表
        :return:
        """
        xpath_ = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[6]'
        cell = table_cell.UIATableCell(self.base_parent, xpath=xpath_)
        # 第一个元素为按钮，移出列表
        return button.UIAButtonList(cell, type='UIAButton').button_list[1:]

    # ************************选择贴纸模板遮罩**********************

    # @property
    # def paster_available_list(self):
    #     """
    #         Summary:
    #             已有贴纸列表
    #     暂时注释,遮罩无法识别抓取
    #     """
    #     xpath_ = '//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout'
    #     return tool_bar.RelativeLayoutList(self.parent, xpath=xpath_).relative_layout_list

    @property
    def select_from_gallery_button(self):
        """
            Summary:
                从手机相册中选择按钮
        :return:
            暂时只能以像素点的方式返回
        """
        x = self.__size['width']/2
        y = self.__size['height']*1.0/13*11.5
        return x, y

    @property
    def cancel_popup_button(self):
        """
            Summary:
                取消弹层按钮
        暂时只能以像素点的方式返回
        """
        x = self.__size['width']/2
        y = self.__size['height']*1.0/13*12.5
        return x, y

    # ************************操作方法***************************
    def choose_custom_paster(self, index):
        """
            Summary:
                在自定义贴纸列表中，选择已有自定义贴纸
            Args:
                index: 序号
        :return:
        """
        log.logger.info("开始选择第{}张贴纸".format(index))
        self.my_custom_paster_list[index-1].tap()
        log.logger.info("完成第{}张贴纸点击".format(index))
        try:
            WebDriverWait(self.base_parent, 10).until(
                EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, '立即使用')))  # 等待"立即使用"的按钮出现
            log.logger.info("已吊起贴纸对话框")
            return True
        except TimeoutException:
            log.logger.info("吊起贴纸对话框失败")
            return False

    def is_guide_exist(self):
        """
            Summary:
                是否出现添加贴纸的引导页,首次进入贴纸页面会出现引导页
        :return:
        """
        try:
            WebDriverWait(self.base_parent, 10).until(
                EC.presence_of_element_located(
                    (MobileBy.ACCESSIBILITY_ID, 'INPasterMallResource.bundle/pasterdiy_addguide')
                )
            )
            return True
        except TimeoutException:
            return False

    def tap_add_paster_button(self):
        """
            Summary:
                点击添加贴纸按钮
        """
        log.logger.info("点击添加贴纸按钮")
        time.sleep(2)
        self.add_paseter_button.tap()
        log.logger.info("完成贴纸添加按钮的点击")
        time.sleep(3)
        log.logger.info("弹出底部遮罩弹层")

    # def select_paster_available(self, index):
    #     """
    #         Summary:
    #             在弹出的popupwindow里面选择贴纸
    #         Args:
    #             index：贴纸序号
    #             暂时注释,不能识别抓取控件
    #     """
    #     log.logger.info("开始选择第{}张贴纸".format(index))
    #     self.paster_available_list[index-1].tap()
    #     if self.wait_window(windows.WindowNames.CUSTOM_PASTER_EDITOR, 10):
    #         log.logger.info("成功进入贴纸搭配页")
    #         return True
    #     log.logger.info("进入贴纸搭配页失败")
    #     return False

    def select_from_gallery(self):
        """
            Summary:
                从相册中选择
        :return:
        """
        log.logger.info("点击从相册中选择按钮")
        self.base_parent.tap([self.select_from_gallery_button])
        # self.select_from_gallery_button.tap()
        log.logger.info("完成从相册中选择按钮的点击")
        if self.wait_for_element_present(self.base_parent, timeout=5,
                                         name='INPasterMallResource.bundle/pasterdiy_selectimagetip'):
            log.logger.info("选择图片的引导tips存在,先关闭")
            self.tap_window_top()

        if self.wait_window(windows.WindowNames.PHOTO_ALBUM_PICKER, 10):
            log.logger.info("成功进入图片列表选择页")
            return True
        log.logger.error("进入图片列表选择页失败")
        return False

    def tap_cancel_popup(self):
        """
            Summary:
                点击取消弹出面板按钮
        :return:
        """
        log.logger.info("点击取消按钮")
        self.base_parent.tap([self.cancel_popup_button])
        # self.cancel_popup_button.tap()
        log.logger.info("点击结束")
        time.sleep(2)
        return True
