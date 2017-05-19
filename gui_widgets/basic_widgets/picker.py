#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:UIAPicker

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIAPicker(base_frame_view.BaseFrameView):
    """
        Summary:
            UIAPicker类
    """
    def __init__(self, parent, picker=None, **kwargs):
        super(UIAPicker, self).__init__(parent)
        self.__picker = picker if isinstance(picker, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__picker, item, None)

    def tap(self):
        self.__picker.click()


class UIAPickerList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAPickerList, self).__init__(parent)
        self.__picker_list = self.find_elements(**kwargs)

    @property
    def picker_widget_list(self):
        if self.__picker_list:
            return [UIAPicker(picker_item.parent, picker_item) for picker_item in self.__picker_list]
        return None


