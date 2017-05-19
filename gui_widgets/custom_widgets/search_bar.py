#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:该模块为搜索框的封装
 
Authors: turinblueice
Date:    16/3/16 16:46
"""

from base import base_frame_view
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import image_button
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import linear_layout
from gui_widgets.basic_widgets import window
from util import log

from UIAWindows import windows

import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SearchBar(base_frame_view.BaseFrameView):

    def __init__(self, parent, **kwargs):
        super(SearchBar, self).__init__(parent)
        if kwargs:
            self.__linear_layout = linear_layout.LinearLayout(self.parent, **kwargs)
        else:
            self.__id = 'com.jiuyan.infashion:id/layout_search'  # 搜索栏的ID
            self.__linear_layout = linear_layout.LinearLayout(self.parent, id=self.__id)

    @property
    def search_box(self):
        """
            Summary:
                搜索文本框
        """
        id_ = 'com.jiuyan.infashion:id/searchbox'
        return text_field.EditText(self.__linear_layout, id=id_)

    @property
    def cancel_search(self):
        """
            Summary:
                取消搜索
        """
        id_ = 'com.jiuyan.infashion:id/btn_cancel'
        return static_text.TextView(self.__linear_layout, id=id_)

    # *********************方法***************************

    def input_search_value(self, *value):
        """
            Summary:
                输入搜索内容
        """
        log.logger.info("清空搜索框")
        self.search_box.clear_text_field()
        log.logger.info("输入搜索内容")
        self.search_box.send_keys(*value)
        log.logger.info("搜索内容输入完毕")
        time.sleep(2)

    def tap_cancel_button(self):
        """
            Summary:
                点击删除文字
        """
        log.logger.info("点击取消搜索")
        self.cancel_search.tap()
        log.logger.info("已取消搜索")
        time.sleep(2)


class PasterSearchBar(SearchBar):
    """
        Summary:
            贴纸搜索栏
    """
    center_tab_title_value = u'我的'  # 中心tab的标题

    def __init__(self, parent):
        super(PasterSearchBar, self).__init__(parent)

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        """
        id_ = 'com.jiuyan.infashion:id/img'
        return image.ImageView(self.__linear_layout, id=id_)

    def tap_back_button(self, timeout=10):
        """
            Summary:
                点击返回
        """
        log.logger.info("点击返回按钮")
        self.back_button.tap()
        try:
            WebDriverWait(self.base_parent, timeout).until(
                EC.text_to_be_present_in_element((MobileBy.ID, 'com.jiuyan.infashion:id/title_bar'),
                                                 self.center_tab_title_value)
            )
            log.logger.info("成功进入中心tab页面")
            return True
        except TimeoutException:
            log.logger.error("进入中心tab页面失败")
            return False


