#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import configparser

class read_config:

    def __init__(self):
        #获取当前文件的路径
        current_path = os.path.dirname(__file__)
        self.whole_path = os.path.join(current_path,'../conf/config.ini')
        # self.current_path = self.whole_path.replace('\\','/')
        # print (self.whole_path)
        self.conf = configparser.ConfigParser()
        self.conf_read = self.conf.read(self.whole_path,encoding='utf-8')

    def read(self,sec,option):
        return self.conf.get(sec,option)
    # def read_db_server(self):
    #     return self.read('default','db_server')
    def read_url(self):
        return self.read('default','url')

readConfig = read_config()

if __name__ == '__main__':
    # print (readConfig.read_db_server())
    print (readConfig.read_url())
