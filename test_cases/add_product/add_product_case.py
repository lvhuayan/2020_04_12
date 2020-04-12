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

    def test_add_product_case(self):
        '''添加产品'''
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("CD123456")
        time.sleep(1)
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[@href="/biz/product-index-no.html"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//i[@class="icon icon-sm icon-plus"]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//input[@class="form-control input-product-title"]').send_keys("测试产品003")
        self.driver.find_element_by_xpath('//input[@class="form-control input-product-code"]').send_keys("productcode003")
        product_button = self.driver.find_element_by_xpath('//*[@id="submit"]')
        product_button.send_keys("\n")
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@href="/biz/product-index-no.html"]').click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element_by_xpath('//a[@title="测试产品003"]'))
if __name__ == '__main__':
    # suite = unittest.TestSuite()
    unittest.main()
