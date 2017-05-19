#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 故事设置页

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import table_group
from gui_widgets.basic_widgets import table_cell
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import table_view

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from UIAWindows import windows

import time
import random


class StorySettingWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            发布故事集-故事设置页

        Attributes:

    """

    def __init__(self, parent):
        super(StorySettingWindow, self).__init__(parent)

        # 滑动区域
        self._scroll_view = table_view.UIATableView(self.parent, type='UIATableView')

    @property
    def back_button(self):
        """
            Summary:
                后退按钮
        """
        name_ = '返回'
        return button.UIAButton(self.parent, name=name_)

    @property
    def finish_button(self):
        """
            Summary:
                完成按钮
        :return:
        """
        name_ = '完成'
        return button.UIAButton(self.parent, name=name_)

    @property
    def diary_name_edit_box(self):
        """
            Summary:
                故事名称编辑框
        :return:
        """
        name_ = 'INEditStoryPreviouspage'
        table_group_ = table_group.UIAStaticGroup(self.parent, name=name_)
        return text_field.UIATextFieldList(table_group_, type='UIATextField').text_field_list[0]

    @property
    def diary_cover_date(self):
        """
            Summary:
                故事时间
        :return:
        """
        name_ = 'INEditStoryPreviouspage'
        table_group_ = table_group.UIAStaticGroup(self.parent, name=name_)
        return text_field.UIATextFieldList(table_group_, type='UIATextField').text_field_list[1]

    @property
    def diary_cover_location(self):
        """
            Summary:
                故事地点
        :return:
        """
        name_ = 'INEditStoryPreviouspage'
        table_group_ = table_group.UIAStaticGroup(self.parent, name=name_)
        return text_field.UIATextFieldList(table_group_, type='UIATextField').text_field_list[2]

    @property
    def privacy_setting_bar(self):
        """
            Summary:
                隐私设置栏
        :return:
        """
        name_ = '隐私设置'
        return table_cell.UIATableCell(self.parent, name=name_)

    @property
    def category_list(self):
        """
            Summary:
                分类列表
        """
        xpath_ = '//UIATableView[1]/UIATableCell[position()>1]'
        return table_cell.UIATableCellList(self.base_parent, xpath=xpath_).cell_list

    # ************************操作***************************

    def tap_finish_button(self):
        """
            Summary:
                点击完成按钮
        :return:
        """
        log.logger.info("开始点击完成按钮")
        self.finish_button.tap()
        log.logger.info("点击完毕")
        if self.wait_window(windows.WindowNames.STORY_SHARE, 10):
            log.logger.info("成功进入故事分享页")
            return True
        log.logger.error("进入故事分享页失败")
        return False

    def select_category(self, index):
        """
            Summary:
                选择类别
            Args:
                index: 类别序号
        """
        log.logger.info("开始点击第{}个类目".format(index))
        self.category_list[index-1].tap()
        time.sleep(1)
        log.logger.info("完成点击")

    # 无法识别选取控件
    # def is_category_selected(self, index):
    #     """
    #         Summary:
    #             判断类目是否选中
    #         Args:
    #             index： 序号
    #     """
    #     if self.wait_for_element_present(self.category_list[index-1],
    #                                      id='com.jiuyan.infashion:id/iv_story_set_type_select'):
    #         return True
    #     return False
