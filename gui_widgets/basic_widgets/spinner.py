#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.widget.Spinner

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class Spinner(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, spinner=None, **kwargs):
        super(Spinner, self).__init__(parent)
        self.__spinner = spinner if isinstance(spinner, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__spinner, item, None)

    @property
    def text(self):
        return self.__spinner.text

    def tap(self):
        self.__spinner.click()


class SpinnerList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(SpinnerList, self).__init__(parent)
        self.__spinner_list = self.find_elements(**kwargs)


