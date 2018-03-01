# /usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import os, sys
import os.path as path

'''
层级定位练习
'''

file_path = 'file:///'+path.abspath('../html/level_locate.html')
print file_path

print('start')
dr = webdriver.Chrome()
dr.get(file_path)

dr.find_element_by_class_name('dropdown-toggle').click()

ul = dr.find_element_by_class_name('dropdown-menu')
while(ul.is_displayed()==False):
    pass
menu = ul.find_element_by_link_text('Another action')
webdriver.ActionChains(dr).move_to_element(menu).perform()

sleep(3)
dr.quit()