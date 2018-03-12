#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
窗口句柄操作
'''

from selenium import webdriver
from time import sleep



dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
dr.implicitly_wait(5)



navs = dr.find_elements_by_class_name('mnav')
# 获取当前窗口句柄
for nav in navs:
    nav.click()
    h = dr.current_window_handle
    handles = dr.window_handles
    print len(handles)
    for handle in handles:
        if handle != h:
            dr.switch_to.window(handle)
            print(dr.title)
            sleep(3)
            dr.close()
    dr.back()
print('end')
dr.quit()