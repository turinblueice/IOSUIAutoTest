#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 登录的好友推荐页

Authors: turinblueice
Date: 2016/7/26
"""

from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import table_view
from gui_widgets.basic_widgets import image_button
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import action_sheet

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UIAWindows import windows
from selenium.common.exceptions import TimeoutException

import time


class LoginFriendRecommendWindow(base_frame_view.BaseFrameView):

    """
    Summary:
        登陆好友推荐页

    Attributes:
        parent: 该活动页的父亲framework

    """

    name = '.login.activity.FriendRecommendActivity'

    def __init__(self, parent):
        super(LoginFriendRecommendWindow, self).__init__(parent)

        self._scroll_view = table_view.UIATableView(
            self.parent, type='UIATableView')

    @property
    def title(self):
        """
            Summary:
                标题
        """
        name_ = '推荐好友'
        return static_text.UIAStaticText(self.parent, name=name_).text

    @property
    def finish_button(self):
        """
        Summary:
            完成按钮
        """
        name_ = '完成'
        return button.UIAButton(self.parent, name=name_)

    @property
    def find_friend_in_contact_button(self):
        """
            Summary:
                找一找通讯录好友
        """
        name_ = '找一找通讯录好友'
        return button.UIAButton(self.parent, id=name_)

    # ***********************操作方法*********************************

    def tap_finish_button(self):
        """
            Summary:
                点击完成按钮
        """
        log.logger.info("开始点击完成按钮")
        self.finish_button.tap()
        log.logger.info("结束完成按钮点击")
        if self.wait_window(windows.WindowNames.IN_MAIN):
            log.logger.info("成功进入主页")
            return True
        log.logger.error("进入主页失败")
        return False
