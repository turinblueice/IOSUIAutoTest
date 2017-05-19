#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 图片发布页

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log

from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import tool_bar
from gui_widgets.basic_widgets import linear_layout
from gui_widgets.basic_widgets import text_field
from UIAWindows import windows

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class PublishWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            图片发布页

        Attributes:

    """

    def __init__(self, parent):
        super(PublishWindow, self).__init__(parent)

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        :return:
        """
        name_ = 'common nav back'
        return button.UIAButton(self.parent, name=name_)

    # @property
    # def photo_available_list(self):
    #     """
    #         Summary:
    #             顶栏图片列表
    #     暂时注释,目前无法获取顶部图片元素
    #     """
    #     xpath_ = '//UIAScrollView[1]/UIAButton[1]'
    #     button_ = button.UIAButton(self.parent, xpath=xpath_)
    #     return tool_bar.RelativeLayoutList(
    #         button_, type='android.widget.RelativeLayout').relative_layout_list

    @property
    def edit_box(self):
        """
            Summary:
                文本输入框
        :return:
        """

        return text_field.UIATextField(self.parent, type='UIATextView')

    @property
    def publish_button(self):
        """
            Summary:
                发布按钮
        :return:
        """
        name_ = '发布'
        return button.UIAButton(self.parent, name=name_)

    @property
    def at_button(self):
        """
            Summary:
                “@”按钮
        :return:
        """
        name_ = 'photoinfo addfriend'
        return button.UIAButton(self.parent, name=name_)

    @property
    def privacy_button(self):
        """
            Summary:
                公开按钮
        :return:
        """
        name_ = '公开'
        return button.UIAButton(self.parent, name=name_)

    @property
    def location_button(self):
        """
            Summary:
                添加位置按钮
        :return:
        """
        name_ = '位置'
        return button.UIAButton(self.parent, name=name_)

    @property
    def topic_button(self):
        """
            Summary:
                添加话题按钮
        :return:
        """
        name_ = '添加话题'
        return button.UIAButton(self.parent, name=name_)

    # **************************输入文字时出现的遮罩元素*****************************
    @property
    def confirm_button(self):
        """
            Summary:
                确定按钮
        :return:
        """
        name_ = '确定'
        return button.UIAButton(self.parent, name=name_)

    # **************************操作方法******************************

    def input_words(self, *values):
        """
            Summary:
                输入文字
        :return:
        """
        log.logger.info("开始输入文字，说点什么")
        self.edit_box.clear_text_field()
        self.edit_box.send_keys(*values)
        time.sleep(2)
        log.logger.info("完成输入")
        self.tap_confirm_button()

    def tap_publish_button(self):
        """
            Summary:
                点击完成按钮
        """
        log.logger.info("开始点击发布按钮")
        self.publish_button.tap()
        log.logger.info("完成发布按钮点击")
        if self.wait_window(windows.WindowNames.IN_MAIN, 10):
            log.logger.info("成功进入发布页")
            return True
        log.logger.error("进入发布页失败")
        return False

    def tap_confirm_button(self):
        """
            Summary:
                点击确定按钮
        """
        log.logger.info("开始点击确定按钮")
        self.confirm_button.tap()
        log.logger.info("完成确定按钮点击")
        time.sleep(2)

    def is_publish_successful(self):
        """
            Summary:
                是否发布成功
        :return:
        """

        try:
            WebDriverWait(self.base_parent, 15).until(
                EC.presence_of_element_located(
                    (MobileBy.ACCESSIBILITY_ID, '发布成功')
                )
            )
            return True
        except TimeoutException:
            return False

