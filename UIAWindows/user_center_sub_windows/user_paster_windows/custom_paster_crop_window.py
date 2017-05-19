#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 用户中心-我的贴纸-选择照片-裁减贴纸

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import button
from UIAWindows import windows


class CustomPasterCropWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            用户中心-我的贴纸-选择照片-裁减贴纸

        Attributes:

    """

    def __init__(self, parent):
        super(CustomPasterCropWindow, self).__init__(parent)

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        """
        name_ = "push back"
        return button.UIAButton(self.parent, name=name_)

    @property
    def next_button(self):
        """
            Summary:
                继续按钮
        """
        name_ = "继续"
        return button.UIAButton(self.parent, name=name_)

    @property
    def change_image_button(self):
        """
            Summary:
                换一张
        Returns:

        """
        name_ = '换一张'
        return button.UIAButton(self.parent, name=name_)

    # ************************操作***************************

    def tap_next_button(self, timeout=10):
        """
            Summary:
                点击继续按钮
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击确认按钮")
        self.next_button.tap()
        if self.wait_window(windows.WindowNames.CHOOSE_PART_PASTER, timeout):
            log.logger.info("成功进入选择想要的部分页")
            return True
        else:
            log.logger.error("进入选择想要的部分页失败")
            return False

