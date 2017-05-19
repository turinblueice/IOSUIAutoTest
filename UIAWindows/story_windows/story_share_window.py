#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 故事分享页

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import tool_bar
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import linear_layout
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import window
from gui_widgets.basic_widgets import scroll_view
from gui_widgets.basic_widgets import action_sheet
from gui_widgets.custom_widgets import alert

from UIAWindows.common_windows import photo_picker_window
from UIAWindows.common_windows import cropper_window

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from UIAWindows import windows

import time
import random


class StoryShareWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            发布故事集-故事分享页

        Attributes:

    """

    def __init__(self, parent):
        super(StoryShareWindow, self).__init__(parent)

    @property
    def publish_success_tips(self):
        """
            Summary:
                发布成功提示——"发布成功"
        """
        return static_text.UIAStaticText(self.parent, name='发布成功!').text

    @property
    def close_button(self):
        """
            Summary:
                关闭按钮
        """
        name_ = 'album publish succ close'
        return button.UIAButton(self.parent, name=name_)

    @property
    def wechat_button(self):
        """
            Summary:
                微信好友按钮
        :return:
        """
        name_ = 'album publish succ share wecha'
        return button.UIAButton(self.parent, name=name_)

    @property
    def moments_button(self):
        """
            Summary:
                朋友圈按钮
        :return:
        """
        name_ = 'album publish succ share frien'
        return button.UIAButton(self.parent, name=name_)

    @property
    def weibo_button(self):
        """
            Summary:
                微博按钮
        :return:
        """
        name_ = 'album publish succ share weibo'
        return button.UIAButton(self.parent, name=name_)

    @property
    def qq_button(self):
        """
            Summary:
                QQ按钮
        :return:
        """
        name_ = 'album publish succ share qq'
        return button.UIAButton(self.parent, id=name_)

    @property
    def qzone_button(self):
        """
            Summary:
                QQ空间按钮
        :return:
        """
        name_ = 'album publish succ share qqzon'
        return button.UIAButton(self.parent, id=name_)

    @property
    def save_picture_button(self):
        """
            Summary:
                保存长图按钮
        :return:
        """
        name_ = 'album publish succ share downl'
        return button.UIAButton(self.parent, id=name_)

    @property
    def print_story_button(self):
        """
            Summary:
                打印故事集
        """
        name_ = '打印故事集'
        return button.UIAButton(self.parent, name=name_)

    # ************************操作***************************

    def tap_close_button(self):
        """
            Summary:
                点击关闭按钮
        :return:
        """
        log.logger.info("开始点击关闭按钮")
        self.close_button.tap()
        log.logger.info("点击完毕")
        if self.wait_window(windows.WindowNames.STORY_DETAIL, 10):
            log.logger.info("成功进入故事详情页")
            return True
        log.logger.error("进入故事详情页失败")
        return False

    def is_publish_success(self):
        """
            Summary:
                是否发布成功
        :return:
        """
        if self.wait_for_element_present(self.base_parent, timeout=10, name='发布成功!'):
            log.logger.info("发布成功")
            return True
        log.logger.error("发布失败")
        return False
