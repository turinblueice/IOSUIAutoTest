#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:UIAStaticText

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIAStaticText(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, text_view=None, **kwargs):
        super(UIAStaticText, self).__init__(parent)
        self.__text_view = text_view if isinstance(text_view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):

        return getattr(self.__text_view, item, None)

    @property
    def text(self):

        if isinstance(self.__text_view.text, unicode):
            return self.__text_view.text.encode('utf8')
        return self.__text_view.text

    def tap(self):
        self.__text_view.click()

    def clear_text_field(self):
        self.__text_view.clear()  # Clears the text if it’s a text entry element.

    def send_keys(self, *values):
        self.__text_view.send_keys(*values)
        # 显示等待0.5秒
        self.base_parent.implicitly_wait(0.5)

    def set_text(self, keys=''):
        self.__text_view.set_text(keys)


class UIAStaticTextList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAStaticTextList, self).__init__(parent)
        self.__text_view_list = self.find_elements(**kwargs)

    @property
    def text_view_list(self):
        if self.__text_view_list:
            return [UIAStaticText(layout.parent, layout) for layout in self.__text_view_list]
        return None

