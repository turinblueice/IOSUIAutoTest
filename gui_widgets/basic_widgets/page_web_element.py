#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:html webelement
            网页元素类型
Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class PageWebElement(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, element=None, **kwargs):
        super(PageWebElement, self).__init__(parent)
        self.__element = element if isinstance(element, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__element, item, None)

    @property
    def text(self):
        if isinstance(self.__element.text, unicode):
            return self.__element.text.encode('utf8')
        return self.__element.text

    def tap(self, timeout=0.5):
        """
        :param timeout 等待时间
        Args:
            
        Returns:
        Raises
        """
        self.__element.click()
        self.base_parent.implicitly_wait(timeout)

    def input_value(self, *values):
        """
            Summary:
                输入
        """
        self.__element.clear()  # Clears the text if it’s a text entry element.
        self.__element.send_keys(*values)


class PageWebElementList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(PageWebElementList, self).__init__(parent)
        self.__element_list = self.find_elements(**kwargs)

    @property
    def element_list(self):

        return [PageWebElement(element.parent, element) for element in self.__element_list]


