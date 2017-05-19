#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIAToolbar

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIAToolbar(base_frame_view.BaseFrameView):
    """
    Attribute:
        __switch:
    """
    def __init__(self, parent, layout=None, **kwargs):
        super(UIAToolbar, self).__init__(parent)
        self.__toolbar_layout = layout if isinstance(layout, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__toolbar_layout, item, None)

    def tap(self):
        self.__toolbar_layout.click()

    def get_webelement(self):
        return self.__toolbar_layout


class UIAToolbarList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAToolbarList, self).__init__(parent)
        self.__toolbar_layout_list = self.find_elements(**kwargs)

    @property
    def relative_layout_list(self):
        if self.__toolbar_layout_list:
            return [UIAToolbar(layout.parent, layout) for layout in self.__toolbar_layout_list]
        return None


