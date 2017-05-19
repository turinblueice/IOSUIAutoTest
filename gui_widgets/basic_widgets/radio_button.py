#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.widget.RadioButton

Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class RadioButton(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, radio_button=None, **kwargs):
        super(RadioButton, self).__init__(parent)
        self.__radio_button = radio_button if isinstance(radio_button, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):

        return getattr(self.__radio_button, item, None)

    def tap(self):
        self.__radio_button.click()


class RadioButtonList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(RadioButtonList, self).__init__(parent)
        self.__radio_button_list = self.find_elements(**kwargs)


