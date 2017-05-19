#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
    模块用法说明: 贴纸操作

    Authors: Hong Quan(hongquan@itugo.com)
    Date:    16/5/5 17:47
"""

import random

from UIAWindows.common_windows import album_picker_window
from UIAWindows.common_windows import photo_picker_window
from UIAWindows.common_windows import publish_core_window
from UIAWindows.common_windows import publish_window
from UIAWindows.photo_windows import photo_camera_window
from UIAWindows.user_center_sub_windows.user_paster_windows import choose_part_paster_window
from UIAWindows.user_center_sub_windows.user_paster_windows import custom_paster_crop_window
from UIAWindows.user_center_sub_windows.user_paster_windows import custom_paster_editor_window
from UIAWindows.user_center_sub_windows.user_paster_windows import my_own_paster_tab_window
from base import app_unit_test
from base import base_frame_view
from common_actions import access_to_window
from gui_widgets.custom_widgets import custom_paster_msgbox
from multi_clients_manager import multi_clients_base_test
from util import log


class PasterTestCase(app_unit_test.AppTestCase, multi_clients_base_test.MultiClientsBaseTest):

    def __init__(self, *args, **kwargs):
        super(PasterTestCase, self).__init__(*args, **kwargs)
        multi_clients_base_test.MultiClientsBaseTest.__init__(self, **kwargs)

    def setUp(self):

        self.create_driver(self.debug_mode)
        driver = self.get_driver()

        action = access_to_window.ActionsAccess2Window(driver)
        action.wait_for_app_launch()
        action.go_to_my_paster()  # 准备工作，进入我的贴纸页面

    def tearDown(self):
        driver = self.get_driver()
        if driver:
            driver.quit()

    def test_create_paster_operation(self):
        """
            test_cases/test_paster_operations.py:PasterTestCase.test_create_paster_operation
            Summary:
                创建贴纸
        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:
            curr_my_own_paster_tab_window = my_own_paster_tab_window.MyOwnPasterTabWindow(base_app)

            if curr_my_own_paster_tab_window.is_guide_exist():
                curr_my_own_paster_tab_window.tap_window_top()

            # 记录当前贴纸个数
            tmp_my_paster_num = len(curr_my_own_paster_tab_window.my_custom_paster_list)
            log.logger.info("当前已有贴纸数{}张".format(tmp_my_paster_num))

            curr_my_own_paster_tab_window.tap_add_paster_button()

            status = curr_my_own_paster_tab_window.select_from_gallery()
            self.assertTrue(status, "进入图片选择页失败")

            curr_album_picker_window = album_picker_window.PhotoAlbumPickerWindow(base_app)
            curr_album_picker_window.post_photo_album_list[3].tap()

            curr_photo_picker_window = photo_picker_window.PhotoPickerWindow(base_app)

            log.logger.info("选择第三张图片加工为贴纸")
            curr_photo_picker_window.post_photo_list[2].tap()

            curr_photo_crop_window = custom_paster_crop_window.CustomPasterCropWindow(base_app)
            curr_photo_crop_window.tap_next_button()

            curr_choose_part_photo_window = choose_part_paster_window.ChoosePartPasterWindow(base_app)
            curr_choose_part_photo_window.tap_continue_button()

            curr_editor_photo_window = custom_paster_editor_window.CustomPasterEditorWindow(base_app)
            curr_editor_photo_window.tap_finish_button()

            log.logger.info("验证创建的贴纸添加到了已有贴纸里面")
            now_my_paster_num = len(curr_my_own_paster_tab_window.my_custom_paster_list)
            log.logger.info("现在贴纸数目{}张".format(now_my_paster_num))

            log.logger.info("检查新增贴纸的new标记")
            self.assertTrue(curr_my_own_paster_tab_window.new_paster_icon.is_displayed(), "新增标记未出现")
            log.logger.info("新增贴纸的new标记已检测成功")

            self.assertEqual(1, now_my_paster_num-tmp_my_paster_num, "贴纸数量不一致，创建贴纸失败")

        except Exception as exp:
            log.logger.error("发现异常, case:test_paster_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'create_paster', exp)

    def test_publish_paster_available_operation(self):
        """
            test_cases/test_paster_operations.py:PasterTestCase.test_publish_paster_available_operation
            Summary:
                发布已有贴纸
        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:
            curr_my_own_paster_tab_window = my_own_paster_tab_window.MyOwnPasterTabWindow(base_app)

            # 记录当前贴纸个数
            tmp_my_paster_num = len(curr_my_own_paster_tab_window.my_custom_paster_list)
            log.logger.info("当前已有贴纸数{}张".format(tmp_my_paster_num))

            index = random.randint(0, tmp_my_paster_num-1)
            log.logger.info("点击第{}张贴纸".format(index+1))
            status = curr_my_own_paster_tab_window.choose_custom_paster(index+1)
            self.assertTrue(status, "吊起贴纸对话框失败")

            curr_paster_box = custom_paster_msgbox.CustomPasterMsgBox(base_app)
            status = curr_paster_box.tap_use_button()
            self.assertTrue(status, "使用贴纸失败")

            log.logger.info("选择图片，编辑贴纸")
            curr_camera_window = photo_camera_window.CameraWindow(base_app)
            indexes = (3, 1, 4)
            curr_camera_window.select_photos(indexes[0], indexes[1], indexes[2])
            log.logger.info("验证所选图片是否已选中")

            for index, value in enumerate(indexes, start=1):
                self.assertEqual(str(index), curr_camera_window.photo_list[value-1].selected_value,
                                 "选中序号不正确")

            log.logger.info("图片选择验证完毕")
            status = curr_camera_window.tap_next_step_button()
            self.assertTrue(status, "进入发布加工页失败")

            curr_publish_core_window = publish_core_window.PublishCoreWindow(base_app)
            status = curr_publish_core_window.tap_finish_button()
            self.assertTrue(status, "进入发布页失败")

            curr_publish_window = publish_window.PublishWindow(base_app)

            curr_publish_window.input_words(u"测试发布")
            curr_publish_window.tap_publish_button()
            log.logger.info("开始验证发布情况")
            status = curr_publish_window.is_publish_successful()
            self.assertTrue(status, "发布失败")
            log.logger.info("发布情况验证完毕")

        except Exception as exp:
            log.logger.error("发现异常, case:test_publish_paster_available_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'test_publish_paster', exp)
