#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:登录主节目

Authors: turinblueice
Date: 2016/7/26
"""

from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import secure_text_field
from gui_widgets.basic_widgets import window
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import button

from UIAWindows.register_sign_windows import login_friend_recommend_window

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UIAWindows import windows
from selenium.common.exceptions import TimeoutException

import time


class LoginMainWindow(base_frame_view.BaseFrameView):

    """
    Summary:
        登陆活动页

    Attributes:
        parent: 该活动页的父亲framework

    """

    def __init__(self, parent):
        super(LoginMainWindow, self).__init__(parent)

    @property
    def account_field(self):
        """
        Summary:
            帐号输入框

        """
        return text_field.UIATextField(self.parent, type='UIATextField')

    @property
    def password_field(self):
        """
        Summary:
            密码输入框
        """
        return secure_text_field.UIASecureTextField(self.parent, type='UIASecureTextField')

    @property
    def login_button(self):
        """
        Summary:
            登陆按钮
        """
        name_ = '登录'
        return button.UIAButton(self.parent, name=name_)

    # ***********************操作方法*********************************

    def input_account(self, phone_number):
        """
            Summary:
                在登陆页面输入账户手机号码

            Args:
                phone_number:手机号
        """
        log.logger.info("开始清空账号内容")
        self.account_field.clear_text_field()
        log.logger.info("账号内容清空完毕，开始输入账号")
        self.account_field.send_keys(phone_number)
        time.sleep(2)

    def input_password(self, password):
        """
            Summary:
                 在登陆页面输入密码
            Args:
                password:密码
        """
        log.logger.info("开始清空密码内容")
        self.password_field.clear_text_field()
        log.logger.info("密码内容清空完毕，开始输入密码")
        self.password_field.send_keys(password)
        time.sleep(2)

    def tap_login_button(self, auto=True):
        """
            Summary:
                点击登陆按钮
            Args:
                timeout:最大等待时间
                interval:重试间隔
                auto:True:自动判断是否首次登录，是首次登录则会跳过引导页;False:默认非首次登录
        """
        log.logger.info("开始点击登录按钮")
        self.login_button.tap()
        log.logger.info("完成点击登录按钮")
        if auto:
            #  点击登录按钮后，首先判断是否进入好友推荐页
            if self.wait_window(windows.WindowNames.LOGIN_FRIEND_RECOMMEND, 5):
                log.logger.info("登录后首先进入了好友推荐页")
                log.logger.info("点击好友推荐页的完成按钮")
                curr_friend_window = login_friend_recommend_window.LoginFriendRecommendWindow(self.parent)
                curr_friend_window.tap_finish_button()

        if self.wait_window(windows.WindowNames.IN_MAIN):
            log.logger.info("登陆成功，成功进入In主页")
            return True
        else:
            log.logger.info("登陆失败，进入In主页面失败")
            return False
