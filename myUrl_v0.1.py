#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-26 17:54:49
# @Author  : Maobi Zhu (zhumaobi@qq.com)
# @Link    : https://github.com/zhumaobi/pyhtonLearning

import urllib, urllib2
import re
from bs4 import BeautifulSoup

url = 'http://www.heibanke.com/lesson/crawler_ex00/'

request = urllib2.Request(url)
while True:	
	try:
		response = urllib2.urlopen(request)
	except urllib2.HTTPError as e:
		print e.code
		break
	except urllib2.URLError as e:
		print e.reason
		break

	soup = BeautifulSoup(response,"html.parser")
	for x in soup.h3.stripped_strings:
		print x
	my_num = soup.find(re.compile('h3'))
	#print my_num[0].string
	string = my_num.string
	num_to_wirte = re.search(r'\d+',string)
	if(num_to_wirte):
		url = 'http://www.heibanke.com/lesson/crawler_ex00/'+num_to_wirte.group()+'/'
		request = urllib2.Request(url)
	else:
		print '终于tmd找完了～!下面是最后的网页内容'
		print (soup.prettify())
		break;