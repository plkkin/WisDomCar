import json
import sys
import unittest

from pageobjects.loginpage import LoginPage


class Wis_Dom_Car_003(unittest.TestCase):
    def test_Wis_Dom_Car_001(self):
        driver = LoginPage()
        # noinspection PyBroadException
        try:

            driver.logger.info('点击轨迹查询')
            driver.find_element_by_css_selector(driver.track_query_class).click()
            driver.sleep(1)
            driver.logger.info('选择热力图')
            driver.find_element_clear_readonly('请选择类型', '线路图')
            driver.sleep(1)
            driver.find_element_by_css_selector("[placeholder = '请选择部门']").click()
            driver.sleep(2)

            # 获取部门对应的警车
            car_number = json.loads(driver.get_ini(driver.sys_address, 'car_number'))

            driver.logger.info('选择的部门是:%s' % list(car_number.keys())[0])
            driver.find_element_by_xpath('//span[text() ="%s"]' % list(car_number.keys())[0]).click()
            driver.sleep(1)
            # 点击选择警车框
            driver.find_element_by_css_selector("[placeholder = '请选择警车']").click()
            driver.sleep(1)

            # 获取选择的部门下的第一个警车
            car = car_number[list(car_number.keys())[0]][0]
            driver.logger.info('选择的警车是:%s' % car)
            driver.find_element_by_xpath('//span[text() ="%s"]' % car).click()
            driver.sleep(1)
            driver.find_element_clear_readonly('开始时间', '2021-08-20 08:00:00')
            driver.sleep(1)
            driver.find_element_by_xpath('//span[contains(text(), "确定")]').click()
            driver.sleep(2)
            driver.find_element_clear_readonly('结束时间', '2021-09-13 08:00:00')
            driver.sleep(2)
            driver.find_element_by_xpath(driver.locus_end_time).click()
            driver.sleep(2)
            driver.find_element_by_css_selector(driver.inquire).click()
            driver.sleep(2)
            driver.quit()
        except Exception as e:
            driver.screen_shot(sys._getframe().f_code.co_name)
            self.assertTrue(False)
