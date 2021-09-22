import json
import sys
import unittest

from pageobjects.loginpage import LoginPage


class Wis_Dom_Car_002(unittest.TestCase):

    def test_Wis_Dom_Car_001(self):
        """
        1.打开在线警车，列表显示在线警车和未在线警车.
        """
        driver = LoginPage()
        # noinspection PyBroadException
        try:
            driver.logger.info('点击菜单按钮')
            driver.find_element_by_css_selector(driver.order_menu).click()
            driver.sleep(4)
            driver.logger.info('点击在线警车')
            driver.find_element_by_css_selector(driver.online_car_class).click()
            driver.sleep(1)
            for name in json.loads(driver.get_ini(driver.sys_address, 'online_car')):
                # 使用json.loads将读取的字符串转换为list
                self.assertTrue(driver.find_element_by_xpath(name), '未检查到:%s' % name)

        except Exception as e:
            driver.screen_shot(sys._getframe().f_code.co_name)
            self.assertTrue(False)
