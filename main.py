import os
import time
from selenium import webdriver
import unittest
import HTMLTestRunner

current_path = os.path.dirname('__file__')
report_path = os.path.join(current_path,'report')

cases_path = os.path.join(current_path,'test_cases')
report_html_path = os.path.join(report_path,'report_%s.html'%time.strftime('%Y_%m_%d_%H_%M_%S'))

discover = unittest.defaultTestLoader.discover(start_dir=cases_path,pattern='*_case.py',top_level_dir=cases_path)
main_suite = unittest.TestSuite()
main_suite.addTests(discover)

file = open(report_html_path,'wb')
report_html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='禅道自动化测试',description='禅道自动化测试实战演练')
report_html_runner.run(main_suite)


