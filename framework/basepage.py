import configparser
import time

import document as document

from framework.logger import Logger


class BasePage(object):
    """
    页面基类
    """
    __instance = None
    __init_flag = False  # 创建类属性用于__init__方法中的判断

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            # return 上一次创建的对象的引用
            return cls.__instance

    def __init__(self, driver):
        if not BasePage.__init_flag:
            self.driver = driver
            self.sys_address = '218_server'  # 连接的服务器地址
            self.logger = Logger(logger='Message').getlog()

            self.cf = configparser.ConfigParser()
            self.cf.read('./config/config.ini', encoding="utf-8-sig")
            BasePage.__init_flag = True  # 赋值  init只初始化一次

    def open_url(self, url):
        self.logger.info('打开地址%s', url)
        self.driver.get(url)

    def find_element(self, loc):
        return self.driver.find_element(*loc)

    def end_keys(self, selector, text):
        el = self.driver.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            self.logger.info('输入：%s', text)
        except NameError as e:
            self.logger.info('输入:%s失败!!', text)

    def sleep(self, seconds):
        time.sleep(seconds)
        self.logger.info('等待%s秒', seconds)

    def get_ini(self, option, host):
        return self.cf.get(option, host)

    def find_element_by_css_selector(self, placeholder, text):
        self.logger.info('预输入框%s输入内容：%s' % (placeholder, text))
        return self.driver.find_element_by_css_selector("[placeholder='%s']" % placeholder).send_keys(text)

    def find_element_clear_readonly(self, placeholder, text):
        '''
         利用JS代码消除readonly属性  进行填充文字
        '''
        bumen = self.driver.find_element_by_css_selector("[placeholder='%s']" % placeholder)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", bumen)
        bumen.clear()
        return bumen.send_keys(text)

    def find_element_clear_disaply(self, placeholder, text):
        '''
         利用JS代码消除readonly属性  进行填充文字
        '''
        bumen = self.driver.find_element_by_css_selector("[placeholder='%s']" % placeholder)

        self.driver.execute_script("arguments[0].removeAttribute('disabled')", bumen)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", bumen)
        self.driver.execute_script('arguments[0].value = "豫R3D369"', bumen)

    def screen_shot(self, func_name):
        """
        截图
        """
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.driver.get_screenshot_as_file('./screen/%s_%s.png' % (func_name, now))

    def clear(self, name):
        """
        根据预输入清楚内容
        """
        self.logger.info('清除预输入框"%s"的内容', name)
        return self.driver.find_element_by_css_selector("[placeholder='%s']" % name).clear()
