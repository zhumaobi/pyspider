#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 16:48:02
# @Author  : Maobi Zhu (zhumaobi@qq.com)
# @Link    : https://github.com/zhumaobi/pyhtonLearning
from bs4 import BeautifulSoup
import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/maobizhu/Documents/python_codes/chromedriver')
driver.get('http://www.heibanke.com/lesson/crawler_ex01/');
time.sleep(1)
nick_box = driver.find_element_by_name('username')
nick_box.send_keys('zhaolaomei')
password_box = driver.find_element_by_name('password')
num = 0
password_box.send_keys('%d'%num)
driver.find_element_by_id('id_submit').click()
time.sleep(1)

while num<30:
	html = driver.page_source
	soup = BeautifulSoup(html,'html.parser')
	msg = soup.h3.string
	if(msg.find(u'密码错误')>0):
		num += 1
		driver.get('http://www.heibanke.com/lesson/crawler_ex01/');
		time.sleep(1)
		nick_box = driver.find_element_by_name('username')
		nick_box.send_keys('zhaolaomei')
		password_box = driver.find_element_by_name('password')
		password_box.send_keys('%d'%num)
		driver.find_element_by_id('id_submit').click()
		time.sleep(1)
	else:
		print html
		break
time.sleep(1)
driver.close()