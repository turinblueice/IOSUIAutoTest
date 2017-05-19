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


class CheckBox(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, check_box=None, **kwargs):
        super(CheckBox, self).__init__(parent)
        self.__check_box = check_box if isinstance(check_box, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):

        return getattr(self.__check_box, item, None)

    def check(self):
        self.__check_box.click()


class CheckBoxList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(CheckBoxList, self).__init__(parent)
        self.__check_box_list = self.find_elements(**kwargs)

    @property
    def check_box_list(self):

        return [CheckBox(check_box.parent, check_box) for check_box in self.__check_box_list]

