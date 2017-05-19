#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 故事预览页

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import collection_view


from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from UIAWindows import windows

import time
import random


class StoryPreviewWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            发布故事集-故事预览页

        Attributes:

    """

    def __init__(self, parent):
        super(StoryPreviewWindow, self).__init__(parent)

        # 滑动区域
        self._scroll_view = collection_view.UIACollectionView(
            self.parent, type='UIATableView')

    @property
    def next_button(self):
        """
            Summary:
                预览按钮
        :return:
        """
        name_ = '下一步'
        return button.UIAButton(self.parent, name=name_)

    # ************************操作***************************

    def tap_next_button(self):
        """
            Summary:
                点击下一步按钮
        :return:
        """
        log.logger.info("开始点击下一步按钮")
        self.next_button.tap()
        log.logger.info("点击完毕")
        if self.wait_window(windows.WindowNames.STORY_SETTING, 10):
            log.logger.info("成功进入故事设置页")
            return True
        log.logger.error("进入故事设置页失败")
        return False
