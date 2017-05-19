## 1. 准备工作

> 1. 安装

>> 安装ideviceinstaller和ios-deploy
>>
>> brew install libimobiledevice --HEAD  #先安装依赖
>> 
>> 如果遇到  'Could not connect to lockdownd, error code -21' 错误，运行
>> sudo chmod -R 777 /var/db/lockdown/
>> 
>> brew install ideviceinstaller
>> 
>> npm install -g ios-deploy

>2. 检测

>> device_id -l #将真机链接到电脑，输入该命令，如果出现设备id，则说明安装成功
>>
>> deviceinfo -u _udid_ #会出现该设备的信息

## 2. 安装环境
> ### 检测设备信息
> #### 如果iOS device低于9.3，Appium版本不要高于1.6;
>
> #### 如果ios device高于9.3，需升级以下版本：
>
>> Appium version - 1.6.4
>>
>> Appium Client - 1.0.1 beta
>>
>> Mac OSX version - 10.12.1
>>
>> Xcode - 8.0
>>
>> 按照官方文档安装WDA https://github.com/appium/appium-xcuitest-driver/blob/master/docs/real-device-config.md
>>

## 3. 运行程序
> 非debug模式，直接运行  python clients_main.py [-m [module [-f [function]]]] 
>
> debug模式：
>>
>>先启动appium server
>>
>>然后create session #该会话需未指定webDriverAgentUrl
>>
>>等待appium log显示与手机进行通信之后，再安装启动WebDriverAgent， 默认端口8100进行通信
>>>
>>>xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=<udid>' test
>>>
>>>or更多详细信息
>>>
>>>xcodebuild build-for-testing test-without-building -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=<udid>' -configuration Debug -xcconfig Configurations/ProjectSettings.xcconfig
>
>遇到问题，可先重启手机，再重启服务和回话

