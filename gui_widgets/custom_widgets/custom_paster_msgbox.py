#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:自定义贴纸对话框
 
Authors: turinblueice
Date:    16/3/16 16:46
"""

from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import button

from UIAWindows import windows

import time


class CustomPasterMsgBox(base_frame_view.BaseFrameView):
    """
        Summary:
            自定义贴纸对话框
    """

    def __init__(self, parent):
        super(CustomPasterMsgBox, self).__init__(parent)

    @property
    def title(self):
        """
            Summary:
                对话框的标题
        """
        return static_text.UIAStaticText(self.base_parent,
                                         xpath="//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]").text

    @property
    def use_immediate_button(self):
        """
            Summary:
                立即使用按钮
        """
        name_ = '立即使用'
        return button.UIAButton(self.parent, name=name_)

    @property
    def cancel_button(self):
        """
            Summary:
                取消按钮
        """
        name_ = 'cancel'
        return button.UIAButton(self.parent, name=name_)

    # **************************操作方法****************************

    def tap_use_button(self):
        """
            Summary:
                点击立即使用按钮
        :return:
        """
        log.logger.info("开始点击立即使用按钮")
        self.use_immediate_button.tap()
        log.logger.info("完成点击")
        if self.wait_window(windows.WindowNames.CAMERA, 10):
            log.logger.info("成功进入拍照照片编辑页")
            return True
        log.logger.error("进入拍照照片编辑页失败")
        return False
