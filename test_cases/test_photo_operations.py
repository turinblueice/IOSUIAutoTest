#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 发表图片操作

Authors: Hong Quan(hongquan@itugo.com)
Date:    16/5/5 17:47
"""

from base import base_frame_view
from base import app_unit_test
from util import log

from UIAWindows.common_windows import story_gallery_window
from UIAWindows.common_windows import publish_core_window
from UIAWindows.common_windows import publish_window

from multi_clients_manager import multi_clients_base_test
from common_actions import access_to_window
import random


class PhotoTestCase(app_unit_test.AppTestCase, multi_clients_base_test.MultiClientsBaseTest):

    def __init__(self, *args, **kwargs):
        super(PhotoTestCase, self).__init__(*args, **kwargs)
        multi_clients_base_test.MultiClientsBaseTest.__init__(self, **kwargs)

    def setUp(self):

        driver = self.create_driver(self.debug_mode)

        action = access_to_window.ActionsAccess2Window(driver)
        action.wait_for_app_launch()
        action.go_to_publish_photo_tab()

    def tearDown(self):
        driver = self.get_driver()
        if driver:
            driver.quit()

    def test_publish_photo_operation(self):
        """
            test_cases/test_photo_operations.py:PhotoTestCase.test_publish_photo_operation
            Summary:
                发布图片
        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:
            curr_gallery_window = story_gallery_window.StoryGalleryWindow(base_app)

            log.logger.info("切换一次底部tab，避免\"发布故事集\"的引导遮罩对选取图片的干扰")
            curr_gallery_window.tap_story_tab()
            curr_gallery_window.tap_photo_tab()

            #  当前图片tab下的图片列表
            curr_photo_list = curr_gallery_window.image_photo_list
            photo_count = curr_gallery_window.image_photo_enable_picked_count

            picked_count = 3
            log.logger.info("随机选{}张图片".format(picked_count))
            #  选随机选择几张图片,为了排除底部遮罩tab的干扰，图片最多选择11张
            max_pick_count = photo_count if photo_count < 11 else 11
            for index, photo_index in enumerate(random.sample(xrange(max_pick_count), picked_count)):
                log.logger.info("选择第{}张照片,相册中的第{}张照片".format(index+1, photo_index+1))
                curr_photo_list[photo_index].select()
                log.logger.info("验证该图片有没有被选中")
                self.assertEqual(str(index+1), curr_photo_list[photo_index].check_value, "该图片没有被选中")
                log.logger.info("该图片已被选中")

            log.logger.info("验证已选中的图片的数目")
            self.assertEqual(str(picked_count), curr_gallery_window.selected_photo_count, "选择的图片数量不一致")
            log.logger.info("已完成对已选图片数目的验证")

            curr_gallery_window.tap_photo_continue_button()

            curr_publish_core_window = publish_core_window.PublishCoreWindow(base_app)

            if curr_publish_core_window.is_guide_mask_exist():
                log.logger.info("点击屏幕中央，避免引导遮罩干扰")
                curr_publish_core_window.tap_window_center()

            log.logger.info("验证发布加工页的图片数")
            self.assertEqual(picked_count, len(curr_publish_core_window.photo_available_list),
                             "发布加工页面图片数目不正确")

            curr_publish_core_window.tap_finish_button()

            curr_publish_window = publish_window.PublishWindow(base_app)

            curr_publish_window.input_words(u"测试图片发布")
            curr_publish_window.tap_publish_button()
            log.logger.info("开始验证发布情况")
            status = curr_publish_window.is_publish_successful()
            self.assertTrue(status, "发布失败")

        except Exception as exp:
            log.logger.error("发现异常, case:test_publish_photo_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'publish_photo', exp)

