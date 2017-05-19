#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.widget.CheckBox

Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class CheckedTextView(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, checked_text_view=None, **kwargs):
        super(CheckedTextView, self).__init__(parent)
        self.__checked_text_view = checked_text_view if \
            isinstance(checked_text_view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):

        return getattr(self.__checked_text_view, item, None)

    def tap(self):
        self.__checked_text_view.click()


class CheckedTextViewList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(CheckedTextViewList, self).__init__(parent)
        self.__check_text_view_list = self.find_elements(**kwargs)

    @property
    def checked_text_view_list(self):

        return [CheckedTextView(check_box.parent, check_box) for check_box in self.__check_text_view_list]

