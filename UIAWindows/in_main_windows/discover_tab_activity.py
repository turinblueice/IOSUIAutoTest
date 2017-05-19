#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: IN主页-发现tab页面

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log

from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import tool_bar
from gui_widgets.basic_widgets import linear_layout
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import action_sheet

from UIAWindows import windows
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


class DiscoverTabActivity(base_frame_view.BaseFrameView):

    """
        Summary:
            In主页面-发现tab

        Attributes:

    """
    name = '.InActivity'

    def __init__(self, parent):
        super(DiscoverTabActivity, self).__init__(parent)
        self._scroll_view = action_sheet.RecyclerView(self.parent,
                                                      id='com.jiuyan.infashion:id/swipe_container')

    @property
    def qr_code(self):
        """
            Summary:
                二维码扫一扫
        """
        id_ = 'com.jiuyan.infashion:id/layout_qrcode'
        return tool_bar.RelativeLayout(self.parent, id=id_)

    @property
    def search_box(self):
        """
            Summary:
                搜索框
        """
        xpath_ = '//android.widget.RelativeLayout[@resource-id=\"com.jiuyan.infashion:id/header_search\"]/' \
                 'android.widget.LinearLayout[2]'
        return tool_bar.RelativeLayout(self.base_parent, xpath=xpath_)

    @property
    def sign_up(self):
        """
            Summary:
                签到
        """
        id_ = 'com.jiuyan.infashion:id/layout_signup'
        return tool_bar.RelativeLayout(self.parent, id=id_)

    @property
    def hot_topic_recycler(self):
        """
            Summary:
                热门话题左右滑动区域
        """
        id_ = 'com.jiuyan.infashion:id/tag_recycler'
        return action_sheet.RecyclerView(self.parent, id=id_)

    @property
    def hot_topic_list(self):
        """
            Summary:
                热门话题列表
        """
        rec_ = action_sheet.RecyclerView(self.parent, id='com.jiuyan.infashion:id/tag_recycler')
        return HotTopicList(rec_, type='android.widget.RelativeLayout').topic_list

    # ************************操作***************************

    def select_hot_topic(self, index=1):
        """
            Summary:
                选择热门话题
            Args:
                index:序号
        """
        log.logger.info("开始选择第{}个热门话题".format(index))
        status = self.hot_topic_list[index-1].tap()
        return status

    def swipe_topic_list(self, direction='right'):
        """
            Summary:
                左右滑动话题列表
            Args：
                direction: left:向左;right:向右
        """
        if direction == 'right':
            self.hot_topic_recycler.swipe_right_entire_recycler_view()
        elif direction == 'left':
            self.hot_topic_recycler.swipe_left_entire_recycler_view()
        else:
            log.logger.info("未指定方向")


class HotTopic(base_frame_view.BaseFrameView):

    def __init__(self, parent, item=None, **kwargs):
        super(HotTopic, self).__init__(parent)
        self.__item = item if isinstance(item, WebElement) else self.find_element(**kwargs)

    @property
    def title(self):

        return static_text.UIAStaticText(self.__item, id='com.jiuyan.infashion:id/tv_title').text

    def tap(self):

        log.logger.info("开始点击该话题")
        title = self.title
        self.__item.click()
        if self.base_parent.wait_activity(windows.ActivityNames.TOPIC_DETAIL, 10):
            log.logger.info("成功进入话题\"{}\"的详情页".format(title))
            return True
        log.logger.error("进入话题详情页失败")
        return False


class HotTopicList(base_frame_view.BaseFrameView):

    def __init__(self, parent, **kwargs):
        super(HotTopicList, self).__init__(parent)
        self.__item_list = self.find_elements(**kwargs)

    @property
    def topic_list(self):

        if self.__item_list:
            return [HotTopic(item.parent, item) for item in self.__item_list]
        return None


