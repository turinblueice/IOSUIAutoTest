# -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIASearchbar

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIASearchBar(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, bar=None, **kwargs):
        super(UIASearchBar, self).__init__(parent)
        self.__search_bar = bar if isinstance(bar, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__search_bar, item, None)

    def tap(self, wait_time=0.5):
        self.__search_bar.click()
        # 显示等待wait_Time秒
        self.base_parent.implicitly_wait(wait_time)

    def clear_text_field(self):
        self.__search_bar.clear()  #  Clears the text if it’s a text entry element.

    def send_keys(self, *values):
        self.__search_bar.send_keys(*values)
        # 显示等待0.5秒
        self.base_parent.implicitly_wait(0.5)

    def set_text(self, keys=''):

        self.__search_bar.set_text(keys)


class UIASearchBarList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIASearchBarList, self).__init__(parent)
        self.__bar_list = self.find_elements(**kwargs)


