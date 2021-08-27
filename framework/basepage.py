import configparser
import time

from framework.logger import Logger


class BasePage(object):
    """
    页面基类
    """
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger(logger='Message').getlog()

        self.cf = configparser.ConfigParser()
        self.cf.read('./config/config.ini')

    def open_url(self, url):
        self.logger.info('打开地址%s', url)
        self.driver.get(url)

    def find_element(self, loc):
        return self.driver.find_element(*loc)

    def end_keys(self, selector, text):
        el =self.driver.find_element(selector)
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
        return self.driver.find_element_by_css_selector("[placeholder='%s']" % placeholder).send_keys(text)

