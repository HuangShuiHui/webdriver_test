# /usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


file_path = os.path.abspath('../html/button_group.html')
if not os.path.exists(file_path):
    print('文件不存在！',file_path)
    exit(0)


dr = webdriver.Chrome()
dr.get(file_path)

sleep(2)

btns = dr.find_element_by_class_name('btn-group').find_elements_by_class_name('btn')
for btn in btns :
    if btn.text == 'second':
        #btn.click()
        print('find second button')
        sleep(2)


dr.quit()