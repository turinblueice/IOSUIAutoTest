#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:该模块为主页面底部tab栏
 
Authors: turinblueice
Date:    16/3/16 16:46
"""

from base import base_frame_view
from gui_widgets.basic_widgets import button

from util import log

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UIAWindows import windows

from selenium.common import exceptions

import time


class BottomTabWidget(base_frame_view.BaseFrameView):
    """
        Summary:
            主页面底部的tab栏组件
    """

    def __init__(self, parent):
        super(BottomTabWidget, self).__init__(parent)

    @property
    def focus_tab(self):
        """
            Summary:
                关注tab
        """
        name_ = '关注'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def discovery_tab(self):
        """
            Summary:
                发现tab
        """
        name_ = '发现'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def camera_tab(self):
        """
            Summary:
                相机tab
        """
        name_ = 'paizhao'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def in_note_tab(self):
        """
            Summary:
                in记tab
        """
        name_ = 'in记'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def center_tab(self):
        """
            Summary:
                中心tab
        """
        name_ = '中心'
        return button.UIAButton(self.base_parent, name=name_)

    # ********************* 操作方法************************

    def tap_center_tab(self, timeout=10):
        """
            Summary:
                点击中心tab
            Args：
                timeout: 等待时长
        """
        log.logger.info("开始点击中心tab")
        self.center_tab.tap()
        log.logger.info("中心tab点击完毕")
        try:
            WebDriverWait(self.base_parent, timeout).until(
                EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, '我的'))
            )
            log.logger.info("成功进入中心tab页面")
            return True
        except exceptions.TimeoutException:
            log.logger.error("进入中心tab页面失败")
            return False

    def tap_focus_tab(self, timeout=10):
        """
            Summary:
                点击关注tab
            Args：
                timeout: 等待时长
        """
        log.logger.info("开始点击关注tab")
        self.focus_tab.tap()
        log.logger.info("关注tab点击完毕")
        try:
            WebDriverWait(self.base_parent, timeout).until(
                EC.presence_of_element_located(
                    (MobileBy.ACCESSIBILITY_ID, ''))  # 待实现
            )
            log.logger.info("成功进入关注tab页面")
            return True
        except exceptions.TimeoutException:
            log.logger.error("进入关注tab页面失败")
            return False

    def tap_discover_tab(self, timeout=10):
        """
            Summary:
                点击发现tab
            Args：
                timeout: 等待时长
        """
        log.logger.info("等待相机气泡消失再点击相机按钮")
        while self.wait_for_element_present(self.base_parent, timeout=5, id='com.jiuyan.infashion:id/id_fl_parster'):
            log.logger.info("相机气泡存在，继续等待5秒")
            time.sleep(5)

        log.logger.info("开始点击发现tab")
        self.discovery_tab.tap()
        log.logger.info("发现tab点击完毕")
        try:
            WebDriverWait(self.base_parent, timeout).until(
                EC.element_located_to_be_selected(
                    (MobileBy.ACCESSIBILITY_ID, '热门话题'))
            )
            log.logger.info("成功进入发现tab页面")
            return True
        except exceptions.TimeoutException:
            log.logger.error("进入发现tab页面失败")
            return False

    def tap_camera_tab(self, timeout=10):
        """
            Summary:
                点击拍照tab
            Args：
                timeout: 等待时长
        """
        log.logger.info("等待相机气泡消失再点击相机按钮")
        while self.wait_for_element_present(self.base_parent, timeout=5, id='com.jiuyan.infashion:id/id_fl_parster'):
            log.logger.info("相机气泡存在，继续等待5秒")
            time.sleep(5)

        log.logger.info("开始点击拍照tab")
        self.camera_tab.tap()
        log.logger.info("拍照tab点击完毕")
        if self.wait_window(windows.WindowNames.PHOTO_STORY_GALLERY, timeout):
            log.logger.info("成功进入相册页面")
            return True
        log.logger.error("进入相册页面失败")
        return False
