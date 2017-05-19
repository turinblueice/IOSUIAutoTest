#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 用户中心-设置页面

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import table_cell
from gui_widgets.basic_widgets import table_view

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from UIAWindows import windows

import time


class UserSettingWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            用户中心-设置页面

        Attributes:

    """
    name = windows.WindowNames.USER_SETTING

    def __init__(self, parent):
        super(UserSettingWindow, self).__init__(parent)
        self._scroll_view = table_view.UIATableView(self.parent, type='UIATableView')

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        """
        return button.UIAButton(self.parent, type='UIAButton')

    @property
    def title_bar(self):
        """
            Summary:
                标题-设置
        """
        return static_text.UIAStaticText(self.parent, type='UIAStaticText').text

    @property
    def logout_bar(self):
        """
            Summary:
                退出栏
        """
        name_ = "退出登录"
        return table_cell.UIATableCell(self.parent, name=name_)

    # ************************操作***************************

    def tap_logout_bar(self, accept=True, timeout=10):
        """
            Summary:
                点击退出
            Args:
                accept: True:点击提示框的确认退出;False:点击提示框的取消退出
                timeout:等待时长
        """
        log.logger.info("开始点击退出登录")
        self.logout_bar.tap()
        log.logger.info("等待提示框弹出")
        time.sleep(3)

        location = self.get_location(self.logout_bar)
        if accept:
            log.logger.info("开始点击确认退出按钮")
            location = (location[0], location[1]-self.logout_bar.size['height'])
            self.base_parent.tap([location])
            if self.wait_window(windows.WindowNames.LOGIN_MAIN, timeout):
                log.logger.info("成功退出登录")
                return True
            else:
                log.logger.info("退出登录失败")
                return False
        else:
            log.logger.info("开始点击取消按钮")
            self.base_parent.tap([location])
            if self.wait_window(self.name, timeout):
                log.logger.info("成功取消退出登录")
                return True
            else:
                log.logger.info("取消退出登录失败")
                return False


