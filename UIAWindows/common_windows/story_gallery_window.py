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

from gui_widgets.basic_widgets import window
from gui_widgets.basic_widgets import table_cell
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import tool_bar
from gui_widgets.basic_widgets import collection_cell
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import image

from appium.webdriver import WebElement
from UIAWindows import windows

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


class StoryGalleryWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            发图-选择图片/写故事页面

        Attributes:

    """
    name = '.album.StoryGalleryActivity'
    STORY_PHOTO = 'photo_list'
    STORY_SELECT_ALL = 'all_button'
    
    def __init__(self, parent):
        super(StoryGalleryWindow, self).__init__(parent)

    @property
    def photo_tab(self):
        """
            Summary:
                发图片tab按钮
        :return:
        """
        return button.UIAButton(self.parent, name='发图片')

    @property
    def story_tab(self):
        """
            Summary:
                写故事tab按钮
        :return:
        """
        return button.UIAButton(self.parent, name='写故事')

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        """
        name_ = "photolibrary close"
        return button.UIAButton(self.parent, id=name_)

    @property
    def album_drop_list_button(self):
        """
            Summary:
                相册下拉列表按钮-相机胶卷
        :return:
        """
        name_ = 'INStory listIndicator'
        return button.UIAButton(self.parent, name=name_)

    @property
    def album_title(self):
        """
            Summary:
                相册集的名称
        """
        xpath_ = '//UIAApplication[1]/UIAWindow/UIAButton[2]'
        return button.UIAButton(self.base_parent, xpath=xpath_).text

    @property
    def continue_button(self):
        """
            Summary:
                继续按钮
        """
        name_ = "继续"
        return button.UIAButtonList(self.parent, name=name_).button_list[-1]

    # *************************"发图片"tab下的属性******************************

    @property
    def camera(self):
        """
            Summary:
                相机按钮
        """
        #  列表下首个id为item_photo_root的元素为摄像头
        return collection_cell.UIACollectionCell(self.parent,
                                                 name='INPublishResource.bundle/image_library_cammer')

    @property
    def image_photo_list(self):
        """
            Summary:
                发图片tab下，要上传的图片列表
        """
        xpath_ = '//UIAApplication[1]/UIAWindow[position()<3]/UIACollectionView[1]/' \
                 'UIACollectionCell[@name=\"image library checkmark normal\"]'

        #  等待图片列表全部载入，载入首张图片即可认为列表已初始化完毕
        if self.wait_for_element_present(self.base_parent, name='image library checkmark normal'):
            return PostImgItemList(self.base_parent, xpath=xpath_).item_list
        return None

    @property
    def image_photo_enable_picked_count(self):
        """
            Summary:
                屏幕内可选图片数量
        :return:
        """
        all_count = len(self.image_photo_list)
        return all_count if all_count <= 11 else 11  # 单个屏幕中最多可显示可点击图片为11张

    @property
    def selected_photo_count(self):
        """
            Summary:
                发图片tab下选择的图片数量
        :return:
        """
        xpath_ = '//UIAApplication[1]/UIAWindow/UIAButton[4]'
        return button.UIAButton(self.base_parent, xpath=xpath_).text

    # ************************写故事tab下的元素***************
    @property
    def story_tab_in_diary_album_bar(self):
        """
            Summary:
                写故事tab下，展开下拉列表后，in记相册栏
        """
        return table_cell.UIATableCell(self.parent, name='in记相册')

    @property
    def story_tab_album_bar_list(self):
        """
            Summary:
                写故事tab下，展开下拉列表后的相册列表
        """
        return table_cell.UIATableCellList(self.parent, type='UIATableCell').cell_list

    @property
    def story_photo_list(self):
        """
            Summary:
                写故事tab下的照片列表
        """
        xpath_ = '//UIACollectionView[2]/UIACollectionCell'

        return PostImgItemList(self.base_parent, xpath=xpath_).item_list

    @property
    def in_diary_photo_list(self):
        """
            Summary:
                "in记"相册下的所有照片列表,其他相册则使用"日期":{"全选按钮"：button,"相册列表":[]}的方式
        """
        xpath_ = '//UIACollectionView[2]/UIACollectionCell[@name="INPhotoMomentEditN"]'  # [@name="INPhotoMomentEditN"]
        return PostImgItemList(self.base_parent, xpath=xpath_).item_list

    @property
    def selected_story_photo_count(self):
        """
            Summary:
                写故事tab下的图片选择数
        :return:
        """
        xpath_ = '//UIAApplication[1]/UIAWindow/UIAButton[7]'
        return button.UIAButton(self.base_parent, xpath=xpath_).text

    # ************************操作***************************
    def open_camera(self):
        """
            Summary:
                打开摄像头
        """
        log.logger.info("点击打开摄像头")
        self.camera.tap()
        time.sleep(2)
        log.logger.info("摄像头已打开")

    def select_image_photo(self, index):
        """
            Summary:
                选择发图片tab下要上传的图片
            Args:
                index: 图片序号
        """
        self.post_image_list[index-1].select()
        time.sleep(1)

    def unselect_image_photo(self, index=1):
        """
            Summary:
                取消选择发图片tab下上传的图片
            Args:
                index: 图片序号,从1开始
        """
        self.post_image_list[index-1].unselect()
        time.sleep(1)

    def tap_photo_continue_button(self, timeout=10):
        """
            Summary:
                点击继续按钮
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击下一步按钮")
        self.continue_button.tap()
        time.sleep(5)
        if self.wait_window(windows.WindowNames.PUBLISH_CORE, timeout):
            log.logger.info("成功进入发布加工页")
            return True
        log.logger.error("进入发布加工失败")
        return False

    def tap_story_continue_button(self, timeout=10):
        """
            Summary:
                点击继续按钮
            Args:
                timeout:等待时长
        """
        log.logger.info("开始点击下一步按钮")
        self.continue_button.tap()
        if self.wait_window(windows.WindowNames.STORY_EDIT, timeout):
            log.logger.info("成功进入故事编辑页")
            return True
        log.logger.error("进入故事编辑页失败")
        return False

    def tap_album_droplist(self):
        """
            Summary:
                点击相册下拉列表
        """
        log.logger.info("点击最上方的下拉列表")
        self.album_drop_list_button.tap()
        time.sleep(3)
        log.logger.info("完成下拉列表的点击")

    def tap_in_diary_album(self):
        """
            Summary:
                点击in记相册
        """
        log.logger.info("点击in记相册")
        self.story_tab_in_diary_album_bar.tap()
        try:
            WebDriverWait(self.base_parent, 10).until(
                EC.presence_of_element_located(
                    (MobileBy.ACCESSIBILITY_ID, 'in记相册'))
            )
            log.logger.info("成功展开in记相册")
            return True
        except TimeoutException:
            log.logger.error("展开in记相册失败")
            return False

    def select_photo_from_in_diary(self, index_list=[]):
        """
            Summary:
                从印记相册中选择照片上传
            Args:
                index_list: 照片序号列表
        """
        photo_list = self.in_diary_photo_list
        for index in index_list:
            log.logger.info("开始选择第{}张照片".format(index))
            photo_list[index-1].select()

        log.logger.info("照片已选择完毕")
        time.sleep(2)

    # *****************************公共方法********************************

    def tap_photo_tab(self):
        """
            Summary:
                点击图片tab
        :return:
        """
        log.logger.info("开始点击图片tab")
        self.photo_tab.tap()
        log.logger.info("点击完毕")
        time.sleep(2)
        return True

    def tap_story_tab(self):
        """
            Summary:
                点击故事tab页
        :return:
        """
        log.logger.info("开始点击故事tab")
        self.story_tab.tap()
        log.logger.info("点击完毕")
        try:
            WebDriverWait(self.base_parent, 10).until(
                EC.presence_of_element_located(
                    (MobileBy.ACCESSIBILITY_ID, '照片')
                )
            )
            log.logger.info("故事集图片选择页已初始化完毕")
            return True
        except TimeoutException:
            log.logger.error("故事集图片选择未完成初始化")
            return False


class PostImgItem(base_frame_view.BaseFrameView):
    """
        Summary:
            上传的图片item
    """
    def __init__(self, parent, item=None, index=None, **kwargs):
        super(PostImgItem, self).__init__(parent)
        self._layout_view = item if isinstance(item, WebElement) else self.find_element(**kwargs)
        self.__index = index

    def __getattr__(self, item):
        return getattr(self._layout_view, item, None)

    @property
    def check_box(self):
        """
            Summary:
                勾选框
        """
        return button.UIAButton(self._layout_view, type='UIAButton')

    @property
    def check_text(self):
        """
            Summary:
                选中显示的序号值
        :return:
        """
        return self.check_box.text

    @property
    def check_value(self):
        """
            Summary:
                选中显示的value属性值
        """
        return self.check_box.value

    def tap(self):
        """
            Summary:
                点击该图片
        :return:
        """
        log.logger.info("开始点击选择{}图片".format('第' + str(self.__index) + '张' if self.__index is not None else '该'))
        self._layout_view.click()
        time.sleep(1)
        log.logger.info("点击完毕")

    def select(self):
        """
            Summary:
                选择图片，点击图片区域即可选择，无需点击check_box
        """

        log.logger.info("开始点击选择{}图片".format('第'+str(self.__index)+'张' if self.__index is not None else '该'))
        self.check_box.tap()
        time.sleep(1)
        log.logger.info("完成选择, 已成功选中图片")

    def unselect(self):
        """
            Summary:
                取消选择图片
        """
        log.logger.info("开始取消选择{}图片".format('第' + str(self.__index) + '张' if self.__index is not None else '该'))
        self.check_box.tap()
        time.sleep(1)
        log.logger.info("完成取消, 已成功取消选择图片")

    def is_selected(self):
        """
            Summary:
                是否被选中
        :return:
        """
        value = self.check_value
        return value


class PostImgItemList(base_frame_view.BaseFrameView):

    def __init__(self, parent, **kwargs):
        super(PostImgItemList, self).__init__(parent)
        self.__item_list = self.find_elements(**kwargs)

    @property
    def item_list(self):
        if self.__item_list:
            return [PostImgItem(item.parent, item, index)
                    for index, item in enumerate(self.__item_list, start=1)
                    if item.location['x'] >= 0 and item.location['y'] > 0]  # 选取坐标(x, y) 纵坐标不能小于0即在屏幕之上
        return None
