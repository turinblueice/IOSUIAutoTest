#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 图片发布加工页

Authors: turinblueice
Date: 2016/7/27
"""
from base import base_frame_view
from util import log
from gui_widgets.basic_widgets import static_text
from gui_widgets.basic_widgets import scroll_view
from gui_widgets.basic_widgets import button
from gui_widgets.basic_widgets import image
from UIAWindows import windows

from appium.webdriver import WebElement
import time


class PublishCoreWindow(base_frame_view.BaseFrameView):

    """
        Summary:
            图片发布加工页

        Attributes:

    """

    def __init__(self, parent):
        super(PublishCoreWindow, self).__init__(parent)

    @property
    def back_button(self):
        """
            Summary:
                返回按钮
        :return:
        """
        return button.UIAButton(self.parent, name='common nav back')

    @property
    def photo_available_list(self):
        """
            Summary:
                顶栏图片列表
        """
        if self.wait_for_element_present(parent=self.base_parent, type='UIAScrollView'):
            scroll_view_ = scroll_view.UIAScrollView(self.parent, type='UIAScrollView')
            return PhotoItemList(scroll_view_, type='UIAButton').item_list[:-1]  # 最后一个为添加照片按钮
        return None

    @property
    def finish_button(self):
        """
            Summary:
                完成按钮
        :return:
        """
        name_ = '完成'
        return button.UIAButton(self.parent, name=name_)

    @property
    def add_photo_thumb_button(self):
        """
            Summary:
                添加照片按钮
        :return:
        """
        name_ = 'edit addPhotoIndicator'
        return button.UIAButton(self.parent, name=name_)

    @property
    def photo_bar_hide_display_button(self):
        """
            Summary:
                照片栏隐藏/显示按钮
        :return:
        """
        name_ = 'TabExpand'
        return button.UIAButton(self.parent, name=name_)

    @property
    def brand_button(self):
        """
            Summary:
                点击呼出遮罩-品牌按钮
        :return:
        """
        name_ = 'phototagbrandbig'
        return button.UIAButton(self.parent, name=name_)

    @property
    def words_button(self):
        """
            Summary:
                点击呼出遮罩-文字按钮
        :return:
        """
        name_ = 'phototagfeelbig'
        return button.UIAButton(self.parent, name=name_)

    @property
    def address_button(self):
        """
            Summary:
                点击呼出遮罩-地点按钮
        :return:
        """
        name_ = 'phototagaddressbig'
        return button.UIAButton(self.parent, name=name_)

    @property
    def bottom_scroll_view(self):
        """
            Summary:
                底部滑动按钮模块
        Returns:

        """
        xpath_ = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]'
        return scroll_view.UIAScrollView(self.base_parent, xpath=xpath_)

    @property
    def bottom_edit_buttons(self):
        """
            Summary:
                底部编辑功能的各按钮
        Returns:

        """
        xpath_ = '//UIAScrollView[2]/UIAButton'
        return button.UIAButtonList(self.base_parent, xpath=xpath_).button_list

    # *************************首次操作的引导属性**********************
    @property
    def paster_guide(self):
        """
            Summary:
                贴纸引导
        """
        name_ = 'pasterForGirl'
        return button.UIAButton(self.parent, name=name_)

    @property
    def magic_tool_guide(self):
        """
            Summary:
                魔术棒引导
        Returns:

        """
        name_ = 'INPublishResource.bundle/publish_akey_guide-mask'
        return image.UIAImage(self.parent, name=name_)

    # **************************操作方法******************************

    def tap_finish_button(self):
        """
            Summary:
                点击完成按钮
        """
        log.logger.info("开始点击完成按钮")
        self.finish_button.tap()
        log.logger.info("结束完成按钮点击")
        if self.wait_window(windows.WindowNames.PUBLISH, 10):
            log.logger.info("成功进入发布页")
            return True
        log.logger.error("进入发布页失败")
        return False

    def is_guide_mask_exist(self):
        """
            Summary:
                是否存在引遮罩
        """
        if self.wait_for_element_present(self.parent, timeout=5, name='pasterForGirl'):
            log.logger.info("存在贴纸引导遮罩")
            return True
        if self.wait_for_element_present(self.parent, timeout=4, name='INPublishResource.bundle/publish_akey_guide-mask'):
            log.logger.info("存在魔法棒引导遮罩")
            return True
        log.logger.info("不存在引导遮罩")
        return False


class PhotoItem(base_frame_view.BaseFrameView):
    """
        Summary:
            照片item
    """
    def __init__(self, parent, item=None, index=None, **kwargs):
        super(PhotoItem, self).__init__(parent)
        self._layout_view = item if isinstance(item, WebElement) else self.find_element(**kwargs)
        self.__is_select = True
        self.__index = index

    def __getattr__(self, item):
        return getattr(self._layout_view, item, None)

    @property
    def is_selected(self):

        return self.__is_select

    def tap(self):
        """
            Summary:
                点击该图片
        """
        log.logger.info("开始点击选择{}照片".format('第' + str(self.__index) + '张' if self.__index is not None else '该'))
        self._layout_view.click()
        time.sleep(2)
        log.logger.info("点击完毕")

    # def select(self):
    #     """
    #         Summary:
    #             选择图片，点击图片区域即可选择，无需点击check_box
    #     """
    #     if not self.__is_select:
    #         log.logger.info("开始点击选择{}图片".format('第'+str(self.__index)+'张' if self.__index is not None else '该'))
    #         self._layout_view.click()
    #         time.sleep(2)
    #         self.__is_select = True
    #         log.logger.info("已完成图片选择")

    def unselect(self):
        """
            Summary:
                取消选择图片
        """
        if self.__is_select:
            log.logger.info("开始取消选择{}图片".format('第' + str(self.__index) + '张' if self.__index is not None else '该'))
            self._layout_view.click()
            time.sleep(3)
            self.__is_select = False
            log.logger.info("已完成图片取消选择")


class PhotoItemList(base_frame_view.BaseFrameView):

    def __init__(self, parent, **kwargs):
        super(PhotoItemList, self).__init__(parent)
        self.__item_list = self.find_elements(**kwargs)

    @property
    def item_list(self):
        if self.__item_list:
            log.logger.info("可视区域内图片个数为{}".format(len(self.__item_list)))
            return [PhotoItem(item.parent, item, index) for index, item in enumerate(self.__item_list, start=1)]
        return None
