#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 拍照编辑页,主页-点击照片-点击照相机

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log

from gui_widgets.basic_widgets import image_button
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import static_text

from appium.webdriver import WebElement
from UIAWindows import windows
from selenium.common.exceptions import NoSuchElementException

import time


class CameraWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            拍照编辑页,主页-点击照片-点击照相机

        Attributes:

    """
    
    def __init__(self, parent):
        super(CameraWindow, self).__init__(parent)

    @property
    def close_button(self):
        """
            Summary:
                关闭按钮
        """
        name_ = 'camera close'
        return button.UIAButton(self.parent, name=name_)

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        """
        name_ = 'camera close'
        return button.UIAButton(self.parent, name=name_)

    @property
    def grid_button(self):
        """
            Summary:
                九宫格线按钮
        """
        name_ = 'camera grid'
        return button.UIAButton(self.parent, name=name_)

    @property
    def switch_camera_button(self):
        """
            Summary:
                切换摄像头按钮
        """
        name_ = "camera switch"
        return button.UIAButton(self.parent, name=name_)

    @property
    def photo_bar_hide_display_button(self):
        """
            Summary:
                照片栏隐藏/显示按钮
        :return:
        """
        name_ = 'TabExpand'
        return button.UIAButton(self.parent, name=name_)

    @property
    def camera(self):
        """
            Summary:
                相机按钮
        """
        name_ = 'camera captureBtn'
        return button.UIAButton(self.parent, name=name_)

    @property
    def photo_list(self):
        """
            Summary:
                已存在图片列表
        """
        photo_xpath_ = '//UIAScrollView[2]/UIAImage'
        check_xpath_ = '//UIAScrollView[2]/UIAStaticText'
        return PhotoItemList(self.base_parent, photo_key='xpath', photo_value=photo_xpath_,
                             check_key='xpath', check_value=check_xpath_).item_list

    @property
    def next_step_button(self):
        """
            Summary:
                下一步按钮
        :return:
        """
        name_ = '下一步'
        return button.UIAButton(self.parent, name=name_)

    @property
    def slide_filter_tips(self):
        """
            Summary:
                首次进入的滑动切换滤镜的提示
        Returns:

        """
        name_ = '滑动切换滤镜'
        return static_text.UIAStaticText(self.parent, name=name_)

    @property
    def filter_slide_block(self):
        """
            Summary:
                滤镜滑块
        Returns:

        """
        name_ = 'INPublishResource.bundle/cameraFilterGuid.png'
        return image.UIAImage(self.parent, name=name_)

    # ************************操作***************************
    def tap_camera(self):
        """
            Summary:
                点击摄像头
        """
        log.logger.info("点击摄像头")
        self.caremra.tap()
        time.sleep(2)
        log.logger.info("摄像头已点击")

    def select_photos(self, *indexes):
        """
            Summary:
                选择图片
            Args:
                *indexes: 图片序号元组
        """
        for index in indexes:
            log.logger.info("开始选择第{}张图片".format(index))
            self.photo_list[index-1].tap()
            log.logger.info("选择完毕")
            time.sleep(2)

    def tap_next_step_button(self, timeout=10):
        """
            Summary:
                点击下一步按钮
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击下一步按钮")
        self.next_step_button.tap()
        if self.wait_window(windows.WindowNames.PUBLISH_CORE, timeout):
            log.logger.info("成功进入图片发布加工页")
            return True
        else:
            log.logger.error("进入图片发布加工页失败")
            return False


class PhotoItem(base_frame_view.BaseFrameView):
    """
        Summary:
            照片item
    """
    def __init__(self, parent, item=None, check_item=None, index=None, **kwargs):
        super(PhotoItem, self).__init__(parent)
        self._layout_view = item if isinstance(item, WebElement) else self.find_element(**kwargs)
        self._check_item = check_item
        self.__is_select = False
        self.__index = index

    def __getattr__(self, item):
        return getattr(self._layout_view, item, None)

    @property
    def selected_value(self):
        """
            Summary:
                选中序号
        """
        text = self._check_item.text
        if isinstance(text, unicode):
            text = text.encode('utf8')
        return text

    @property
    def is_selected(self):

        return True if self.selected_value else False

    def tap(self):
        """
            Summary:
                点击该图片
        """
        log.logger.info("开始点击选择{}照片".format('第' + str(self.__index) + '张' if self.__index is not None else '该'))
        self._layout_view.click()
        time.sleep(2)
        log.logger.info("点击完毕")

    def select(self):
        """
            Summary:
                选择图片，点击图片区域即可选择，无需点击check_box
        """
        if not self.__is_select:
            log.logger.info("开始点击选择{}图片".format('第'+str(self.__index)+'张' if self.__index is not None else '该'))
            self._layout_view.click()
            time.sleep(2)
            if self._update_check_status():
                log.logger.info("选中标记出现，已选中")
                self.__is_select = True
                log.logger.info("完成选择")
                log.logger.info("已成功选中图片")
                return True
            log.logger.error("选中图片失败")
            return False

    def unselect(self):
        """
            Summary:
                取消选择图片
        """
        if self.__is_select:
            log.logger.info("开始取消选择{}图片".format('第' + str(self.__index) + '张' if self.__index is not None else '该'))
            self._layout_view_item.click()
            time.sleep(2)
            if not self._update_check_status():
                log.logger.info("选中标记已消失，已取消选择")
                self.__is_select = False
                log.logger.info("完成取消")
                return True
            log.logger.error("取消选中失败")
            return False

    def _update_check_status(self):
        """
            Summary:
                更新图片选中状态
        Returns:

        """
        check_value = '//UIAScrollView[2]/UIAStaticText[{}]'.format(self.__index)
        self._check_item = self.find_element(key='xpath', value=check_value)
        if self._check_item.text:
            return True
        return False


class PhotoItemList(base_frame_view.BaseFrameView):

    def __init__(self, parent, photo_key, photo_value, check_key, check_value):
        super(PhotoItemList, self).__init__(parent)
        self.__image_list = self.find_elements(key=photo_key, value=photo_value)  # 图片列表
        self.__check_list = self.find_elements(key=check_key, value=check_value)  # 选中数字列表

    @property
    def item_list(self):
        if self.__image_list:
            log.logger.info("可视区域内图片个数为{}".format(len(self.__image_list)))
            photo_list = []
            for index, item in enumerate(self.__image_list, start=1):
                photo_item = PhotoItem(item.parent, item, self.__check_list[index-1], index)
                photo_list.append(photo_item)

            return photo_list
        return None
