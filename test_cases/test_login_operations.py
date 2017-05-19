#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:登录模块

Authors: turinblueice
Date: 2016/7/26
"""


from UIAWindows.register_sign_windows import login_main_window
from UIAWindows.in_main_windows import user_center_tab_window
from UIAWindows.user_center_sub_windows import user_setting_window

from base import base_frame_view
from base import app_unit_test
from util import log

from multi_clients_manager import multi_clients_base_test
from common_actions import access_to_window


class LoginTestCase(app_unit_test.AppTestCase, multi_clients_base_test.MultiClientsBaseTest):

    def __init__(self, *args, **kwargs):
        super(LoginTestCase, self).__init__(*args, **kwargs)
        multi_clients_base_test.MultiClientsBaseTest.__init__(self, **kwargs)

    # @classmethod
    # def setUpClass(cls):
    #
    #     cls.create_driver()
    #     log.logger.info("类执行创建driver")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     if cls.driver:
    #         cls.driver.quit()

    def setUp(self):
        self.create_driver(self.debug_mode)
        access_to_window.ActionsAccess2Window.wait_for_app_launch(12)

    def tearDown(self):
        driver = self.get_driver()
        if driver:
            driver.quit()
    
    def test_login_operation(self):
        """
            test_cases/test_login_operations.py:LoginTestCase.test_login_operation
        Summary:
            登录case

        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        thread_number = self.get_current_thread_number()
        try:

            curr_login_window = login_main_window.LoginMainWindow(base_app)

            account = self.config_model.get('account', 'account'+str(thread_number))
            password = self.config_model.get('account', 'password'+str(thread_number))
            curr_login_window.input_account(account)
            curr_login_window.input_password(password)

            log.logger.info("开始点击登录按钮")
            login_status = curr_login_window.tap_login_button()

            log.logger.info("验证登录结果,登录是否跳转成功")
            self.assertTrue(login_status, "登陆失败")

        except Exception as exp:
            log.logger.error("发现异常, case:test_login_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'login', exp)

    def test_logout_operation(self):
        """
            test_cases/test_login_operations.py:LoginTestCase.test_login_operation
        Summary:
            登出case

        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:
            common_action = access_to_window.ActionsAccess2Window(self.get_driver())
            common_action.go_to_user_center_tab()
            log.logger.info("进入用户中心tab页")
            curr_user_center_tab = user_center_tab_window.UserCenterTabWindow(base_app)

            log.logger.info("向上滑动整个屏幕，使\"设置\"出现在屏幕中")
            curr_user_center_tab.swipe_up_entire_scroll_view()

            log.logger.info("点击设置栏")
            status = curr_user_center_tab.tap_settings_bar()
            self.assertTrue(status, "没有进入用户设置页面")

            curr_user_setting_window = user_setting_window.UserSettingWindow(base_app)

            log.logger.info("向上滑动屏幕，使\"退出登录\"出现在屏幕中")
            curr_user_setting_window.swipe_up_entire_scroll_view()
            status = curr_user_setting_window.tap_logout_bar()
            self.assertTrue(status, "用户退出失败")

        except Exception as exp:
            log.logger.error("发现异常, case:test_logout_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'logout', exp)
