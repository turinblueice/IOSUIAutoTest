#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.support.v4.view.ViewPager

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class ViewPager(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, view=None, **kwargs):
        super(ViewPager, self).__init__(parent)
        self._layout_view = view if isinstance(view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self._layout_view, item, None)

    def tap(self, wait_time=0.5):
        self._layout_view.click()
        # 显示等待wait_Time秒
        self.base_parent.implicitly_wait(wait_time)


class ViewList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(ViewList, self).__init__(parent)
        self.__layout_view_list = self.find_elements(**kwargs)

    @property
    def pager_view_list(self):
        if self.__layout_view_list:
            return [ViewList(item.parent, item) for item in self.__layout_view_list]
        return None

