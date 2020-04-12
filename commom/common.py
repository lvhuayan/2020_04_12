import os
from selenium import webdriver
import unittest
from commom.read_conf import read_config

def open_Zentao():
    ZentaoUrl = read_config().read_url()
    driver = webdriver.Chrome()
    driver.get(ZentaoUrl)
    return driver