## 1. 准备工作


mac下需安装ideviceinstaller和ios-deploy，以获得设备命令行操作的支持


 ```bash

 brew install libimobiledevice --HEAD  #先安装依赖

 ```

 如果遇到  'Could not connect to lockdownd, error code -21' 错误，运行
 ```bash 
 sudo chmod -R 777 /var/db/lockdown/
 
brew install ideviceinstaller

 npm install -g ios-deploy
 ```

运行以下命令检查安装结果
```bash
 idevice_id -l #将真机链接到电脑，获取移动设备的udid，则工具安装成功

 ideviceinfo #获取移动设备的详细信息
```


## 2. 环境配置

 检测设备信息,若IOS设备系统版本高于9.3，需做以下升级:

 - Appium升级至1.6.4及以上
 - Appium Client升级至1.0.1 beta及以上
 - Mac OSX升级至10.12.0及以上
 - Xcode升级到8.0及以上

 按照官方文档安装WDA https://github.com/appium/appium-xcuitest-driver/blob/master/docs/real-device-config.md


## 3. 运行程序

 - 非debug模式下直接运行  
 
     ```python
      python  clients_main.py  [-m [module [-f [function]]]] 
     ```
     或者为了获取case通过率的xml支持，可运行
     ```python
      python  clients_main_nose.py  [-m [module [-f [function]]]] 
     ```
     
 - debug模式（需将util/switch.conf的debug置为True）下按以下步骤：
     - 启动appium server
     - 创建appium会话（create session），建议在webdriver创建参数中不加入webDriverAgentUrl
     - （移动设备系统版本为9.3以上需要）等待appium server log显示与手机进行通信之后，再启动移动设备中的WebDriverAgent， 默认使用8100端口进行通信，命令> 行下启动命令如下
     
        ```bash
            xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 
            'id=<udid>' test
        ```
        
     - 若要获取更多详细信息，可执行命令
    
        ```bash
           xcodebuild build-for-testing test-without-building -project WebDriverAgent.xcodeproj -scheme  
           WebDriverAgentRunner -destination 'id=<udid>' -configuration Debug -xcconfig
           Configurations/ProjectSettings.xcconfig   
        ```

若遇到问题，可先重启手机，再重启服务和会话


