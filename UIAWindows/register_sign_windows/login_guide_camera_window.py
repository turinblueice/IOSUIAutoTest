#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 登录的引导页

Authors: turinblueice
Date: 2016/7/26
"""

from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import window
from gui_widgets.basic_widgets import image_button
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import action_sheet

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UIAWindows import windows
from selenium.common.exceptions import TimeoutException

import time


class LoginGuideCameraWindow(base_frame_view.BaseFrameView):

    """
    Summary:
        登陆引导页

    Attributes:
        parent: 该活动页的父亲framework

    """

    name = '.login.Window.GuideCameraWindow'

    def __init__(self, parent):
        super(LoginGuideCameraWindow, self).__init__(parent)

    @property
    def camera_guide_login(self):
        """
            Summary:
                登录页的摄像头
        :return:
        """
        id_ = 'com.jiuyan.infashion:id/iv_guide_camera'
        return image.ImageView(self.parent, id=id_)

    @property
    def skip_guide_login_button(self):
        """
            Summary:
                登录引导页的跳过，首次安装会出现
        :return:
        """
        id_ = 'com.jiuyan.infashion:id/tv_guide_skip'
        return static_text.TextView(self.parent, id=id_)

    @property
    def skip_dialogue_button(self):
        """
            Summary:
                弹出框的跳过按钮
        :return:
        """
        id_ = 'com.jiuyan.infashion:id/dialog_guide_camera_cancel'
        return static_text.TextView(self.parent, id=id_)

    @property
    def take_a_photo_dialogue_button(self):
        """
            Summary:
                弹出框的’拍一张‘按钮
        """
        id_ = 'com.jiuyan.infashion:id/dialog_guide_camera_confirm'
        return static_text.TextView(self.parent, id=id_)

    # ***********************操作方法*********************************

    def tap_skip_button(self, skip=True):
        """
            Summary:
                跳过引导
            Args:
                skip:True:点击提示框的跳过按钮，False：点击提示框的拍一张按钮
        """
        log.logger.info("点击跳过引导页")
        self.skip_guide_login_button.tap()
        log.logger.info("点击完毕")
        try:
            WebDriverWait(self.base_parent, 10).until(
                EC.presence_of_element_located(
                    (MobileBy.ID, 'com.jiuyan.infashion:id/dialog_guide_camera_content'))
            )
            log.logger.info("弹出了提示框")
            if skip:
                log.logger.info("点击提示框的跳过按钮")
                self.skip_dialogue_button.tap()
                log.logger.info("点击完毕")
                if self.wait_window(windows.WindowNames.IN_MAIN, 10):
                    log.logger.info("成功进入In主页")
                    return True
                log.logger.error("进入In主页失败")
                return False
            else:
                log.logger.info("点击拍一张按钮")
                self.take_a_photo_dialogue_button.tap()
                log.logger.info("点击完毕")
                if self.wait_window(windows.WindowNames.PHOTO_STORY_GALLERY, 10):
                    log.logger.info("成功进入图片选择页")
                    return True
                log.logger.error("进入图片选择页失败")
                return False
        except TimeoutException:
            log.logger.error("没有出现提示框")
            return False

