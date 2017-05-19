#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIACellectionCell

Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement
from util import log


class UIACollectionCell(base_frame_view.BaseFrameView):
    """
        Summary:
            UIAButton类型
    """
    def __init__(self, parent, cell=None, index=0, **kwargs):
        super(UIACollectionCell, self).__init__(parent)
        self.__cell = cell if isinstance(cell, WebElement) else self.find_element(**kwargs)
        self.__index = index

    def __getattr__(self, item):
        return getattr(self.__cell, item, None)

    def tap(self, timeout=0.5):
        """
        :param timeout 等待时间
        Args:
            
        Returns:
        Raises
        """
        log.logger.info("点击图集中的第{}张图片".format(self.__index+1))
        self.__cell.click()
        self.base_parent.implicitly_wait(timeout)


class UIACollectionCellList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIACollectionCellList, self).__init__(parent)
        self.__cell_list = self.find_elements(**kwargs)

    @property
    def cell_list(self):

        return [UIACollectionCell(cell.parent, index, cell) for index, cell in enumerate(self.__cell_list)]


