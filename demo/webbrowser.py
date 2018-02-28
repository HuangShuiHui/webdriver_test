# /usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time, os


url = 'http://www.baidu.com'


def startbrowser():
    print('启动和关闭浏览器')
    dr = webdriver.Chrome()
    url = 'http://www.baidu.com'
    dr.get(url)
    time.sleep(3)
    dr.quit()


def maxbrowsersize():
    dr = webdriver.Chrome()
    url = 'http://www.baidu.com'
    dr.get(url)
    print('浏览器窗口最大化')
    dr.maximize_window()
    time.sleep(3)
    dr.quit()


def setwindowsize(width,height):
    dr = webdriver.Chrome()
    url = 'http://www.3g.qq.com'
    dr.get(url)
    print('设置浏览器窗口大小')
    dr.set_window_size(width,height)
    time.sleep(3)
    dr.quit()

def print_titleandurl():
    if "HTTP_PROXY" in os.environ: del os.environ['HTTP_PROXY']
    dr = webdriver.Chrome()
    dr.get(url)
    print('title of current page is %s'%(dr.title))
    print('url of current page is %s'%(dr.current_url))
    time.sleep(1)
    dr.quit()


