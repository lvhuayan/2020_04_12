import os
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from commom.read_conf import read_config

ZentaoUrl = read_config().read_url()
class logout_case(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(ZentaoUrl)
    def tearDown(self) -> None:
        self.driver.quit()
    def test_logout(self):
        '''退出登录测试用例'''
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("CD123456")
        time.sleep(1)
        self.driver.find_element_by_id("submit").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@class="dropdown-toggle"]').click()
        self.driver.find_element_by_xpath('//a[@href="/biz/user-logout.html"]').click()
        time.sleep(2)
        self.assertTrue(EC.visibility_of(self.driver.find_element_by_id("account")))



if __name__ == '__main__':
    # suite = unittest.TestSuite()
    unittest.main()
