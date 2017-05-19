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
from gui_widgets.basic_widgets import image
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import collection_view
from gui_widgets.basic_widgets import text_field
from gui_widgets.basic_widgets import linear_layout
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import window
from gui_widgets.basic_widgets import collection_cell
from gui_widgets.custom_widgets import alert

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from UIAWindows import windows

import time
import random


class StoryEditWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            发布故事集-编辑故事页

        Attributes:

    """

    def __init__(self, parent):
        super(StoryEditWindow, self).__init__(parent)

        # 滑动区域，覆盖父类的属性
        self._scroll_view = collection_view.UIACollectionView(self.parent, type='UIACollectionView')

    @property
    def title(self):
        """
            Summary:
                标题-编辑故事
        """
        name_ = "编辑故事"
        return static_text.UIAStaticText(self.parent, name=name_).text

    @property
    def back_button(self):
        """
            Summary:
                后退按钮
        """
        name_ = 'push back white'
        return button.UIAButton(self.parent, name=name_)

    @property
    def preview_button(self):
        """
            Summary:
                预览按钮
        :return:
        """
        name_ = '预览'
        return button.UIAButton(self.parent, name=name_)

    @property
    def add_diary_page_button(self):
        """
            Summary:
                页面最下方的故事段落添加按钮
        :return:
        """
        name_ = 'NEditStoryAdd'
        return button.UIAButton(self.parent, name=name_)

    @property
    def add_diary_page_button_middle(self):
        """
            Summary：
                故事页中间的添加按钮
        :return:
        """
        name_ = 'INFireStoryInsetGroup'
        return button.UIAButton(self.parent, name=name_)

    @property
    def diary_cover_detail(self):
        """
            Summary:
                日志故事封面信息
        """

        return DiaryCover(self.parent)

    @property
    def diary_page_list(self):

        name_ = '添加描述~'
        return DiaryPageDetailList(self.parent, name=name_).page_list

    # ************************操作***************************

    def tap_preview_button(self):
        """
            Summary:
                点击预览按钮
        :return:
        """
        log.logger.info("开始点击预览按钮")
        self.preview_button.tap()
        log.logger.info("点击完毕")
        if self.wait_window(windows.WindowNames.STORY_DETAIL, 10):
            log.logger.info("成功进入故事预览页")
            return True
        log.logger.error("进入预览页失败")
        return False


class DiaryCover(base_frame_view.BaseFrameView):
    """
        Summary:
            日记故事封面/开头模块
    """
    def __init__(self, parent):
        super(DiaryCover, self).__init__(parent)

    @property
    def diary_name_edit_box(self):
        """
            Summary:
                故事名称编辑框
        :return:
        """
        xpath_ = '//UIACollectionView[1]/UIACollectionCell[2]/UIATextField[1]'
        return text_field.UIATextField(self.base_parent, xpath=xpath_)

    @property
    def diary_cover_date(self):
        """
            Summary:
                故事时间
        :return:
        """
        xpath_ = '//UIACollectionView[1]/UIACollectionCell[2]/UIATextField[2]'
        return text_field.UIATextField(self.base_parent, xpath=xpath_)

    @property
    def diary_cover_location(self):
        """
            Summary:
                故事地点
        :return:
        """
        xpath_ = '//UIACollectionView[1]/UIACollectionCell[2]/UIATextField[3]'
        return text_field.UIATextField(self.base_parent, xpath=xpath_)

    @property
    def diary_beginning_edit_box(self):
        """
            Summary:
                故事开头编辑框
        :return:
        """
        xpath_ = '//UIACollectionView[1]/UIACollectionCell[3]/UIATextView[1]'
        return static_text.UIAStaticText(self.base_parent, xpath=xpath_)

    @property
    def diary_cover(self):
        """
            Summary:
                封面
        :return:
        """
        name_ = '点击图片设置封面'
        return collection_cell.UIACollectionCell(self.parent, name=name_)

    @property
    def popup_cover_list(self):
        """
            Summary:
                弹出框封面图片列表
        :return:
        """
        xpath_ = '//UIACollectionView[1]/UIACollectionCell'
        return DiaryCover.CoverAlternativeList(self.parent, xpath=xpath_).cover_list

    class CoverAlternativeList(base_frame_view.BaseFrameView):
        """
            Summary:
                点击封面后,下方升起的封面列表候选列表
        """
        def __init__(self, parent, **kwargs):
            super(DiaryCover.CoverAlternativeList, self).__init__(parent)
            self.__items = self.find_elements(**kwargs)

        @property
        def cover_list(self):
            if self.__items:
                return [DiaryCover.CoverAlternative(item.parent, item) for item in self.__items]
            return None

    class CoverAlternative(base_frame_view.BaseFrameView):
        """
            Summary:
                点击封面后,下方升级的候选封面类
        """
        def __init__(self, parent, item=None, **kwargs):
            super(DiaryCover.CoverAlternative, self).__init__(parent)
            self.__item = item if isinstance(item, WebElement) else self.find_element(**kwargs)

        @property
        def select_icon(self):
            """
                Summary:
                    勾选标记图
            Returns:

            """
            name_ = 'NAlbumResource.bundle/INAlbumCoverImage_selected_icon'
            return image.UIAImage(self.__item, name=name_)

        # *************************操作方法****************************

        def tap(self):

            log.logger.info("开始点击该封面")
            self.__item.click()
            log.logger.info("点击结束")
            time.sleep(2)

        def select(self):

            if not self.is_selected():
                log.logger.info("开始点击该封面")
                self.__item.click()
                log.logger.info("点击结束")
                time.sleep(2)
            else:
                log.logger.info("该封面已是选中状态")

        def is_selected(self):
            """
                Summary:
                    是否选中　
            Returns:

            """
            try:
                self.select_icon.is_displayed()
                return True
            except:
                return False

    # **************************操作方法********************************

    def input_diary_name(self, *values):
        """
            Summary:
                输入故事名称
        """
        log.logger.info("开始输入故事名称")
        self.diary_name_edit_box.clear_text_field()
        self.diary_name_edit_box.send_keys(*values)
        time.sleep(1)
        log.logger.info("故事名称输入完毕")

    def input_diary_beginning(self, *values):
        """
            Summary:
                添加故事开头
            Args:
                values: 元组，编辑的值
        """
        log.logger.info("开始添加故事的开头")
        self.diary_beginning_edit_box.clear_text_field()
        self.diary_beginning_edit_box.send_keys(*values)
        time.sleep(1)
        log.logger.info("故事开头完成输入")

    def tap_cover_for_setting(self):
        """
            Summary:
                点击图片设置封面
        :return:
        """
        log.logger.info("点击图片封面")
        self.diary_cover.tap()
        log.logger.info("完成封面点击")
        try:
            WebDriverWait(self.base_parent, 10).until(
                (MobileBy.ACCESSIBILITY_ID, '选择一张照片作为封面')
            )
            log.logger.info("成功吊起封面面板")
            return True
        except:
            log.logger.error("吊起封面面板失败")
            return False

    def select_cover(self, index):
        """
            Summary:
                选择封面图片
            Args:
                index：序号
        """
        log.logger.info("点击第{}张图片".format(index))
        curr_cover = self.popup_cover_list[index-1]
        curr_cover.select()
        log.logger.info("点击完毕")
        log.logger.info("开始检测该图片是否被选中")

        if curr_cover.is_selected():
            log.logger.info("该图片已选中")
            return True
        log.logger.error("该图片未选中")
        return False


class DiaryPageDetail(base_frame_view.BaseFrameView):
    """
        Summary:
            故事集每一页
    """
    def __init__(self, parent, page_item=None, **kwargs):
        super(DiaryPageDetail, self).__init__(parent)
        if kwargs:
            self._layout_view = page_item if isinstance(page_item, WebElement) else self.find_element(**kwargs)
        else:
            self._layout_view = page_item if isinstance(page_item, WebElement) else self.find_element(
                name='添加描述~'
            )

    @property
    def photo(self):
        """
            Summary:
                照片面板,IOS版本精确的照片面板无法抓取,暂采用整个外部容器代替
        :return:
        """
        return collection_cell.UIACollectionCell(self.parent, self._layout_view)

    @property
    def diary_page_description_edit_box(self):
        """
            Summary:
                故事描述编辑框
        :return:
        """

        return static_text.UIAStaticText(self._layout_view, type='UIATextView')

    @property
    def diary_page_description_time(self):
        """
            Summary:
                故事描述的时间
        :return:
        """
        return text_field.UIATextField(self._layout_view, type='UIATextField')

    @property
    def diary_page_description_location(self):
        """
            Summary:
                故事地点
        :return:
        """
        return text_field.UIATextFieldList(self._layout_view, type='UIATextField').text_field_list[1]

    @property
    def edit_right_menu(self):
        """
            Summary:
                右侧边栏编辑组图按钮
        :return:
        """

        return button.UIAButtonList(self._layout_view, type='UIAButton').button_list[0]

    @property
    def add_diary_photo_button(self):
        """
            Summary:
                侧边栏故事图片添加按钮
        :return:
        """
        return button.UIAButtonList(self._layout_view, type='UIAButton').button_list[1]

    @property
    def delete_diary_page_button(self):
        """
            Summary:
                侧边栏删除故事按钮
        :return:
        """
        return button.UIAButtonList(self._layout_view, type='UIAButton').button_list[2]

    @property
    def move_up_button(self):
        """
            Summary:
                上移按钮
        """
        return button.UIAButtonList(self._layout_view, type='UIAButton').button_list[3]

    @property
    def move_down_button(self):
        """
            Summary:
                下移按钮
        :return:
        """

        return button.UIAButtonList(self._layout_view, type='UIAButton').button_list[-1]  # 最后一个按钮

    # 呼出菜单无法识别,暂时注释
    # @property
    # def magic_button(self):
    #     """
    #         Summary:
    #             呼出的编辑菜单的魔法棒加工按钮
    #     :return:
    #     """
    #     id_ = 'com.jiuyan.infashion:id/btn_filter'
    #     return image.ImageView(self.base_parent, id=id_)
    #
    # @property
    # def change_button(self):
    #     """
    #         Summary:
    #             呼出编辑菜单的更换按钮
    #     :return:
    #     """
    #     id_ = 'com.jiuyan.infashion:id/btn_change'
    #     return image.ImageView(self.base_parent, id=id_)
    #
    # @property
    # def delete_button(self):
    #     """
    #         Summary:
    #             呼出编辑菜单的删除按钮
    #     :return:
    #     """
    #     id_ = 'com.jiuyan.infashion:id/btn_del'
    #     return image.ImageView(self.base_parent, id=id_)
    #
    # @property
    # def zoom_in_button(self):
    #     """
    #         Summary:
    #             呼出编辑菜单的放大按钮
    #     :return:
    #     """
    #     id_ = 'com.jiuyan.infashion:id/btn_zoom_in'
    #     return image.ImageView(self.base_parent, id=id_)
    #
    # @property
    # def zoom_out_button(self):
    #     """
    #         Summary:
    #             呼出编辑菜单的缩小按钮
    #     :return:
    #     """
    #     id_ = 'com.jiuyan.infashion:id/zoom_out'
    #     return image.ImageView(self.base_parent, id=id_)

    # ************************操作方法******************************

    def input_diary_description(self, *values):
        """
            Summary:
                输入故事描述
        """
        log.logger.info("开始输入故事描述")
        self.diary_page_description_edit_box.clear_text_field()
        self.diary_page_description_edit_box.send_keys(*values)
        time.sleep(1)
        log.logger.info("故事描述输入完毕")

    def tap_right_menu(self):
        """
            Summary:
                点击侧边栏菜单
        """
        log.logger.info("点击侧边栏编辑组图菜单")
        self.edit_right_menu.tap()
        time.sleep(2)
        log.logger.info("完成编辑组图菜单点击")

    def tap_add_photo_button(self):
        """
            Summary:
                点击增加照片按钮
        :return:
        """
        log.logger.info("点击增加照片按钮")
        self.add_diary_photo_button.tap()
        log.logger.info("完成点击")
        if self.wait_window(windows.WindowNames.PHOTO_STORY_GALLERY, 10):
            log.logger.info("成功进入图片选择页")
            return True
        log.logger.error("进入图片选择页失败")
        return False

    def tap_delete_story_item_button(self, accept=True):
        """
            Summary:
                点击删除故事描述/图片按钮
            Args:
                accept:True:点击确认对话框的确定按钮；False:点击确认对话框的取消按钮
        :return:
        """
        log.logger.info("点击删除故事按钮")
        self.delete_diary_page_button.tap()
        log.logger.info("完成删除按钮点击")

        #  等待对话框弹出
        if self.wait_for_element_present(self.base_parent, name='确认删除片段？'):
            log.logger.info("弹出确认对话框")
            curr_alert = alert.Alert()
            if accept:
                curr_alert.confirm_button.tap()
            else:
                curr_alert.cancel_button.tap()
            return True
        log.logger.error("确认对话框未弹出")
        return False

    # def tap_photo_to_display_menu(self):
    #     """
    #         Summary:
    #             点击照片唤起操作菜单
    #     :return:
    #     """
    #     log.logger.info("开始点击照片按钮")
    #     self.photo.tap()
    #     log.logger.info("点击完毕")
    #     if self.wait_for_element_present(parent=self.base_parent, id='com.jiuyan.infashion:id/btn_filter'):
    #         log.logger.info("编辑菜单已呼出")
    #         return True
    #     log.logger.error("没有呼出编辑菜单")
    #     return False


class DiaryPageDetailList(base_frame_view.BaseFrameView):

    def __init__(self, parent, **kwargs):
        super(DiaryPageDetailList, self).__init__(parent)
        self.__layout_view_list = self.find_elements(**kwargs)

    @property
    def page_list(self):
        if self._layout_view:
            return [DiaryPageDetail(item.parent, item) for item in self.__layout_view_list]
        return None

