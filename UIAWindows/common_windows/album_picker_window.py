#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 图片集列表选择页

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log

from gui_widgets.basic_widgets import navigation_bar
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import image

from appium.webdriver import WebElement

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time


class PhotoAlbumPickerWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            图片集列表选择页

        Attributes:

    """
    
    def __init__(self, parent):
        super(PhotoAlbumPickerWindow, self).__init__(parent)

    @property
    def back_button(self):
        """
            Summary:
                取消按钮
        """
        name_ = '取消'
        return button.UIAButton(self.__frame_view, name=name_)

    @property
    def post_photo_album_list(self):
        """
            Summary:
                要上传的图片列表
        """
        return PostAlbumItemList(self.base_parent, type='UIATableCell').item_list

    @property
    def guide_mask(self):
        """
            Summary:
                引导页
        Returns:

        """
        name_ = 'INPasterMallResource.bundle/pasterdiy_selectimagetip'
        return image.UIAImage(self.parent, name=name_)

    # ************************操作***************************

    def select_photo_album(self, index):
        """
            Summary:
                选择要上传的图片集
            Args:
                index: 图片序号
        """
        self.post_photo_album_list[index-1].tap()
        time.sleep(1)

    def is_guide_exist(self):
        """
            Summary:
                是否存在引导页面
        Returns:

        """
        if self.wait_for_element_present(self.parent, timeout=5,
                                         name='INPasterMallResource.bundle/pasterdiy_selectimagetip'):
            log.logger.info("存在引导页")
            return True
        return False

    def remove_guide_mask(self):
        """
            Summary:
                取消引导页
        Returns:

        """
        if self.is_guide_exist():
            log.logger.info("存在引导页,点击取消")
            self.guide_mask.tap()
            time.sleep(2)
        log.logger.info("引导页不存在,无需取消")


class PostAlbumItem(base_frame_view.BaseFrameView):
    """
        Summary:
            上传的图片item
    """
    def __init__(self, parent, item=None, index=None, **kwargs):
        super(PostAlbumItem, self).__init__(parent)
        self.__post_album_item = item if isinstance(item, WebElement) else self.find_element(**kwargs)
        self.__index = index

    def __getattr__(self, item):
        return getattr(self.__post_album_item, item, None)

    def title(self):

        return static_text.UIAStaticText(self.__post_album_item, type='UIAStaticText').text

    def tap(self):
        """
            Summary:
                点击该图片
        :return:
        """
        name = self.title()
        log.logger.info("开始点击选择{}图集".format('第' + str(self.__index+1) + '个' if self.__index is not None else '该'))
        self.__post_album_item.click()
        time.sleep(2)
        log.logger.info("点击完毕")
        if self.wait_for_element_present(navigation_bar.UIANavigationbar(self.parent, type='UIANavigationBar'),
                                         timeout=5,
                                         name=name):
            log.logger.info("成功进入\"{}\"相册".format(name))
            return True
        log.logger.error("进入该相册\"{}\"失败".format(name))
        return False


class PostAlbumItemList(base_frame_view.BaseFrameView):

    def __init__(self, parent, **kwargs):
        super(PostAlbumItemList, self).__init__(parent)
        self.__item_list = self.find_elements(**kwargs)

    @property
    def item_list(self):
        if self.__item_list:
            log.logger.info("可视区域内图片集个数为{}".format(len(self.__item_list)))
            return [PostAlbumItem(item.parent, item, index) for index, item in enumerate(self.__item_list, start=0)]
        return None
