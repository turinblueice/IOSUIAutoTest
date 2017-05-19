#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIAImage

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIAImage(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, image_view=None, **kwargs):
        super(UIAImage, self).__init__(parent)
        self.__image_view = image_view if isinstance(image_view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__image_view, item, None)

    def tap(self):
        self.__image_view.click()


class UIAImageList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAImageList, self).__init__(parent)
        self.__image_list = self.find_elements(**kwargs)

    @property
    def image_list(self):

        if self.__image_view_list:
            return [UIAImage(item.parent, item) for item in self.__image_list]
        return None


