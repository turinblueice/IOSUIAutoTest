#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 用户中心-我的贴纸-裁减贴纸-选择想要的部分-自定义贴纸

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import static_text
from UIAWindows import windows


class CustomPasterEditorWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            用户中心-我的贴纸-裁减贴纸-选择想要的部分-自定义贴纸

        Attributes:

    """

    def __init__(self, parent):
        super(CustomPasterEditorWindow, self).__init__(parent)

    @property
    def finish_button(self):
        """
            Summary:
                完成按钮
        :return:
        """
        name_ = '完成'
        return button.UIAButton(self.parent, name=name_)

    def tap_finish_button(self):
        """
            Summary:
                点击完成按钮
        """
        log.logger.info("开始点击完成按钮")
        self.finish_button.tap()
        log.logger.info("完成完成按钮点击")
        if self.wait_window(windows.WindowNames.PASTER_MALL, 15):
            log.logger.info("成功进入我的贴纸页面")
            return True
        log.logger.error("进入我的贴纸页失败")
        return False
