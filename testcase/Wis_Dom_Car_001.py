import sys
import unittest

from pageobjects.loginpage import LoginPage


class Wis_Dom_Car_001(unittest.TestCase):

    def test_Wis_Dom_Car_001(self):
        """
            1.都为空点击登录
            2.输入已注册的用户名和错误的密码验证是否登录成功
            3.输入错误的用户名和错误的密码验证是否登录成功
            4.账户和密码是否大小写敏感
            5..输入已注册的用户名和正确的密码验证是否登录成功
        :return:
        """
        driver = LoginPage()
        # noinspection PyBroadException
        try:

            driver.logger.info("打开测试地址")
            driver.open_url(driver.get_ini(driver.sys_address, 'URL'))
            driver.sleep(2)
            driver.logger.info('步骤一：都为空点击登录')
            driver.find_element_by_css_selector(driver.span_name).click()
            driver.sleep(1)
            self.assertEqual(driver.find_element_by_xpath(driver.point_account).text, '请输入用户账户', '步骤一错误！')

            driver.logger.info('步骤二：输入已注册的用户名和错误的密码验证是否登录成功')
            driver.find_css_selector_placeholder(driver.account_name, driver.get_ini(driver.sys_address, 'name'))
            driver.find_css_selector_placeholder(driver.password_name, '666662')
            driver.logger.info('点击登录')
            driver.find_element_by_css_selector(driver.span_name).click()
            driver.sleep(2)
            self.assertEqual(driver.find_element_by_css_selector(driver.error_login).text, '账号或密码错误', '步骤二错误！')

            driver.logger.info("步骤三：输入错误账号和错误的密码")
            driver.clear('请输入用户账户')
            driver.clear('请输入密码')
            driver.find_css_selector_placeholder(driver.account_name, 'plkkinD')
            driver.find_css_selector_placeholder(driver.password_name, '66666663')
            driver.logger.info('点击登录')
            driver.sleep(2)
            driver.find_element_by_css_selector(driver.span_name).click()
            driver.sleep(1)
            self.assertEqual(driver.find_element_by_css_selector(driver.error_login).text, '请求超时', '步骤三错误！')
            driver.sleep(5)
            driver.logger.info('步骤五：输入正确的账号和密码')
            driver.clear('请输入用户账户')
            driver.sleep(1)
            driver.clear('请输入密码')
            driver.find_css_selector_placeholder(driver.account_name, driver.get_ini(driver.sys_address, 'name'))
            driver.find_css_selector_placeholder(driver.password_name, driver.get_ini(driver.sys_address, 'password'))
            driver.logger.info('点击登录')
            driver.find_element_by_css_selector(driver.span_name).click()
            driver.sleep(2)
            self.assertTrue(driver.find_element_by_css_selector(driver.order_menu), '步骤五错误！')
        except Exception as e:
            driver.screen_shot(sys._getframe().f_code.co_name)
            self.assertTrue(False)
