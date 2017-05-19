#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 用户中心-我的贴纸

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import button

from gui_widgets.custom_widgets import search_bar

from appium.webdriver import WebElement
import time


class UserPasterWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            用户中心-我的贴纸

        Attributes:

    """

    def __init__(self, parent):
        super(UserPasterWindow, self).__init__(parent)
        self._scroll_view = None

    @property
    def scroll_view(self):
        return self._scroll_view

    @property
    def search_bar(self):
        """
            Summary:
                搜索栏
        """
        return search_bar.PasterSearchBar(self.parent)

    @property
    def my_own_tab(self):
        """
            Summary:
                “我的”tab
        :return:
        """
        name_ = '我的'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def recommend_tab(self):
        """
            Summary:
                “推荐”tab
        :return:
        """
        name_ = '推荐'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def decoration_tab(self):
        """
            Summary:
                “装饰”tab
        :return:
        """
        name_ = '装饰'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def cartoon_tab(self):
        """
            Summary:
                “卡通”tab
        :return:
        """
        name_ = '卡通'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def words_tab(self):
        """
            Summary:
                “文字”tab
        :return:
        """
        name_ = '文字'
        return button.UIAButton(self.base_parent, name=name_)

    @property
    def theme_tab(self):
        """
            Summary:
                “主题”tab
        :return:
        """
        name_ = '主题'
        return button.UIAButton(self.base_parent, name=name_)


