#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:话题操作case

Authors: turinblueice
Date: 2016/7/26
"""


from UIAWindows.in_main_windows import discover_tab_activity
from UIAWindows.discover_details_activities import topic_detail_activity
from UIAWindows.discover_details_activities import friend_photo_detail_activity

from base import base_frame_view
from base import app_unit_test
from util import log

from multi_clients_manager import multi_clients_base_test
from common_actions import access_to_window


class TopicTestCase(app_unit_test.AppTestCase, multi_clients_base_test.MultiClientsBaseTest):

    def __init__(self, *args, **kwargs):
        super(TopicTestCase, self).__init__(*args, **kwargs)
        multi_clients_base_test.MultiClientsBaseTest.__init__(self, **kwargs)

    def setUp(self):
        driver = self.create_driver(self.debug_mode)
        action = access_to_window.ActionsAccess2Activity(driver)

        action.wait_for_app_launch()
        action.go_to_discover_tab()

    def tearDown(self):
        driver = self.get_driver()
        if driver:
            driver.quit()

    def test_send_topic_comment_operation(self):
        """
            test_cases/test_topic_operations.py:TopicTestCase.test_send_topic_comment_operation
        Summary:
            选择话题评论

        """
        base_app = base_frame_view.BaseFrameView(self.get_driver())
        try:

            curr_discover_activity = discover_tab_activity.DiscoverTabActivity(base_app)

            log.logger.info("选择话题")
            status = curr_discover_activity.select_hot_topic(1)
            self.assertTrue(status, "进入话题详情页失败")

            curr_topic_activity = topic_detail_activity.TopicDetailActivity(base_app)
            curr_topic_activity.swipe_up_entire_scroll_view()

            curr_hot_container = curr_topic_activity.hotest_container_list[0]
            status = curr_hot_container.tap_to_submit_comment()

            self.assertTrue(status, "进入图片详情页失败")

            curr_friend_photo_activity = friend_photo_detail_activity.FriendPhotoDetailActivity(base_app)
            input_comment = u'in喜欢这个'
            curr_friend_photo_activity.input_comment(input_comment)
            curr_friend_photo_activity.tap_send_button()
            curr_friend_photo_activity.tap_back_button()

            user_name = self.config_model.get('account', 'user_name'+self.get_current_thread_number())
            self.assertEqual(user_name+' '+input_comment.encode('utf8'),
                             curr_hot_container.latest_comment, "最新的发布文字和刚刚发布的文字不一致")

        except Exception as exp:
            log.logger.error("发现异常, case:test_send_topic_topic_operation执行失败")
            self.raise_exp_and_save_screen_shot(base_app, 'send_topic', exp)

    # 双击尚未实现，暂时注释
    # def test_like_newest_photo_operation(self):
    #     """
    #         test_cases/test_topic_operations.py:TopicTestCase.test_like_newest_photo_operation
    #     Summary:
    #         选择话题评论
    #
    #     """
    #     base_app = base_frame_view.BaseFrameView(self.get_driver())
    #     try:
    #
    #         curr_discover_activity = discover_tab_activity.DiscoverTabActivity(base_app)
    #
    #         log.logger.info("选择话题")
    #         status = curr_discover_activity.select_hot_topic(1)
    #         self.assertTrue(status, "进入话题详情页失败")
    #
    #         curr_topic_activity = topic_detail_activity.TopicDetailActivity(base_app)
    #         curr_topic_activity.tap_newest_tab()
    #
    #         curr_topic_activity.swipe_up_half_scroll_view()
    #         curr_newest_photo = curr_topic_activity.newest_photo_album_list[0]
    #
    #         count = int(curr_newest_photo.like_count) if not curr_newest_photo.like_count == 'like' else 0
    #         curr_newest_photo.double_tap()
    #         self.assertEqual(count+1, int(curr_newest_photo.like_count), "点赞数不一致")
    #
    #     except Exception as exp:
    #         log.logger.error("发现异常, case:test_like_newest_photo_operation执行失败")
    #         self.raise_exp_and_save_screen_shot(base_app, 'like_photo', exp)

