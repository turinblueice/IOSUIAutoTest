#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: IN主页-关注tab页面

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

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


class FocusTabActivity(base_frame_view.BaseFrameView):

    """
        Summary:
            In主页面-关注tab

        Attributes:

    """
    name = '.InActivity'

    def __init__(self, parent):
        super(FocusTabActivity, self).__init__(parent)
        #  等待页面网络请求进行初始化
        self.wait_for_element_present(self.parent, id='com.jiuyan.infashion:id/in_title_bar')
        self._scroll_view = action_sheet.RecyclerView(self.parent,
                                                      id='com.jiuyan.infashion:id/rv_attention_main_listview')

    @property
    def in_title_bar(self):
        """
            Summary:
                标题栏
        """
        id_ = 'com.jiuyan.infashion:id/in_title_bar'
        return tool_bar.RelativeLayout(self.parent, id=id_)

    @property
    def new_friend_attention_button(self):
        """
            Summary:
                新增朋友提醒按钮
        """
        id_ = 'com.jiuyan.infashion:id/msg_attention_friend'
        return tool_bar.RelativeLayout(self.parent, id=id_)

    @property
    def drop_list_button(self):
        """
            Summary:
                下拉标题
        """
        id_ = "com.jiuyan.infashion:id/tv_attention_tab_current"
        return static_text.TextView(self.parent, id=id_)

    @property
    def drop_list_title(self):
        """
            Summary:
                下拉列表标题
        """
        id_ = "com.jiuyan.infashion:id/tv_attention_tab_current"
        return static_text.TextView(self.parent, id=id_).text

    @property
    def add_friend_button(self):
        """
            Summary:
                新增朋友按钮
        """
        id_ = 'com.jiuyan.infashion:id/iv_attention_friend_add'
        return image.ImageView(self.parent, id=id_)

    # ************************操作***************************
    def is_friend_attention_exist(self):
        """
            Summary:
                新增好友提醒是否存在
        :return:
        """
        if self.wait_for_element_present(self.parent, id='com.jiuyan.infashion:id/msg_attention_friend'):
            return True
        return False

    def tap_drop_list_button(self, timeout=10):
        """
            Summary:
                点击下拉列表
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击下拉列表")
        self.drop_list_button.tap()
        log.logger.info("完成下拉列表的点击")
        time.sleep(timeout)

    def select_drop_item(self, index=1):
        """
            Summary:
                选择下拉列表选项
            Args:
                index： 下拉列表序号，1,2
        """
        title_bar = self.in_title_bar
        start_x = title_bar.location['x'] + title_bar.size['width']/2
        start_y = title_bar.location['y'] + title_bar.size['height']/2 + 3

        log.logger.info("开始点击第{}个列表选项")
        #  根据像素坐标点击
        self.base_parent.tap([(start_x, start_y+title_bar['height']*index)])
        log.logger.info("已经完成点击")
        time.sleep(3)

    def tap_add_friend_button(self, timeout=10):
        """
            Summary:
                点击添加朋友按钮
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击添加朋友按钮")
        self.add_friend_button.tap()
        if self.wait_activity(windows.ActivityNames.ADD_FRIEND, timeout):
            log.logger.info("成功进入添加好友页")
            return True
        else:
            log.logger.error("进入添加还有页失败")
            return False