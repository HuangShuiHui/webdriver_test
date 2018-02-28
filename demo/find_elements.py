# /usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
import os, sys

'''
通过 find_elements 来定位一组对象
'''

# 获取html文件地址
file_path = os.path.join(os.path.dirname(sys.path[0]),'html/checkbox.html')
print file_path
if os.path.exists(file_path):
    print('start')
    dr = webdriver.Chrome('F:\py_space\webdriver\chromedriver.exe')
    # 打开网页
    dr.get('file:///'+file_path)

    # 选择所有的checkbox并全部勾选
    checkbox = dr.find_elements_by_xpath("//input[@type='checkbox']")
    print len(checkbox)
    for box in checkbox:box.click()
    sleep(1)
    print('重置所有checkbox')
    for box in checkbox: box.click()
    [input.click() for input in dr.find_elements_by_tag_name('input') if input.get_attribute('type')=='check']

    checkbox[-1].click()

    sleep(1)
    dr.quit()