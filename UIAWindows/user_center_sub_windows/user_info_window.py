#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 用户中心-编辑资料

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import table_view
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import table_cell
from gui_widgets.custom_widgets import bottom_photo_change_widget
from gui_widgets.custom_widgets import alert

from UIAWindows.common_windows import photo_picker_window
from UIAWindows.common_windows import album_picker_window
from UIAWindows.common_windows import cropper_window
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from UIAWindows import windows

import time
import random


class UserInfoWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            用户中心-编辑资料

        Attributes:

    """

    def __init__(self, parent):
        super(UserInfoWindow, self).__init__(parent)
        self._scroll_view = table_view.UIATableView(self.parent, type='UIATableView')

    @property
    def title(self):
        """
            Summary:
                标题-编辑资料
        """
        name_ = "编辑资料"
        return static_text.UIAStaticText(self.parent, name=name_).text

    @property
    def back_button(self):
        """
            Summary:
                后退按钮
        """
        name_ = '返回'
        return button.UIAButton(self.parent, name=name_)

    @property
    def save_button(self):
        """
            Summary:
                保存按钮
        :return:
        """
        name_ = '保存'
        return button.UIAButton(self.parent, name=name_)

    @property
    def avatar_bar(self):
        """
            Summary:
                头像栏
        :return:
        """
        name_ = '头像'
        return table_cell.UIATableCell(self.parent, name=name_)

    @property
    def nickname_edit_box(self):
        """
            Summary:
                昵称修改文本输入框
        :return:
        """
        name_ = '昵称'
        cell_ = table_cell.UIATableCell(self.parent, name=name_)
        return text_field.UIATextField(cell_, type='UIATextField')

    @property
    def in_id_edit_box(self):
        """
            Summary:
                in号输入框
        :return:
        """
        name_ = 'in号'
        cell_ = table_cell.UIATableCell(self.parent, name=name_)
        return text_field.UIATextField(cell_, type='UIATextField')

    @property
    def region_bar(self):
        """
            Summary:
                地区栏
        :return:
        """
        name_ = '地区'
        return table_cell.UIATableCell(self.parent, name=name_)

    @property
    def region_text(self):
        """
            Summary:
                地区的显示文本
        :return:
        """
        name_ = 'UIAStaticText'
        return static_text.UIAStaticTextList(self.region_bar, name=name_).text_view_list[1].text

    # ************************操作***************************
    def upload_avatar(self, album_index=1, photo_index=1):
        """
            Summary:
                上传头像
            Args:
                album_index:图集编号
        """
        log.logger.info("点击头像栏")
        self.avatar_bar.tap()
        if self.wait_for_element_present(self.parent, type='UIAActionSheet'):
            log.logger.info("已进弹出底部弹层")
            curr_photo_pop_window = bottom_photo_change_widget.BottomPhotoChangeWidget(
                self.parent, type='UIAActionSheet')
            curr_photo_pop_window.tap_select_from_local_button()

            log.logger.info("进入图片集选择页,随机上传一张照片作为头像")
            curr_album_window = album_picker_window.PhotoAlbumPickerWindow(self.parent)
            curr_album_window.remove_guide_mask()

            curr_album_window.select_photo_album(album_index)
            curr_photo_window = photo_picker_window.PhotoPickerWindow(self.parent)

            photo_num = len(curr_photo_window.post_photo_list)
            photo_index = photo_index if photo_index <= photo_num else random.randint(1, photo_num)
            curr_photo_window.select_photo(photo_index)

            curr_cropper_window = cropper_window.CropperWindow(self.parent)
            if curr_cropper_window.tap_choose_button(window=windows.WindowNames.IN_CENTER):
                log.logger.info("已经进入中心页")
                log.logger.info("已成功上传头像")
                return True
        log.logger.error("上传头像失败")
        return False

    def edit_nickname(self, *values):
        """
            Summary:
                编辑昵称
        """
        log.logger.info("开始编辑昵称")
        self.nickname_edit_box.clear_text_field()
        self.nickname_edit_box.send_keys(*values)
        time.sleep(1)
        log.logger.info("编辑昵称完毕")

    def edit_in_id(self, *values):
        """
            Summary:
                编辑id
            Args:
                values: 元组，编辑的值
        """
        log.logger.info("开始编辑in号")
        self.in_id_edit_box.clear_text_field()
        self.in_id_edit_box.send_keys(*values)
        time.sleep(1)
        log.logger.info("编辑in号完毕")

    def select_region(self, city):
        """
            Summary:
                选择地区-城市
            Args:
                city: 城市名称
        """
        log.logger.info("点击地区栏")
        self.region_bar.tap()
        log.logger.info("等待对话框弹出")
        WebDriverWait(self.base_parent, 10).until(
            EC.text_to_be_present_in_element((MobileBy.ID, 'android:id/alertTitle'), alert.SelectCityAlert.title_value)
        )
        curr_alert = alert.SelectCityAlert(self.base_parent)

        if hasattr(curr_alert, 'select_'+city):
            getattr(curr_alert, 'select_'+city)()
            log.logger.info("点击确定按钮")
            curr_alert.confirm_button.tap()
            log.logger.info("城市选择完毕")
        else:
            log.logger.error('该城市：{}输入错误，无法到达'.format(city))


