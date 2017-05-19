#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 用户中心相关case操作

Authors: Hong Quan(hongquan@itugo.com)
Date:    16/5/5 17:47
"""

from base import base_frame_view
from base import app_unit_test
from util import log

from UIAWindows.user_center_sub_windows import user_info_window
from UIAWindows.in_main_windows import user_center_tab_window

from multi_clients_manager import multi_clients_base_test
from common_actions import access_to_window


class UserCenterTestCase(app_unit_test.AppTestCase, multi_clients_base_test.MultiClientsBaseTest):

    def __init__(self, *args, **kwargs):
        super(UserCenterTestCase, self).__init__(*args, **kwargs)
        multi_clients_base_test.MultiClientsBaseTest.__init__(self, **kwargs)

    def setUp(self):

        self.create_driver(self.debug_mode)
        driver = self.get_driver()

        action = access_to_window.ActionsAccess2Window(driver)
        action.wait_for_app_launch()
        action.go_to_user_center_tab()  # 准备工作，进入个人中心tab

    def tearDown(self):
        driver = self.get_driver()
        if driver:
            driver.quit()

    def test_edit_avatar_operation(self):
        """
            test_cases/test_user_center_operations.py:UserCenterTestCase.test_edit_avatar_operation
            Summary:
                编辑头像信息
        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:
            curr_user_center_window = user_center_tab_window.UserCenterTabWindow(base_app)
            log.logger.info("点击进入用户信息页面")
            status = curr_user_center_window.tap_user_head_bar()
            self.assertTrue(status, "进入用户信息页失败")

            curr_user_info_window = user_info_window.UserInfoWindow(base_app)

            status = curr_user_info_window.upload_avatar()

            log.logger.info("验证图片上传结果")
            self.assertTrue(status, "上传图片失败")
            log.logger.info("验证结束，结果正确")

        except Exception as exp:
            log.logger.error("发现异常, case:test_edit_avatar_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'edit_avatar', exp)

    def test_select_city_operation(self):
        """
            test_cases/test_user_center_operations.py:UserCenterTestCase.test_edit_avatar_operation
            Summary:
                选择地区-选择城市
        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:
            curr_user_center_window = user_center_tab_window.UserCenterTabWindow(base_app)
            log.logger.info("点击进入用户信息页面")
            status = curr_user_center_window.tap_user_head_bar()
            self.assertTrue(status, "进入用户信息页失败")

            curr_user_info_window = user_info_window.UserInfoWindow(base_app)

            log.logger.info("选择地区为浙江杭州")
            curr_user_info_window.select_region('hangzhou')

            region_text = curr_user_info_window.region_text
            expected_text = '浙江 杭州'

            log.logger.info("验证显示的城市名")
            self.assertEqual(expected_text, region_text,
                             "显示的名称不正确，期待名称：\"{}\"，实际名称\"{}\"".format(expected_text, region_text))
            log.logger.info("验证结束，结果正确")

            log.logger.info("选择地区为浙江宁波")
            curr_user_info_window.select_region('ningbo')

            region_text = curr_user_info_window.region_text
            expected_text = '浙江 宁波'

            log.logger.info("验证显示的城市名")
            self.assertEqual(expected_text, region_text,
                             "显示的名称不正确，期待名称：\"{}\"，实际名称\"{}\"".format(expected_text, region_text))
            log.logger.info("验证结束，结果正确")

        except Exception as exp:
            log.logger.error("发现异常, case:test_select_city_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'select_city', exp)
