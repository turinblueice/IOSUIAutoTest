#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.widget.LinearLayout

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class LinearLayout(base_frame_view.BaseFrameView):
    """
    Attribute:
        __switch:
    """
    def __init__(self, parent, linear_layout=None, **kwargs):
        super(LinearLayout, self).__init__(parent)
        self.__linear_layout = linear_layout if isinstance(linear_layout, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__linear_layout, item, None)

    def tap(self):
        self.__linear_layout.click()


class LinearLayoutList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(LinearLayoutList, self).__init__(parent)
        self.__linear_layout_list= self.find_elements(**kwargs)

    @property
    def layout_list(self):

        return [LinearLayout(layout.parent, layout) for layout in self.__linear_layout_list]


