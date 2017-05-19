#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:UIAButton

Authors: turinblueice
Date:    16/3/16 12:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class UIAButton(base_frame_view.BaseFrameView):
    """
        Summary:
            UIAButton类型
    """
    def __init__(self, parent, button=None, **kwargs):
        super(UIAButton, self).__init__(parent)
        self.__button = button if isinstance(button, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):
        return getattr(self.__button, item, None)

    def tap(self, timeout=0.5):
        """
        :param timeout 等待时间
        Args:
            
        Returns:
        Raises
        """
        self.__button.click()
        self.base_parent.implicitly_wait(timeout)

    @property
    def text(self):

        text = self.__button.text
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        return text

    @property
    def label(self):

        label = self.__button.get_attribute('label')
        if isinstance(label, unicode):
            label = label.encode('utf-8')
        return label

    @property
    def value(self):

        value = self.__button.get_attribute('value')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        return value


class UIAButtonList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(UIAButtonList, self).__init__(parent)
        self.__button_list = self.find_elements(**kwargs)

    @property
    def button_list(self):

        return [UIAButton(button.parent, button) for button in self.__button_list]


