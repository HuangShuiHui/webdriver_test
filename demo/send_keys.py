# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os, sys


if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = os.path.join(os.path.dirname(sys.path[0]), 'html/send_keys.html')
if not os.path.exists(file_path) :
    print('文件不存在!')
    exit(0)

dr.get('file:///'+file_path)

# copy content of A
dr.find_element_by_id('A').send_keys((Keys.CONTROL, 'a'))
dr.find_element_by_id('A').send_keys((Keys.CONTROL, 'x'))
sleep(2)


# paste to B
dr.find_element_by_id('B').send_keys((Keys.CONTROL, 'v'))
sleep(2)


# send keys to a
dr.find_element_by_id('A').send_keys(('watir', '-', 'webdirver', Keys.SPACE, 'is '))
sleep(2)

dr.quit()
