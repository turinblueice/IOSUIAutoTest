#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 个人资料/in记主页

Authors: turinblueice
Date: 2016/7/26
"""

from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import collection_view
from gui_widgets.basic_widgets import image_button
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import linear_layout
from gui_widgets.basic_widgets import action_sheet

from appium.webdriver import WebElement

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UIAWindows import windows
from selenium.common.exceptions import TimeoutException

import time


class PersonalMainWindow(base_frame_view.BaseFrameView):

    """
    Summary:
        个人资料/in记主页

    Attributes:
        parent: 该活动页的父亲framework

    """

    def __init__(self, parent):
        super(PersonalMainWindow, self).__init__(parent)

        self._scroll_view = collection_view.UIACollectionView(self.parent, type='UIACollectionView')

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        """
        id_ = 'diary othersdiaryback'
        return button.UIAButton(self.parent, id=id_)

    @property
    def live_button(self):
        """
            Summary:
                ta的直播按钮
        """
        id_ = 'Ta的直播'
        return button.UIAButton(self.parent, id=id_)

    @property
    def follow_button(self):
        """
            Summary:
                关注按钮
        """
        id_ = ' 关注'
        return button.UIAButton(self.parent, id=id_)

    @property
    def unfollow_button(self):
        """
            Summary:
                取消关注按钮
        """
        id_ = '取消关注'
        return button.UIAButton(self.parent, id=id_)

    @property
    def im_button(self):
        """
            Summary:
                聊天按钮
        """
        id_ = ' 聊天'
        return button.UIAButton(self.parent, id=id_)

    # ****************************封面信息**************************************
    # IOS无法抓取控件
    # @property
    # def cover(self):
    #     """
    #         Summary:
    #             in记封面
    #     Returns:
    #
    #     """
    #     id_ = 'com.jiuyan.infashion:id/diary_user_header_holder'
    #     return frame_layout.FrameLayout(self.parent, id=id_)

    @property
    def user_nickname(self):
        """
            Summary:
                用户名称
        """

        return static_text.UIAStaticText(self.parent, type='UIAStaticText').text
    
    #IOS无法抓取控件
    # @property
    # def menu(self):
    #     """
    #         Summary:
    #             更多菜单
    #     """
    #     id_ = 'com.jiuyan.infashion:id/diary_user_header_menu'
    #     return image_view.ImageView(self.parent, id=id_)
    #
    # @property
    # def fans(self):
    #     """
    #         Summary:
    #             粉丝显示
    #     """
    #     id_ = 'com.jiuyan.infashion:id/diary_user_header_fans'
    #     return linear_layout.LinearLayout(self.parent, id=id_)
    #
    # @property
    # def fans_number(self):
    #     """
    #         Summary:
    #             粉丝个数
    #     Returns:
    #
    #     """
    #     id_ = 'com.jiuyan.infashion:id/diary_user_header_fans_tv'
    #     return text_view.TextView(self.parent, id=id_).text
    #
    # @property
    # def photo_tab(self):
    #     """
    #         Summary:
    #             照片tab
    #     """
    #     id_ = 'com.jiuyan.infashion:id/layout_timeline'
    #     return linear_layout.LinearLayout(self.parent, id=id_)
    #
    # @property
    # def story_tab(self):
    #     """
    #         Summary:
    #             故事tab
    #     """
    #     id_ = 'com.jiuyan.infashion:id/layout_story'
    #     return linear_layout.LinearLayout(self.parent, id=id_)

    # *************************** 点击关注后可能出现的推荐感兴趣的人属性********************

    @property
    def friends_recommend_list(self):
        """
            Summary:
                推荐好友列表
        Returns:

        """
        return [FriendRecommendItem(self.parent, index) for index in range(3)]

    @property
    def remove_recommend_list_button(self):
        """
            Summary:
                收起可能感兴趣的人的按钮
        Returns:

        """
        id_ = 'followrecbottom'
        return button.UIAButton(self.parent, id=id_)

    # ******************************封面以下图片流元素**********************************

    @property
    def switch_button(self):
        """
            Summary:
                图片展示方式切换按钮
        """
        id_ = 'com.jiuyan.infashion:id/timeline_fabtn_layout'
        return button.Button(self.parent, id=id_)

    @property
    def matrix_photo_album_list(self):
        """
            Summary:
                矩阵式照片排列列表
        """
        rec_view = recycler_view.RecyclerView(self.parent, id='com.jiuyan.infashion:id/timeline_recycler')
        return PhotoAlbumItemList(rec_view, type='android.widget.FrameLayout').item_list

    @property
    def timeline_photo_album_list(self):
        """
            Summary:
                时间线方式的照片列表

        """
        xpath_ = '//android.support.v7.widget.RecyclerView[@resource-id=\"com.jiuyan.infashion:id/timeline_recycler\"]/' \
                 'android.widget.LinearLayout'
        return PhotoAlbumItemList(self.base_parent, xpath=xpath_).timeline_item_list

    # *****************************取消关注的底部弹出元素********************************

    @property
    def unfollow_bottom_button(self):
        """
        Summary:
            取消关注按钮
        """
        id_ = 'com.jiuyan.infashion:id/cancel_watch'
        return static_text.TextView(self.parent, id=id_)

    @property
    def cancel_unfollow_bottom_button(self):
        """
        Summary:
            取消遮罩按钮
        """
        id_ = 'com.jiuyan.infashion:id/tv_cancel'
        return static_text.TextView(self.parent, id=id_)

    # ***********************操作方法*********************************

    def tap_unfollow_button(self):
        """
            Summary:
                点击取消关注按钮
        """
        log.logger.info("开始点击取消关注按钮")
        self.follow_button.tap()
        log.logger.info("结束取消关注按钮点击")
        if self.wait_for_element_present(self.parent, id='com.jiuyan.infashion:id/cancel_watch'):
            return True
        log.logger.error("弹出底部遮罩框失败")
        return False

    def tap_confirm_unfollow_button(self):
        """
            Summary:
                点击确认取消关注按钮
        """
        log.logger.info("开始点击确认取消关注按钮")
        self.unfollow_bottom_button.tap()
        log.logger.info("结束确认取消关注按钮点击")
        time.sleep(3)


class PhotoAlbumItem(base_frame_view.BaseFrameView):
    """
        Summary:
            照片列表
    """
    def __init__(self, parent, item=None, **kwargs):
        super(PhotoAlbumItem, self).__init__(parent)
        self._layout_view = item if isinstance(item, WebElement) else self.find_element(**kwargs)

    @property
    def photo_count(self):

        id_ = 'com.jiuyan.infashion:id/tv_number_multi_photo'
        return static_text.TextView(self._layout_view, id=id_).text

    #  **********************操作方法************************
    def tap(self):
        """
            Summary:
                点击图片集
        """
        log.logger.info("开始点击该图片集")
        self._layout_view.click()
        if self.wait_activity(windows.WindowNames.PHOTO_ALBUM_CORE, 10):
            log.logger.info("成功进入图片集详情页")
            return True
        log.logger.error("进入图片集详情页失败")
        return False


class PhotoAlbumItemList(base_frame_view.BaseFrameView):

    def __init__(self, parent, **kwargs):
        super(PhotoAlbumItemList, self).__init__(parent)
        self.__list = self.find_elements(**kwargs)

    @property
    def item_list(self):

        if self.__list:
            return [PhotoAlbumItem(item.parent, item) for item in self.__list]
        return None


# ******************推荐好友列表******************


class FriendRecommendItem(base_frame_view.BaseFrameView):
    """
        Summary:
            推荐好友列表
    """
    def __init__(self, parent, index):
        """

        Args:
            parent: 父亲frame
            index: xpath的序号, 从0开始

        """
        super(FriendRecommendItem, self).__init__(parent)
        self.__index = index
        self.__xpath_parent = '//UIAApplication[1]/UIAWindow[1]/'

    @property
    def avatar(self):
        """
            Summary:
                头像
        Returns:

        """
        curr_index = (self.__index+1) * 3
        xpath_ = self.__xpath_parent + 'UIAImage[{}]'.format(curr_index)
        return image.UIAImage(self.base_parent, xpath=xpath_)

    @property
    def user_name(self):
        """
            Summary:
                名称
        Returns:

        """
        curr_index = (self.__index + 1) * 2
        xpath_ = self.__xpath_parent + 'UIAStaticText[{}]'.format(curr_index)
        return static_text.UIAStaticText(self.base_parent, xpath=xpath_).text

    @property
    def follow_button(self):
        """
            Summary:
                关注按钮
        Returns:

        """
        xpath_ = self.__xpath_parent + 'UIAButton[@name="＋关注"]'
        return button.UIAButtonList(self.parent, xpath=xpath_).button_list[self.__index]

    #  **********************操作方法************************

    def tap_avatar(self):
        """
            Summary:
                点击头像
        Returns:

        """
        log.logger.info('开始点击可能感兴趣的人的头像')
        self.avatar.tap()
        log.logger.info("点击完毕")
        time.sleep(2)
