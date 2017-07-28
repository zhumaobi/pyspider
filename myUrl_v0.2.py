#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-26 17:54:49
# @Author  : Maobi Zhu (zhumaobi@qq.com)
# @Link    : https://github.com/zhumaobi/pyhtonLearning

import requests

num = 0	
url = 'http://www.heibanke.com/lesson/crawler_ex02/'
while num<=30:
	data = {'username':'zhumaobi', 'password':str(num)}
	r = requests.post(url,data=data)

	if (r.text.find(u'密码错误') > 0):
		print('输入的密码%d错误！' %num)
		num += 1
	else:
		print(r.text)
		print('密码为%d' %num)
		break