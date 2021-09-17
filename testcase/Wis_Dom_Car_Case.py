import json
import logging
import sys
import time
import unittest

import document
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from pageobjects.loginpage import LoginPage
from pageobjects.testbase import TestBase


class WisDomCarCase(TestBase):
    @unittest.skipIf(True, '测试BUG')
    def test_Wis_Dom_Car_000(self):
        """
        临时BUG验证
        """
        driver = LoginPage(self.driver)
        driver.logger.info("开始测试")
        driver.open_url(driver.get_ini('testServer', 'URL'))
        driver.logger.info("输入账号")
        driver.find_element_by_css_selector(driver.account_name, driver.get_ini('account', 'name'))
        driver.sleep(1)
        driver.logger.info('输入密码')
        driver.find_element_by_css_selector(driver.password_name, driver.get_ini('account', 'password'))
        driver.sleep(60 * 40)
        driver.logger.info('点击登录')
        self.driver.find_element_by_css_selector(driver.span_name).click()
        driver.sleep(1)
        if self.driver.find_element_by_css_selector(driver.error_login).text == '账号或密码错误':  # 账号或密码错误
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            self.driver.get_screenshot_as_file('./screen/' + now + 'err.png')

    def test_Wis_Dom_Car_001(self):
        """
        登录
        :return:
        """
        driver = LoginPage(self.driver)
        # noinspection PyBroadException
        try:

            driver.logger.info("打开测试地址")
            driver.open_url(driver.get_ini(driver.sys_address, 'URL'))

            driver.logger.info('步骤一：都为空点击登录')
            self.driver.find_element_by_css_selector(driver.span_name).click()
            driver.sleep(1)
            self.assertEqual(self.driver.find_element_by_xpath(driver.point_account).text, '请输入用户账户', '步骤一错误！')

            driver.logger.info('步骤二：输入已注册的用户名和错误的密码验证是否登录成功')
            driver.find_element_by_css_selector(driver.account_name, driver.get_ini(driver.sys_address, 'name'))
            driver.find_element_by_css_selector(driver.password_name, '666662')
            driver.logger.info('点击登录')
            self.driver.find_element_by_css_selector(driver.span_name).click()
            driver.sleep(2)
            self.assertEqual(self.driver.find_element_by_css_selector(driver.error_login).text, '账号或密码错误', '步骤二错误！')

            driver.logger.info("步骤三：输入错误账号和错误的密码")
            driver.clear('请输入用户账户')
            driver.clear('请输入密码')
            driver.find_element_by_css_selector(driver.account_name, 'plkkinD')
            driver.find_element_by_css_selector(driver.password_name, '66666663')
            driver.logger.info('点击登录')
            driver.sleep(2)
            self.driver.find_element_by_css_selector(driver.span_name).click()
            driver.sleep(1)
            self.assertEqual(self.driver.find_element_by_css_selector(driver.error_login).text, '请求超时', '步骤三错误！')
            driver.sleep(5)
            driver.logger.info('步骤五：输入正确的账号和密码')
            driver.clear('请输入用户账户')
            driver.sleep(1)
            driver.clear('请输入密码')
            driver.find_element_by_css_selector(driver.account_name, driver.get_ini(driver.sys_address, 'name'))
            driver.find_element_by_css_selector(driver.password_name, driver.get_ini(driver.sys_address, 'password'))
            driver.logger.info('点击登录')
            self.driver.find_element_by_css_selector(driver.span_name).click()
            driver.sleep(2)
            self.assertTrue(self.driver.find_element_by_css_selector(driver.order_menu), '步骤五错误！')
        except Exception as e:
            driver.screen_shot(sys._getframe().f_code.co_name)
            self.assertTrue(False)

    def test_Wis_Dom_Car_002(self):

        driver = LoginPage('开始测试')
        # noinspection PyBroadException
        try:
            driver.logger.info('点击菜单按钮')
            self.driver.find_element_by_css_selector(driver.order_menu).click()
            driver.sleep(4)
            driver.logger.info('点击在线警车')
            self.driver.find_element_by_css_selector(driver.online_car_class).click()
            driver.sleep(1)
            for name in json.loads(driver.get_ini(driver.sys_address, 'online_car')):
                # 使用json.loads将读取的字符串转换为list
                self.assertTrue(self.driver.find_element_by_xpath(name), '未检查到:%s' % name)

        except Exception as e:
            driver.screen_shot(sys._getframe().f_code.co_name)
            self.assertTrue(False)

    def test_Wis_Dom_Car_003(self):
        driver = LoginPage('开始测试')
        # noinspection PyBroadException
        try:

            driver.logger.info('点击轨迹查询')
            self.driver.find_element_by_css_selector(driver.track_query_class).click()
            driver.sleep(1)
            driver.logger.info('选择热力图')
            driver.find_element_clear_readonly('请选择类型', '线路图')
            driver.sleep(1)
            self.driver.find_element_by_css_selector("[placeholder = '请选择部门']").click()
            driver.sleep(2)

            # 获取部门对应的警车
            car_number = json.loads(driver.get_ini(driver.sys_address, 'car_number'))

            driver.logger.info('选择的部门是:%s' % list(car_number.keys())[0])
            self.driver.find_element_by_xpath('//span[text() ="%s"]' % list(car_number.keys())[0]).click()
            driver.sleep(1)
            # 点击选择警车框
            self.driver.find_element_by_css_selector("[placeholder = '请选择警车']").click()
            driver.sleep(1)

            # 获取选择的部门下的第一个警车
            car = car_number[list(car_number.keys())[0]][0]
            driver.logger.info('选择的警车是:%s' % car)
            self.driver.find_element_by_xpath('//span[text() ="%s"]' % car).click()
            driver.sleep(1)
            driver.find_element_clear_readonly('开始时间', '2021-08-20 08:00:00')
            driver.sleep(1)
            self.driver.find_element_by_xpath('//span[contains(text(), "确定")]').click()
            driver.sleep(2)
            driver.find_element_clear_readonly('结束时间', '2021-09-13 08:00:00')
            driver.sleep(2)
            self.driver.find_element_by_xpath(driver.locus_end_time).click()
            driver.sleep(2)
            self.driver.find_element_by_css_selector(driver.inquire).click()
            driver.sleep(2)
        except Exception as e:
            driver.screen_shot(sys._getframe().f_code.co_name)
            self.assertTrue(False)
