#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: IN主页-中心tab页面

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log

from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import table_view
from gui_widgets.basic_widgets import table_cell
from gui_widgets.basic_widgets import button

from UIAWindows import windows

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


class UserCenterTabWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            In主页面-用户中心tab

        Attributes:

    """

    def __init__(self, parent):
        super(UserCenterTabWindow, self).__init__(parent)
        self._scroll_view = table_view.UIATableView(self.parent, type='UIATableView')

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        """
        return button.UIAButton(self.parent, type='UIAButton')

    @property
    def title(self):
        """
            Summary:
                活动页标题
        """
        return static_text.UIAStaticText(self.parent, type='UIAStaticText').text

    @property
    def user_head_bar(self):
        """
            Summary:
                用户头部信息栏，包括头像
        """
        xpath_ = '//UIAApplication[1]/UIAWindow/UIATableView[1]/UIAButton[1]'
        return button.UIAButton(self.base_parent, xpath=xpath_)

    @property
    def my_friends_bar(self):
        """
            Summary:
                我的好友栏
        """
        name_ = '我的好友'
        return table_cell.UIATableCell(self.parent, name=name_)

    @property
    def paster_bar(self):
        """
            Summary:
                我的贴纸栏
        """
        name_ = '我的贴纸'
        return table_cell.UIATableCell(self.parent, name=name_)

    @property
    def setting_bar(self):
        """
            Summary:
                设置栏
        """
        name_ = '设置'
        return table_cell.UIATableCell(self.parent, name=name_)

    # ************************操作***************************

    def tap_user_head_bar(self, timeout=10):
        """
            Summary:
                点击用户头部信息栏
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击个人中心-头部信息栏")
        self.user_head_bar.tap()
        if self.wait_window(windows.WindowNames.USER_INFO, timeout):
            log.logger.info("成功进入个人信息设置页")
            return True
        else:
            log.logger.error("进入个人信息设置页失败")
            return False

    def tap_paster_bar(self, timeout=10):
        """
            Summary:
                点击贴纸栏
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击个人中心-贴纸栏")
        self.paster_bar.tap()
        if self.wait_window(windows.WindowNames.PASTER_MALL, timeout):
            log.logger.info("成功进入贴纸商城页")
            return True
        else:
            log.logger.error("进入贴纸商城页失败")
            return False

    def tap_friends_bar(self, timeout=10):
        """
            Summary:
                点击我的好友
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击个人中心-我的好友")
        self.my_friends_bar.tap()
        if self.wait_window(windows.WindowNames.USER_CENTER_FRIEND, timeout):
            log.logger.info("成功进入我的好友")
            return True
        else:
            log.logger.error("点击进入我的好友页失败")
            return False

    def tap_settings_bar(self, timeout=10):
        """
            Summary:
                点击设置栏
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击个人中心-设置")
        self.setting_bar.tap()
        if self.wait_window(windows.WindowNames.USER_SETTING, timeout):
            log.logger.info("成功进入用户设置页")
            return True
        else:
            log.logger.error("点击设置进入用户设置页失败")
            return False
