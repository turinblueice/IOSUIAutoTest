#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.view.View

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class View(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, view=None, **kwargs):
        super(View, self).__init__(parent)
        self.__view = view if isinstance(view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__view, item, None)

    @property
    def text(self):
        if isinstance(self.__view.text, unicode):
            return self.__view.text.encode('utf8')
        return self.__view.text

    def tap(self, wait_time=0.5):
        self.__view.click()
        # 显示等待wait_Time秒
        self.base_parent.implicitly_wait(wait_time)

    def clear_text_field(self):
        self.__view.clear()  #Clears the text if it’s a text entry element.

    def send_keys(self, *values):
        self.__view.send_keys(*values)
        # 显示等待0.5秒
        self.base_parent.implicitly_wait(0.5)


class ViewList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(ViewList, self).__init__(parent)
        self.__view_list = self.find_elements(**kwargs)


