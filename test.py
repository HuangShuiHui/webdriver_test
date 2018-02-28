# /usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup as bs
import urllib,urllib2

url = "https://detail.tmall.hk/hk/item.htm?spm=a220m.1000858.1000725.1.673f66ccZUCFVE&id=531190944681&skuId=3166294273383&areaId=440300&user_id=2030008797&cat_id=2&is_b=1&rn=ebe7ac62cf78786e33950053c4dfe1b9";
response = urllib2.urlopen(url)
html = response.read()

soup = bs(html,'lxml')
print(soup.title)
title = soup.find_all('h1')
print(len(title))

price = soup.find_all(class_='tm-price')

print(price)

