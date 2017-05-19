#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIAWindow

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIAWindow(base_frame_view.BaseFrameView):
    """
    Attribute:

    """
    def __init__(self, parent, window=None, **kwargs):
        super(UIAWindow, self).__init__(parent)
        self.__window = window if isinstance(window, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__window, item, None)

    def tap(self):
        self.__window.click()


class UIAWindowList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAWindowList, self).__init__(parent)
        self.__window_list = self.find_elements(**kwargs)

    @property
    def window_list(self):

        if self.__window_list:
            return [UIAWindow(item.parent, item) for item in self.__window_list]
        return None


