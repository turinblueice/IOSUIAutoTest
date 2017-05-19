#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIAStaticGroup
Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement
import time


class UIAStaticGroup(base_frame_view.BaseFrameView):
    """

    Attribute:
        __image_button:private.
    """
    def __init__(self, parent, view=None, **kwargs):
        super(UIAStaticGroup, self).__init__(parent)
        self.__group_view = view if isinstance(view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__group_view, item, None)

    def tap(self):
        self.__group_view.click()

    def swipe_up_entire_list_view(self):
        """
            Summary:
                向上滑动整个列表的高度

        """
        location = self.__group_view.location
        size = self.__group_view.size
        x = location['x'] + size['width'] / 2
        start_y = location['y'] + size['height'] - 1
        end_y = location['y'] + 1

        self.swipe_up(x, start_y, end_y)
        time.sleep(2)

    def swipe_down_entire_list_view(self):
        """
            Summary:
                向下滑动整个列表的高度
        """
        location = self.__group_view.location
        size = self.__group_view.size
        x = location['x'] + size['width'] / 2
        end_y = location['y'] + size['height'] - 1
        start_y = location['y'] + 1

        self.swipe_up(x, start_y, end_y)
        time.sleep(2)


class UIAStaticGroupList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAStaticGroupList, self).__init__(parent)
        self.__group_list = self.find_elements(**kwargs)


