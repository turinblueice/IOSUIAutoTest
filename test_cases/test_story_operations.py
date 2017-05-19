#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 发表故事集操作

Authors: Hong Quan(hongquan@itugo.com)
Date:    16/5/5 17:47
"""

import random

from UIAWindows.common_windows import story_gallery_window
from UIAWindows.story_windows import story_edit_window
from UIAWindows.story_windows import story_preview_window
from UIAWindows.story_windows import story_setting_window
from UIAWindows.story_windows import story_share_window
from base import app_unit_test
from base import base_frame_view
from common_actions import access_to_window
from multi_clients_manager import multi_clients_base_test
from util import log


class StoryTestCase(app_unit_test.AppTestCase, multi_clients_base_test.MultiClientsBaseTest):

    def __init__(self, *args, **kwargs):
        super(StoryTestCase, self).__init__(*args, **kwargs)
        multi_clients_base_test.MultiClientsBaseTest.__init__(self, **kwargs)

    def setUp(self):

        self.create_driver(self.debug_mode)
        driver = self.get_driver()

        action = access_to_window.ActionsAccess2Window(driver)
        action.wait_for_app_launch()
        action.go_to_publish_story_tab()

    def tearDown(self):
        driver = self.get_driver()
        if driver:
            driver.quit()

    def test_publish_story_operation(self):
        """
            test_cases/test_story_operations.py:StoryTestCase.test_publish_story_operation
            Summary:
                发布故事集
        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:
            curr_gallery_window = story_gallery_window.StoryGalleryWindow(base_app)

            #  当前选择的相册内的照片列表
            curr_photo_list = curr_gallery_window.story_photo_list

            # 相册集中的照片，为了排除底部四张照片被遮罩tab的干扰，最多选择前12张
            max_photo_count = len(curr_photo_list) if len(curr_photo_list) < 12 else 12

            picked_count = random.randint(1, max_photo_count)  # 选择的照片数量
            log.logger.info("随机选择{}张照片".format(picked_count))

            for index in random.sample(xrange(max_photo_count), picked_count):
                log.logger.info("选择第{}张照片".format(index+1))
                curr_photo_list[index].select()
                log.logger.info("验证该图片有没有被选中")
                self.assertTrue(curr_photo_list[index].is_selected(), "该图片没有被选中")
                log.logger.info("该图片已被选中")

            log.logger.info("验证已选中的图片的数目")
            self.assertEqual(str(picked_count), curr_gallery_window.selected_story_photo_count, "选择的图片数量不一致")

            curr_gallery_window.tap_story_continue_button()

            curr_story_edit_window = story_edit_window.StoryEditWindow(base_app)
            curr_story_edit_window.diary_cover_detail.input_diary_name(u'第一篇文章')
            curr_story_edit_window.diary_cover_detail.input_diary_beginning(u'文章开头')
            curr_story_edit_window.tap_preview_button()

            curr_story_preview_window = story_preview_window.StoryPreviewWindow(base_app)
            curr_story_preview_window.tap_next_button()

            curr_story_setting_window = story_setting_window.StorySettingWindow(base_app)
            curr_story_setting_window.tap_finish_button()

            curr_story_share_window = story_share_window.StoryShareWindow(base_app)
            self.assertTrue(curr_story_share_window.is_publish_success(), "发布日记未成功")

            status = curr_story_share_window.tap_close_button()
            self.assertTrue(status, "进入in主页失败")

        except Exception as exp:
            log.logger.error("发现异常, case:test_publish_story_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'publish_story', exp)

    def test_publish_story_from_in_gallery_operation(self):
        """
            test_cases/test_story_operations.py:StoryTestCase.test_publish_story_from_in_gallery_operation
            Summary:
                发布故事集-点击写故事-点击照片-点击in记相册选择照片上传
        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:
            curr_gallery_window = story_gallery_window.StoryGalleryWindow(base_app)

            #  点击上方相册选择列表选择IN相册
            curr_gallery_window.tap_album_droplist()
            curr_gallery_window.tap_in_diary_album()
            log.logger.info("随机选择几张照片")
            indexes = [1, 3, 4]
            curr_gallery_window.select_photo_from_in_diary(indexes)

            log.logger.info("验证已选中的图片的数目")
            self.assertEqual(str(len(indexes)), curr_gallery_window.selected_story_photo_count, "选择的图片数量不一致")

            curr_gallery_window.tap_story_continue_button()

            curr_story_edit_window = story_edit_window.StoryEditWindow(base_app)
            curr_story_edit_window.diary_cover_detail.input_diary_name(u'in记相册发布文章')
            curr_story_edit_window.diary_cover_detail.input_diary_beginning(u'in记相册发布文章，发布文章开头')
            curr_story_edit_window.tap_preview_button()

            curr_story_preview_window = story_preview_window.StoryPreviewWindow(base_app)
            curr_story_preview_window.tap_next_button()

            curr_story_setting_window = story_setting_window.StorySettingWindow(base_app)
            curr_story_setting_window.tap_finish_button()

            curr_story_share_window = story_share_window.StoryShareWindow(base_app)
            self.assertTrue(curr_story_share_window.is_publish_success(), "发布日记未成功")

            status = curr_story_share_window.tap_close_button()
            self.assertTrue(status, "进入in主页失败")

        except Exception as exp:
            log.logger.error("发现异常, case:test_publish_story_from_in_gallery_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'publish_story_from_in_gallery', exp)
