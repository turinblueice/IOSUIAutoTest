#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:UIAScrollView

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIAScrollView(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, scroll_view=None, **kwargs):
        super(UIAScrollView, self).__init__(parent)
        self.__scroll_view = scroll_view if isinstance(scroll_view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):

        return getattr(self.__scroll_view, item, None)

    def tap(self):
        self.__scroll_view.click()


class UIAScrollViewList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAScrollViewList, self).__init__(parent)
        self.__scroll_view_list = self.find_elements(**kwargs)

    @property
    def scroll_view_list(self):
        if self.__scroll_view_list:
            return [UIAScrollView(layout.parent, layout) for layout in self.__scroll_view_list]
        return None

