#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIATextField

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIASecureTextField(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, edit_text=None, **kwargs):
        super(UIASecureTextField, self).__init__(parent)
        self.__edit_text = edit_text if isinstance(edit_text, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__edit_text, item, None)

    @property
    def text(self):
        if isinstance(self.__edit_text.text, unicode):
            return self.__edit_text.text.encode('utf8')
        return self.__edit_text.text

    def tap(self, wait_time=0.5):
        self.__edit_text.click()
        # 显示等待wait_Time秒
        self.base_parent.implicitly_wait(wait_time)

    def clear_text_field(self):
        self.__edit_text.clear()  # Clears the text if it’s a text entry element.

    def send_keys(self, *values):
        self.__edit_text.send_keys(*values)
        # 显示等待0.5秒
        self.base_parent.implicitly_wait(0.5)

    def set_text(self, keys=''):

        self.__edit_text.set_text(keys)


class UIASecureTextFieldList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIASecureTextFieldList, self).__init__(parent)
        self.__edit_text_list = self.find_elements(**kwargs)


