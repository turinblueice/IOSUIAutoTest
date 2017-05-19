#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 图片裁剪页面

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log

from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import image


class CropperWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            图片裁剪页面,如更换头像选择图片时的裁减页面

        Attributes:

    """

    def __init__(self, parent):
        super(CropperWindow, self).__init__(parent)

    @property
    def cancel_button(self):
        """
            Summary:
                取消按钮
        """
        name_ = "取消"
        return button.UIAButton(self.parent, name=name_)

    @property
    def choose_button(self):
        """
            Summary:
                继续按钮
        """
        name_ = "选取"
        return button.UIAButton(self.parent, name=name_)

    @property
    def cropper_area(self):
        """
            Summary:
                裁剪区域
        Returns:

        """
        xpath_ = '//UIAScrollView[1]/UIAImage[1]'
        return image.UIAImage(self.base_parent, xpath=xpath_)

    # ************************操作***************************

    def tap_choose_button(self, window, timeout=10):
        """
            Summary:
                点击选取按钮
            Args:
                timeout:等待时长
                window: key_value的键值对字符串,例如'name_xxxxxx'
        """
        log.logger.info("开始点击选取按钮")
        self.next_button.tap()
        if self.wait_window(window, timeout):
            log.logger.info("成功进入目标页")
            return True
        else:
            log.logger.error("进入目标页失败")
            return False
