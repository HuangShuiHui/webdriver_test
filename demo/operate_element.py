# /usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
import os, sys

'''
点击，键盘输入，清空文字操作
'''

file_path = 'file:///'+os.path.abspath('../html/operate_element.html')
print file_path

dr = webdriver.Chrome()
dr.get(file_path)

dr.maximize_window()
# click
dr.find_element_by_class_name('dropdown-toggle').click()
sleep(1)
dr.find_element_by_link_text('Link1').click()

# clear
input = dr.find_element_by_xpath("//input[@name='in']")
input.clear()
sleep(1)
# send keys
input.send_keys('qwer')
sleep(2)

dr.quit()

