# -*-coding:utf-8-*-

################################################################################
#
#
#
################################################################################
"""
finder模块,控件查找的基类

Authors: turinblueice
Date:    16/3/15 12:04
"""
import datetime
import os

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from util import log

import random
import time


class BaseFrameViewMetaClass(type):

    def __new__(mcs, name, bases, dct):
        if 'by_dct' not in dct or not type(dct['by_dct']) == 'dict':
            dct['by_dct'] = dict()

        elem_list = ['elem', 'elems']
        dct['by_dct']['name'] = dict(zip(elem_list, ['find_element_by_accessibility_id',
                                                     'find_elements_by_accessibility_id']))
        dct['by_dct']['xpath'] = dict(zip(elem_list, ['find_element_by_xpath',
                                                      'find_elements_by_xpath']))
        dct['by_dct']['uiautomation'] = dict(zip(elem_list, ['find_element_by_ios_uiautomation',
                                                             'find_elements_by_ios_uiautomation']))
        dct['by_dct']['id'] = dict(zip(elem_list, ['find_element_by_id',
                                                   'find_elements_by_id']))
        # find_element_by_class_name("android.widget.EditText")
        dct['by_dct']['type'] = dict(zip(elem_list, ['find_element_by_class_name',
                                                     'find_elements_by_class_name']))
        dct['by_dct']['tag'] = dict(zip(elem_list, ['find_element_by_tag_name',
                                                    'find_elements_by_tag_name']))

        return super(BaseFrameViewMetaClass, mcs).__new__(mcs, name, bases, dct)


class BaseFrameView(object):

    """
    Summary:
        基础界面框架类,界面控件的父类,查找上层控件

    Attribute:
        _parent: 查找的父层,最底层即基层为驱动层driver

    """

    __metaclass__ = BaseFrameViewMetaClass

    def __init__(self, parent=None):

        super(BaseFrameView, self).__init__()
        self._parent = parent
        self._layout_view = None  # WebElement对象，等待子类实现
        self._scroll_view = None  # 可滑动区域对象，等待子类实现

    @property
    def parent(self):
        """
        Summary:
            返回父亲界面

        Return:
            返回对象的父亲界面对象
        """
        if isinstance(self._parent, BaseFrameView) or isinstance(self._parent, webdriver.Remote) or \
                isinstance(self._parent, WebElement):
            return self._parent
        return None

    @property
    def base_parent(self):
        curr_parent = self._parent

        # 如果当前的父界面是基础界面类型而不是webdriver.Remote类型,则追溯到最底层的父亲界面,最底层类型约定为webdrive.Remote类
        while not isinstance(curr_parent, webdriver.Remote) and isinstance(curr_parent, BaseFrameView):
            curr_parent = curr_parent.parent

        if isinstance(curr_parent, WebElement):
            curr_parent = curr_parent.parent
            return curr_parent

        if not isinstance(curr_parent, webdriver.Remote):
            curr_parent = None

        return curr_parent

    def __getattr__(self, item):

        return getattr(self.base_parent, item, None)

    def find_element(self, key=None, value=None, **kwargs):

        by_dct = getattr(self.__class__, 'by_dct')
        func = None
        if key and value:
            func = getattr(self.parent, by_dct[key]['elem'], None)

        for key in kwargs:
            if key in by_dct:
                func = getattr(self.parent, by_dct[key]['elem'], None)
                if func:
                    value = kwargs[key]
                    break
        elem = func(value)
        return elem

    def find_elements(self, key=None, value=None, **kwargs):

        func = None
        by_dct = getattr(self.__class__, 'by_dct')

        if key and value:
            func = getattr(self.parent, by_dct[key]['elems'], None)

        for key in kwargs:
            if key in by_dct:
                func = getattr(self.parent, by_dct[key]['elems'], None)
                if func:
                    value = kwargs[key]
                    break
        elems = func(value)
        return elems

    def save_screen_shot(self, name, image_dir=None):
        """

        :param name:
        :param image_dir:
        Args:
            name:截图保存名称
            image_dir: 保存图片目录名称
        Return:
        """
        now = datetime.datetime.now()
        now_str = now.strftime("%Y%m%d%H%M%S")
        today_str = now.strftime("%Y%m%d")
        default_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../outputs/screen_shots/'+today_str))

        screen_shot_dir = image_dir or default_dir
        if not os.path.isdir(screen_shot_dir):
            os.makedirs(screen_shot_dir)

        screen_shot_name = os.path.join(screen_shot_dir, 'test_'+name+'_'+now_str+'.png')

        log.logger.info("开始截图")
        self.base_parent.save_screenshot(screen_shot_name)
        log.logger.info("截图已保存到目录:" + screen_shot_dir)

    # *************************************等待子元素出现***********************************
    def wait_for_element_present(self, parent=None, timeout=10, poll=1, key=None, **kwargs):
        """
            Summary:
                等待当前元素的子元素出现
            Args:
                parent: 父容器
                timeout: 等待时长
                poll: 检查间隔
                key: id、name、xpath等键
                kwargs: id=''
        """
        parent = parent or self._layout_view
        by_dct = getattr(self.__class__, 'by_dct')
        key = key or kwargs.keys()[0]
        value = kwargs.itervalues().next()

        end_time = time.time() + timeout
        while True:
            try:
                func = getattr(parent, by_dct[key]['elem'])
                if func:
                    func(value)
                    return True
                raise
            except:
                time.sleep(poll)
                if time.time() > end_time:
                    break
        return False

    def wait_window(self, window, timeout=10, interval=1):
        """
            Summary:
                等待窗口
        """
        key, value = tuple(window.split('_', 1))
        return self.wait_for_element_present(
            parent=self.base_parent, timeout=timeout, poll=interval, key=key, curr_key=value)

    def wait_one_of_windows(self, windows=(), timeout=5, interval=1):
        """
            Summary:
                等待活动页列表中的某个页面出现
            Args:
                windows:活动页列表
                timeout:超时时间
                interval:间隔时间
        """
        random_windows = random.sample(windows, len(windows))
        for window in random_windows:
            if self.wait_window(window, timeout=timeout, interval=interval):
                return True
        return False

    #  ***********************************元素的基础操作*****************************************  #
    def swipe_up(self, x, start_y, end_y, duration=None):
        """
            Summary:
                向上滑动
        """
        if end_y >= start_y:
            log.logger.error("向上滑动,结束位置不应大于起始位置")
            return None
        return self.base_parent.swipe(x, start_y, x-x, end_y-start_y, duration)

    def swipe_down(self, x, start_y, end_y, duration=None):
        """
            Summary:
                向下滑动
        """
        if end_y <= start_y:
            log.logger.error("向下滑动,结束位置不应小于起始位置")
            return None
        return self.base_parent.swipe(x, start_y, x, end_y, duration)

    def swipe_left(self, start_x, end_x, y, duration=None):
        """
            Summary:
                向左滑动
        """
        if start_x <= end_x:
            log.logger.error("向左滑动,结束位置不应大于起始位置")
            return None
        return self.base_parent.swipe(start_x, y, end_x, y, duration)

    def swipe_right(self, start_x, end_x, y, duration=None):
        """
            Summary:
                向右滑动
        """
        if start_x >= end_x:
            log.logger.error("向右滑动,结束位置不应小于起始位置")
            return None
        return self.base_parent.swipe(start_x, y, end_x, y, duration)

    def swipe_up_entire_scroll_view(self):
        """
            Summary:
                向上滑动整个scroll view的高度

        """
        location = self._scroll_view.location
        size = self._scroll_view.size
        x = location['x'] + 2  # + size['width']/2
        start_y = location['y'] + size['height'] - 1
        end_y = location['y'] + 1

        log.logger.info("开始向上滑动整个可滑动区域的屏幕")
        self.swipe_up(x, start_y, end_y)
        log.logger.info("向上滑动结束")
        time.sleep(3)

    def swipe_down_entire_scroll_view(self):
        """
            Summary:
                向下滑动整个scroll view的高度
        """
        location = self._scroll_view.location
        size = self._scroll_view.size
        x = location['x'] + size['width']/2
        end_y = location['y'] + size['height'] - 1
        start_y = location['y'] + 1

        log.logger.info("开始向下滑动整个可滑动区域的屏幕")
        self.swipe_up(x, start_y, end_y)
        log.logger.info("向下滑动结束")

    # **********************************系统方法************************************************  #

    def tap_window_center(self):
        """
            Summary:
                点击窗口中心
        :return:
        """
        size = self.base_parent.get_window_size()

        x = size['width']/2
        y = size['height']/2
        log.logger.info("点击屏幕中央")
        self.base_parent.tap([(x, y)])
        time.sleep(3)

    def tap_window_top(self):
        """
            Summary:
                点击窗口顶部
        :return:
        """
        size = self.base_parent.get_window_size()

        x = size['width']/2
        y = size['height']/20

        self.base_parent.tap([(x, y)])
        time.sleep(3)

    # ************************************

    def get_location(self, element=None):

        element = element or self._layout_view
        size = element.size
        coordination = element.location
        coordinate_x = coordination['x'] + size['width']/2
        coordinate_y = coordination['y'] + size['height']/2

        return coordinate_x, coordinate_y
