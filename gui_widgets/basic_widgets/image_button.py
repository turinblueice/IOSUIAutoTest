#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.widget.ImageButton

Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class ImageButton(base_frame_view.BaseFrameView):
    """

    Attribute:
        __image_button:private.
    """
    def __init__(self, parent, image_button=None, **kwargs):
        super(ImageButton, self).__init__(parent)
        self.__image_button = image_button if isinstance(image_button, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):

        return getattr(self.__image_button, item, None) or super(ImageButton, self).__getattr__(item)

    def tap(self):
        self.__image_button.click()


class ImageButtonList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(ImageButtonList, self).__init__(parent)
        self.__image_button_list = self.find_elements(**kwargs)


