#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 选择图片上传页

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log

from gui_widgets.basic_widgets import collection_cell
from gui_widgets.basic_widgets import navigation_bar
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import static_text

from appium.webdriver import WebElement
from UIAWindows import windows

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time


class PhotoPickerWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            选择图片页面

        Attributes:

    """
    
    def __init__(self, parent):
        super(PhotoPickerWindow, self).__init__(parent)

    @property
    def back_button(self):
        """
            Summary:
                取消按钮
        """
        name_ = '取消'
        return button.UIAButton(self.__frame_view, name=name_)

    @property
    def post_photo_list(self):
        """
            Summary:
                要上传的图片列表
        """
        return collection_cell.UIACollectionCellList(self.base_parent, type='UIACollectionCell').cell_list

    # ************************操作***************************

    def select_photo(self, index):
        """
            Summary:
                选择要上传的图片
            Args:
                index: 图片序号
        """
        self.post_image_list[index-1].tap()
        time.sleep(1)
        if self.wait_one_of_windows((windows.WindowNames.CUSTOM_PASTER_CROP, ), 5):
            log.logger.info("成功进入图片裁减页")
            return True
        log.logger.error("进入图片裁剪页失败")
        return False
