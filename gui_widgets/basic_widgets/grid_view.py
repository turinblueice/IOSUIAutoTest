#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:android.widget.GridView

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class GridView(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, grid_view=None, **kwargs):
        super(GridView, self).__init__(parent)
        self.__grid_view = grid_view if isinstance(grid_view, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):

        return getattr(self.__grid_view, item, None)

    def tap(self):
        self.__grid_view.click()


class GridViewList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(GridViewList, self).__init__(parent)
        self.__grid_view_list = self.find_elements(**kwargs)

    @property
    def grid_view_list(self):
        if self.__grid_view_list:
            return [GridView(layout.parent, layout) for layout in self.__grid_view_list]
        return None

