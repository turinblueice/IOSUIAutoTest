#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:好友图片详情页

Authors: turinblueice
Date: 2016/9/10
"""

from base import base_frame_view
from util import log

from gui_widgets.basic_widgets import window
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import linear_layout
from gui_widgets.basic_widgets import action_sheet
from gui_widgets.basic_widgets import text_field

from appium.webdriver import WebElement
from UIAWindows import windows
import time


class FriendPhotoDetailActivity(base_frame_view.BaseFrameView):

    """
        Summary:
            好友图片详情页面

        Attributes:

    """
    name = '.friend.activity.FriendPhotoDetailActivity'  # 裁剪图片activity名称

    def __init__(self, parent):
        super(FriendPhotoDetailActivity, self).__init__(parent)
        #  等待页面网络请求进行初始化
        self.wait_for_element_present(self.parent, id='com.jiuyan.infashion:id/friend_title_bar')
        self._scroll_view = window.FrameLayout(self.parent,
                                               id='com.jiuyan.infashion:id/lv_friend_photo_detail_comment_list')

    # **************************底部发表控件*******************************
    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        """
        id_ = 'com.jiuyan.infashion:id/iv_friend_back'
        return image.ImageView(self.parent, id=id_)

    @property
    def edit_box(self):
        """
            Summary:
                订阅成功提示
        """
        id_ = 'com.jiuyan.infashion:id/et_content'
        return text_field.EditText(self.parent, id=id_)

    @property
    def send_button(self):
        """
            Summary:
                发送按钮
        """
        id_ = 'com.jiuyan.infashion:id/tv_send'
        return static_text.TextView(self.parent, id=id_)

    # **************************操作方法*****************************
    def tap_back_button(self):
        """
            Summary:
                点击返回按钮
        """
        log.logger.info("开始点击返回按钮")
        self.back_button.tap()
        if self.wait_activity(windows.ActivityNames.TOPIC_DETAIL, 10):
            log.logger.info("成功返回到话题页")
            return True
        log.logger.error("返回话题页失败")
        return False

    def input_comment(self, value):
        """
            Summary:
                输入文字
        """
        log.logger.info("开始输入文字")
        self.edit_box.clear_text_field()
        self.edit_box.set_text(value)
        time.sleep(2)
        log.logger.info("完成输入")

    def tap_send_button(self):
        """
            Summary:
                点击发送按钮
        """
        log.logger.info("开始点击发送按钮")
        self.send_button.tap()
        time.sleep(2)
        log.logger.info("完成发送")