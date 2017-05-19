#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:该模块为底部照片更改的弹层蒙板,如更换头像时底部的弹层
 
Authors: turinblueice
Date:    16/3/16 16:46
"""

from util import log
from gui_widgets.basic_widgets import action_sheet
from gui_widgets.basic_widgets import button

from UIAWindows import windows

import time


class BottomPhotoChangeWidget(action_sheet.UIAActionSheet):
    """
        Summary:
            底部的弹层
    """

    def __init__(self, parent, sheet=None, **kwargs):
        super(BottomPhotoChangeWidget, self).__init__(parent, sheet, **kwargs)
        self._sheet = self._action_sheet

    def __getattr__(self, item):

        if hasattr(self._sheet, item):
            return getattr(self._sheet, item)
        return getattr(self.base_parent, item)

    @property
    def take_photo_button(self):
        """
            Summary:
                拍照按钮
        """
        name_ = '拍照'
        return button.UIAButton(self._sheet, name=name_)

    @property
    def select_from_local_button(self):
        """
            Summary:
                本地获取按钮
        """
        name_ = '本地获取'
        return button.UIAButton(self._sheet, name=name_)

    # *************************操作方法**********************

    def tap_take_photo_button(self):
        """
            Summary:
                点击拍照按钮
        """
        log.logger.info("开始点击拍照按钮")
        self.take_photo_button.tap()
        log.logger.info("完成拍照按钮的点击")
        if self.wait_window(windows.WindowNames.PHOTO_TAKING, 10):
            log.logger.info("成功进入拍照页")
            return True
        log.logger.error("进入拍照页失败")
        return False

    def tap_select_from_local_button(self):
        """
            Summary:
                点击本地获取按钮
        """
        log.logger.info("开始点击从本地获取按钮")
        self.select_from_local_button.tap()
        log.logger.info("完成从本地获取按钮的点击")
        if self.wait_window(windows.WindowNames.PHOTO_ALBUM_PICKER, 10):
            log.logger.info("成功进入图片集选择页")
            return True
        log.logger.error("进入图片集选择页失败")
        return False

