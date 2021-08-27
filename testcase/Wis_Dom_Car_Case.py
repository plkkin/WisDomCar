import unittest

from selenium.webdriver.common.by import By

from pageobjects.loginpage import LoginPage
from pageobjects.testbase import TestBase


class WisDomCarCase(TestBase):

    def test_Wis_Dom_Car_001(self):
        """
        登录
        :return:
        """
        driver = LoginPage(self.driver)
        driver.logger.info("开始测试")
        driver.open_url(driver.get_ini('testServer', 'URL'))
        driver.logger.info("输入账号")
        driver.find_element_by_css_selector(driver.account_name, driver.get_ini('account', 'name'))
        driver.sleep(1)
        driver.logger.info('输入密码')
        driver.find_element_by_css_selector(driver.password_name, driver.get_ini('account', 'password'))
        driver.sleep(1)
        driver.logger.info('点击登录')
        self.driver.find_element_by_css_selector(driver.span_name).click()
        driver.sleep(2)

    def test_Wis_Dom_Car_002(self):
        self.driver.logger.info('开始测试')
        self.driver.find_element_by_css_selector('#app > div > div.zd--index--head > div.head--left > img').click()
        self.driver.sleep(5)
