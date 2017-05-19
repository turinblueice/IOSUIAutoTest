#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 应用各UIAWindow的名称

Authors: turinblueice
Date: 2016/7/28
"""


class WindowNames(object):

    LOGIN_MAIN = 'name_login_background.png'   # 登录页的名称
    IN_MAIN = 'name_paizhao'  # in主页名称,in主页底部tab存在拍照按钮固定不变
    IN_CENTER = 'name_我的'  # in主页-中心页

    LOGIN_FRIEND_RECOMMEND = 'name_推荐好友'  # 登录的好友推荐页

    USER_INFO = 'name_编辑资料'  # 编辑资料名称
    CROPPER = 'name_选取'  # 裁剪图片名称
    USER_SETTING = 'name_设置'  # 用户设置页的activity名称

    PASTER_MALL = 'name_INPasterMallResource.bundle/pastermallbg.jpg'  # 我的贴纸
    PASTER_DIY_GUIDE = 'name_INPasterMallResource.bundle/pasterdiy_addguide'  # 创建贴纸的引导
    CUSTOM_PASTER_CROP = 'name_选择区域'   # 自定义贴纸裁剪选择页
    CUSTOM_PASTER_EDITOR = 'name_自定义贴纸'  #自定义贴纸搭配页
    SELECT_PHOTO_GUIDE = 'name_INPasterMallResource.bundle/pasterdiy_selectimagetip'  # 图片选择引导页
    CHOOSE_PART_PASTER = 'name_选择想要的部分'  # 图片编辑筛选页

    CAMERA = 'name_INPublishResource.bundle/camera_opening_above.png'  # 照片编辑/拍照页,滑动切换滤镜说明所在页
    PUBLISH_CORE = 'name_INPublishResource.bundle/tag_local'  # 图片加工发布页面
    PUBLISH = 'name_发布'  # 图片发布页

    PHOTO_STORY_GALLERY = 'name_相机胶卷'  # 故事集/图片选择页,顶部"相机胶卷"文字不变
    PHOTO_TAKING = 'name_PhotoCapture'  # 拍照页
    PHOTO_ALBUM_PICKER = 'name_照片'  # 照片集上传页的标志/照片集选取页

    STORY_EDIT = 'name_编辑故事'  # 故事编辑页
    STORY_DETAIL = 'name_INAlbumDetailWhiteBack'  # 故事预览/详情页
    STORY_SETTING = 'name_故事集设置'  # 故事集设置页
    STORY_SHARE = 'name_发布成功!'  # 故事发布成功分享页

    ADD_FRIEND = '.usercenter.activity.UserCenterFriendsAddActivity'  # 添加好友页
    USER_CENTER_FRIEND = 'name_我的好友'  # 用户中心的我的好友页

    DIARY_INFO = '.diary.other.v260.DiaryOtherActivity'  # 日记主页
    PHOTO_ALBUM_CORE = '.photo.PhotoCoreActivity'  # 图片集详情页

    TOPIC_DETAIL = '.module.tag.activity.TagActivityV253'  # 话题详情页
    FRIEND_PHOTO_DETAIL = '.friend.activity.FriendPhotoDetailActivity'  # 好友图片详情页