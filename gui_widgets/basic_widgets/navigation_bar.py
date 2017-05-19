#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIANavigationbar

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIANavigationbar(base_frame_view.BaseFrameView):
    """
    Attribute:
        __switch:
    """
    def __init__(self, parent, layout=None, **kwargs):
        super(UIANavigationbar, self).__init__(parent)
        self.__bar_layout = layout if isinstance(layout, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__bar_layout, item, None)

    def tap(self):
        self.__bar_layout.click()

    def get_webelement(self):
        return self.__bar_layout


class UIANavigationbarList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIANavigationbarList, self).__init__(parent)
        self.__bar_layout_list = self.find_elements(**kwargs)

    @property
    def bar_list(self):
        if self.__bar_layout_list:
            return [UIANavigationbar(layout.parent, layout) for layout in self.__bar_layout_list]
        return None


