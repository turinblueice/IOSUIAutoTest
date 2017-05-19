#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIATableCell

Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIATableCell(base_frame_view.BaseFrameView):
    """
        Summary:
            UIAButton类型
    """
    def __init__(self, parent, cell=None, **kwargs):
        super(UIATableCell, self).__init__(parent)
        self.__cell = cell if isinstance(cell, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__cell, item, None)

    def tap(self, timeout=0.5):
        """
        :param timeout 等待时间
        Args:
            
        Returns:
        Raises
        """
        self.__cell.click()
        self.base_parent.implicitly_wait(timeout)


class UIATableCellList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIATableCellList, self).__init__(parent)
        self.__cell_list = self.find_elements(**kwargs)

    @property
    def cell_list(self):

        return [UIATableCell(cell.parent, cell) for cell in self.__cell_list]


