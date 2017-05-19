#-*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明:class:android.widget.Switch

Authors: turinblueice
Date:    16/3/15 16:12
"""

from base import base_frame_view
from appium.webdriver.webelement import WebElement


class Switch(base_frame_view.BaseFrameView):
    """
    Attribute:
        __switch:
    """
    def __init__(self, parent, switch=None, **kwargs):
        super(Switch, self).__init__(parent)
        self.__switch = switch if isinstance(switch, WebElement) else self.find_element(**kwargs)

    def __getattr__(self, item):

        return getattr(self.__switch, item, None)

    def tap(self):
        self.__switch.click()

    def is_selected(self):

        status = self.__switch.get_attribute('checked')
        if status == 'true':
            return True
        else:
            return False


class SwitchList(base_frame_view.BaseFrameView):
    """

    """
    def __init__(self, parent, **kwargs):
        super(SwitchList, self).__init__(parent)
        self.__switch_list = self.find_elements(**kwargs)

    @property
    def switch_list(self):
        if self.__switch_list:
            return [Switch(switch_item.parent, switch_item) for switch_item in self.__switch_list]
        return None


