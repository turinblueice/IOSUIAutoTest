## 1. 准备工作

> 1. 安装依赖

>> mac下需安装ideviceinstaller和ios-deploy，以获得设备命令行操作的支持
>>
>> 
>>  ```bash
>>
>>  brew install libimobiledevice --HEAD  #先安装依赖
>>
>> ```
>> 
>> 如果遇到  'Could not connect to lockdownd, error code -21' 错误，运行
>> ```bash 
>> sudo chmod -R 777 /var/db/lockdown/
>> 
>> brew install ideviceinstaller
>> 
>> npm install -g ios-deploy
>> ```

>2. 检测安装

>>```bash
>> idevice_id -l #将真机链接到电脑，获取移动设备的udid，则工具安装成功
>>
>> ideviceinfo #获取移动设备的详细信息
>>```
>>


## 2. 运行／开发环境配置
>
> ### 检测设备信息
>
> 若IOS设备系统版本高于9.3，需做以下升级
>
>> Appium升级至1.6.4及以上
>>
>> Appium Client升级至1.0.1 beta及以上
>>
>> Mac OSX升级至10.12.0及以上
>>
>> Xcode升级到8.0及以上
>>
>> 按照官方文档安装WDA https://github.com/appium/appium-xcuitest-driver/blob/master/docs/real-device-config.md
>>

## 3. 运行程序
> 非debug模式
>
> 直接运行  
>  ```python
>  python  clients _main.py [-m [module [-f [function]]]] 
>  ```
>
> debug模式：
>>
>>先启动appium server
>>
>>然后创建appium会话（create session） #该会话需未指定webDriverAgentUrl
>>
>>等待appium log显示与手机进行通信之后，再安装启动WebDriverAgent， 默认端口8100进行通信
>>>
>>>xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=<udid>' test
>>>
>>>or更多详细信息
>>>
>>>xcodebuild build-for-testing test-without-building -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=<udid>' -configuration Debug -xcconfig Configurations/ProjectSettings.xcconfig
>
>遇到问题，可先重启手机，再重启服务和会话

