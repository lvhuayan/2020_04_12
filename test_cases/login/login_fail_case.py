import os
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from commom.read_conf import read_config

ZentaoUrl = read_config().read_url()


class login_success_case(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(ZentaoUrl)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_fail(self):
        '''登录失败测试用例'''
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("DC123456")
        time.sleep(1)
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)
        self.assertTrue(EC.alert_is_present())
if __name__ == '__main__':
    # suite = unittest.TestSuite()
    unittest.main()
