#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.widget.ImageView

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class NumberPicker(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, view=None, **kwargs):
        super(NumberPicker, self).__init__(parent)
        self._view = view if isinstance(view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self._view, item, None)

    @property
    def view_element(self):
        return self._view

    def tap(self):
        self._view.click()


class NumberPickerList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(NumberPickerList, self).__init__(parent)
        self._number_picker_list = self.find_elements(**kwargs)

    @property
    def item_list(self):
        if self._number_picker_list:
            return [NumberPicker(item.parent, item) for item in self._number_picker_list]
        return None


