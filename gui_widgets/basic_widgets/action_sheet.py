#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIAActionSheet
Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from util import log
from appium.webdriver.webelement import WebElement
from gui_widgets.basic_widgets import button
import time


class UIAActionSheet(base_frame_view.BaseFrameView):
    """

    Attribute:

    """
    def __init__(self, parent, action_sheet=None, **kwargs):
        super(UIAActionSheet, self).__init__(parent)
        if kwargs:
            self._action_sheet = action_sheet if isinstance(action_sheet, WebElement) else self.find_element(**kwargs)
        else:
            self._action_sheet = action_sheet if isinstance(action_sheet, WebElement) else \
                self.find_element(self.parent, type='UIAActionSheet')

    def __getattr__(self, item):
        return getattr(self._action_sheet, item, None)

    def tap(self):
        self._action_sheet.click()

    @property
    def cancel_button(self):
        """
            Summary:
                UIAActionSheet中的取消按钮
        Returns:

        """
        name_ = '取消'
        return button.UIAButton(self.parent, name=name_)

    # **************操作方法**************

    def tap_cancel_button(self):
        """
            Summary:
                点击取消按钮
        Returns:

        """
        log.logger.info("点击取消按钮")
        self.cancel_button.tap()
        time.sleep(3)
        log.logger.info("完成点击")


class UIAActionSheetList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAActionSheetList, self).__init__(parent)
        self._action_sheet_list = self.find_elements(**kwargs)

    @property
    def sheet_list(self):

        if self._action_sheet_list:
            return [UIAActionSheet(item.parent, item) for item in self._action_sheet_list]
        return None

