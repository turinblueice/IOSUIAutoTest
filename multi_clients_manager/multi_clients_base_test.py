#  -*-coding:utf8-*-

################################################################################
#
#
#
################################################################################
"""
模块用法说明: 多客户端执行和管理模块

Authors: turinblueice
Date:    16/4/19 12:00
"""

import Queue
import os
import threading

from appium import webdriver
from multi_clients_manager import available_ports

from base import thread_device_pool
from model import model
from util import log
from util import switch


class AppiumDevicesPortsInfo(object):
    device_queue = Queue.Queue()
    ports_queue = Queue.Queue()  # 端口队列


class MultiClientsBaseTest(object):

    """
        Summary:
            - 多客户端执行管理类
    """
    config_model = model.config_parser
    mutex = threading.Lock()
    curr_host = available_ports.AvailablePorts.get_local_ip()

    def __init__(self, **kwargs):
        super(MultiClientsBaseTest, self).__init__()

        self.device = None
        # self.package_name = kwargs.get('package', '')  # 包名
        # self.platform = kwargs.get('platform', 'IOS')  # 平台

        # *************运行方式控制属性*************
        self.debug_mode = switch.switch.debug

    @staticmethod
    def app_path(file_path):

        return os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))

    @staticmethod
    def create_driver(debug=False):
        """
            Summary:
                创建webdriver
            Args:
                debug:调试模式
        """
        key = MultiClientsBaseTest.get_current_key()
        config_model = MultiClientsBaseTest.config_model
        if not debug:
            if key not in thread_device_pool.ThreadDeviceInfoPool.thread_device_pool:
                # 若当前线程不在全局线程字典内,则该线程入栈
                with MultiClientsBaseTest.mutex:
                    # 加锁,确保逐个进入线程字典,如此不会导致字典元素数量编号出错
                    thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key] = dict()

                    thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['port'] = \
                        AppiumDevicesPortsInfo.ports_queue.get_nowait() \
                        if not AppiumDevicesPortsInfo.ports_queue.empty() else None

                    thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['device'] = \
                        AppiumDevicesPortsInfo.device_queue.get_nowait() \
                        if not AppiumDevicesPortsInfo.device_queue.empty() else None

                    thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['thread_number'] = \
                        str(len(thread_device_pool.ThreadDeviceInfoPool.thread_device_pool))  # 对当前线程进行编号

                    log.logger.info(
                        "当前线程名称为{},ID为{},编号为{}".format(
                            threading.currentThread().name,
                            threading.currentThread().ident,
                            thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['thread_number']))

            port = thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['port']
            device = thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['device']

            port = port or config_model.get('default_capabilities', 'port')

            device_name = device['device_name'] if device and 'device_name' in device \
                else device['device_brand'] + ' ' + device['device_model'] or config_model.get('default_capabilities', 'device_name')

            platform_version = device['device_os_version'] \
                if device else config_model.get('default_capabilities', 'platform_version')

            udid = device['device_id'] if device else config_model.get('default_capabilities', 'udid')

            log.logger.info("设备名称:{},设备ID:{},使用端口:{},运行线程:{}".format(
                device_name, udid, port, threading.currentThread().ident))

            driver = webdriver.Remote(
                command_executor='http://{host}:{port}/wd/hub'.format(host=MultiClientsBaseTest.curr_host, port=port),
                desired_capabilities={
                    'app': MultiClientsBaseTest.app_path(config_model.get('default_capabilities', 'app')),
                    'platformName': config_model.get('default_capabilities', 'platform_name'),
                    'platformVersion': platform_version,
                    'deviceName': device_name,  # IOS：instruments -s devices；Android:随便写
                    'udid': udid,  # 设备号
                    'bundleId': config_model.get('default_capabilities', 'bundle_id'),
                    'noReset': True if config_model.get('default_capabilities', 'no_reset') == 'True' else False,
                    'autoAcceptAlerts': True if config_model.get('default_capabilities',
                                                                 'auto_accept_alerts') == 'True' else False,
                    'waitForAppScript': config_model.get('default_capabilities', 'wait_for_app_script'),
                    'webDriverAgentUrl': config_model.get('default_capabilities', 'web_driver_agent_url')

                })

        else:
            port = config_model.get('default_capabilities', 'port')
            driver = webdriver.Remote(
                command_executor='http://{host}:{port}/wd/hub'.format(host=MultiClientsBaseTest.curr_host, port=port),
                desired_capabilities={
                    'app': os.path.abspath(os.path.join(os.path.dirname(__file__), '../res/infashiondebug.ipa')),
                    'platformName': config_model.get('default_capabilities', 'platform_name'),
                    'platformVersion': config_model.get('default_capabilities', 'platform_version'),
                    'deviceName': config_model.get('default_capabilities', 'device_name'),  # IOS：instruments -s devices 之一；Android:随便写
                    'bundleId': config_model.get('default_capabilities', 'bundle_id'),
                    'udid': config_model.get('default_capabilities', 'udid'),
                    'noReset': True if config_model.get('default_capabilities', 'no_reset') == 'True' else False,
                    'autoAcceptAlerts': True if config_model.get('default_capabilities', 'auto_accept_alerts') == 'True' else False,
                    'waitForAppScript': config_model.get('default_capabilities', 'wait_for_app_script')

                })
            thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key] = dict()
            thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['thread_number'] = '1'

        thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['driver'] = driver
        log.logger.info("该线程id:{},driver地址{}".format(threading.currentThread().ident, id(driver)))

        return driver

    @staticmethod
    def get_current_key():

        key = thread_device_pool.ThreadDeviceInfoPool.get_current_key()
        return key

    @staticmethod
    def get_current_device():

        device = thread_device_pool.ThreadDeviceInfoPool.get_current_device()
        return device

    @staticmethod
    def get_driver():

        key = MultiClientsBaseTest.get_current_key()
        if key in thread_device_pool.ThreadDeviceInfoPool.thread_device_pool:
            if 'driver' in thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]:
                driver = thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['driver']
                return driver
        return None

    @staticmethod
    def get_current_thread_id():

        thread_id = thread_device_pool.ThreadDeviceInfoPool.get_current_thread_id()
        return thread_id

    @staticmethod
    def get_current_thread_number():
        """
            Summary:
                获取当前线程编号
        """
        key = MultiClientsBaseTest.get_current_key()
        return thread_device_pool.ThreadDeviceInfoPool.thread_device_pool[key]['thread_number']
