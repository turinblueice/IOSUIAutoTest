#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:

Authors: turinblueice
Date: 2016/7/26
"""

from base import base_frame_view
from base import thread_device_pool
from gui_widgets.custom_widgets import bottom_tab_widget

from UIAWindows import windows
from UIAWindows.register_sign_windows import login_main_window
from UIAWindows.register_sign_windows import login_friend_recommend_window
from UIAWindows.in_main_windows import user_center_tab_window

from UIAWindows.common_windows import story_gallery_window
from util import log
from model import model

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


class ActionsAccess2Window(object):

    def __init__(self, driver):
        self.__driver = driver
        self.__base_app = base_frame_view.BaseFrameView(self.__driver)
        self.__model_config = model.config_parser

        # ******************多设备相关变量**********************

        self.__thread_number = thread_device_pool.ThreadDeviceInfoPool.get_current_thread_number()

    @property
    def current_window(self):
        """
            Summary:
                当前活动页面
        """
        return self.__base_app.current_window

    @staticmethod
    def wait_for_app_launch(wait_time=10):
        """
            Summary:
                等待APP启动完毕
            Args:
                wait_time:等待时长
        """
        log.logger.info("等待app启动")
        time.sleep(wait_time)

    def _wait_for_init(self, wait_time=8):
        """
            Summary:
                等待页面初始化
            Args:
                wait_time:等待时长
        """
        try:

            # 应用启动时，默认已登录，直接进入主页
            # 因为主页内容需要网络请求来初始化，因此要继续检查底部tab列表，若“发现”tab被选中，则证明已经进入in的主页
            # 且底部栏已初始化完毕， xpath为“发现”tab的xpath
            log.logger.info("等待in主页面初始化")
            if self.__base_app.wait_window(windows.WindowNames.LOGIN_FRIEND_RECOMMEND, wait_time):
                log.logger.info("登录后首先进入了好友推荐页")
                log.logger.info("点击好友推荐页的完成按钮")
                curr_friend_window = login_friend_recommend_window.LoginFriendRecommendWindow(self.__base_app)
                curr_friend_window.tap_finish_button()

            # 检查广告遮罩
            log.logger.info("检查广告遮罩")
            if self.__base_app.wait_for_element_present(
                    self.__driver, name='ad_test'):  # 广告的accessibility_id待实现
                log.logger.info("当前页面存在广告遮罩")
                log.logger.info("点击非广告部分，关闭广告")
                self.__base_app.tap_window_top()

            WebDriverWait(self.__driver, wait_time).until(
                EC.presence_of_element_located(
                    (MobileBy.ACCESSIBILITY_ID, 'paizhao'))
            )
            log.logger.info("in主页面初始化完毕")
        except TimeoutException:
            # in主页面在指定时间内仍然未初始化完毕，检查当前应用是否未登录
            if self.__base_app.wait_window(windows.WindowNames.LOGIN_MAIN):
                # 未登录，则等待登陆页初始化完毕
                # 进入登录页后，因为页面内容需要初始化，有一定延时，因此要继续检查登录按钮是否存在
                log.logger.info("等待登陆页初始化")
                # 登录按钮出现则说明登录页面初始化完毕
                WebDriverWait(self.__driver, wait_time).until(
                    EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, '登录'))
                )
                log.logger.info("in原生登录页面初始化完毕")
            else:
                # 其他情况，则直接抛出异常，结束程序。如应用一直卡在启动页，或者在指定时间内in主页没初始化完毕
                log.logger.error("指定时间内in主页未初始化完毕")
                raise
        time.sleep(3)

    def go_to_discover_tab(self):
        """
            Summary:
                进入发现tab页面
        :return:
        """
        # 先等待页面初始化完毕
        log.logger.info("应用启动后等待首次展现的页面初始化完毕")
        self._wait_for_init()

        login_status = True  # 默认登录状态
        if self.__base_app.wait_window(windows.WindowNames.LOGIN_MAIN, 1):  # 当前页面为登陆页
            log.logger.info("当前应用未登录，先登录应用")
            login_status = self.login()
            log.logger.info("登录成功后，再次等待in主页面初始化完毕")
            self._wait_for_init()

        if login_status:

            curr_tab_widget = bottom_tab_widget.BottomTabWidget(self.__base_app)
            status = curr_tab_widget.tap_discover_tab()
            if status:
                log.logger.info("准备工作完毕，已成功进入发现tab页")
                return True
        log.logger.error("准备工作完毕，进入发现tab页失败")
        return False

    def go_to_focus_tab(self):
        """
            Summary:
                进入关注tab页面
        :return:
        """
        # 先等待页面初始化完毕
        log.logger.info("应用启动后等待首次展现的页面初始化完毕")
        self._wait_for_init()

        login_status = True  # 默认登录状态
        if self.__base_app.wait_window(windows.WindowNames.LOGIN_MAIN, 1):  # 当前页面为登陆页
            log.logger.info("当前应用未登录，先登录应用")
            login_status = self.login()
            log.logger.info("登录成功后，再次等待in主页面初始化完毕")
            self._wait_for_init()

        if login_status:

            curr_tab_widget = bottom_tab_widget.BottomTabWidget(self.__base_app)
            status = curr_tab_widget.tap_focus_tab()
            if status:
                log.logger.info("准备工作完毕，已成功进入关注tab页")
                return True
        log.logger.error("准备工作完毕，进入关注tab页失败")
        return False

    def go_to_user_center_tab(self):
        """
            Summary:
                进入in主页-中心tab

        """
        # 先等待页面初始化完毕
        log.logger.info("应用启动后等待首次展现的页面初始化完毕")
        self._wait_for_init()

        login_status = True  # 默认登录状态
        if self.__base_app.wait_window(windows.WindowNames.LOGIN_MAIN, 1):  # 当前页面为登陆页
            log.logger.info("当前应用未登录，先登录应用")
            login_status = self.login()
            log.logger.info("登录成功后，再次等待in主页面初始化完毕")
            self._wait_for_init()

        if login_status:

            curr_tab_widget = bottom_tab_widget.BottomTabWidget(self.__base_app)
            status = curr_tab_widget.tap_center_tab()
            if status:
                log.logger.info("准备工作完毕，已成功进入中心tab页")
                return True
        log.logger.error("准备工作完毕，进入中心tab页失败")
        return False

    def go_to_publish_story_tab(self):
        """
            Summary:
                进入发布故事集的tab页面
        """
        if self.go_to_discover_tab():
            curr_tab_widget = bottom_tab_widget.BottomTabWidget(self.__base_app)
            if curr_tab_widget.tap_camera_tab():
                log.logger.info("成功进入图片选择页")
                curr_story_gallery_window = story_gallery_window.StoryGalleryWindow(self.__base_app)
                if curr_story_gallery_window.tap_story_tab():
                    log.logger.info("已成功进入故事集tab")
                    return True
        log.logger.error("进入故事集tab失败")
        return False

    def go_to_publish_photo_tab(self):
        """
            Summary:
                进入发布图片的tab页面
        """
        if self.go_to_discover_tab():
            curr_tab_widget = bottom_tab_widget.BottomTabWidget(self.__base_app)
            if curr_tab_widget.tap_camera_tab():
                log.logger.info("成功进入图片选择页")
                curr_story_gallery_window = story_gallery_window.StoryGalleryWindow(self.__base_app)
                if curr_story_gallery_window.tap_photo_tab():
                    log.logger.info("已成功进入图片tab")
                    return True
        log.logger.error("进入图片tab失败")
        return False

    def go_to_my_paster(self):
        """
            Summary:
                进入我的贴纸页面
        """
        if self.go_to_user_center_tab():
            curr_user_center_window = user_center_tab_window.UserCenterTabWindow(self.__base_app)
            log.logger.info("将\"我的贴纸\"上滑到屏幕中")
            curr_user_center_window.swipe_up_entire_scroll_view()
            if curr_user_center_window.tap_paster_bar():
                return True
        return False

    def login(self):
        """
            Summary:
                登陆
        """
        curr_login_view = login_main_window.LoginMainWindow(self.__base_app)
        curr_login_view.input_account(self.__model_config.get('account', 'account'+str(self.__thread_number)))
        curr_login_view.input_password(self.__model_config.get('account', 'password'+str(self.__thread_number)))
        status = curr_login_view.tap_login_button()

        return status
