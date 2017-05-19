#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 用户中心-我的贴纸-点击添加贴纸-选择想要的部分

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import static_text
from UIAWindows import windows


class ChoosePartPasterWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            用户中心-我的贴纸-制作自定义贴纸-选择图片-选择想要的部分

        Attributes:

    """

    def __init__(self, parent):
        super(ChoosePartPasterWindow, self).__init__(parent)

    @property
    def continue_button(self):
        """
            Summary:
                继续按钮
        :return:
        """
        name_ = '继续'
        return button.UIAButton(self.parent, name=name_)

    def tap_continue_button(self):
        """
            Summray:
                点击继续按钮
        """
        log.logger.info("开始点击继续按钮")
        self.continue_button.tap()
        log.logger.info("完成继续按钮点击")
        if self.wait_window(windows.WindowNames.CUSTOM_PASTER_EDITOR, 10):
            log.logger.info("成功进入贴纸搭配页")
            return True
        log.logger.error("进入贴纸搭配页失败")
        return False
