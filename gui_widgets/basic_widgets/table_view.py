#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIATableView

Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIATableView(base_frame_view.BaseFrameView):
    """
        Summary:
            UIAButton类型
    """
    def __init__(self, parent, view=None, **kwargs):
        super(UIATableView, self).__init__(parent)
        self.__view = view if isinstance(view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__view, item, None)

    def tap(self, timeout=0.5):
        """
        :param timeout 等待时间
        Args:
            
        Returns:
        Raises
        """
        self.__view.click()
        self.base_parent.implicitly_wait(timeout)


class UIATableViewList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIATableViewList, self).__init__(parent)
        self.__view_list = self.find_elements(**kwargs)

    @property
    def cell_list(self):

        return [UIATableView(view.parent, view) for view in self.__view_list]


