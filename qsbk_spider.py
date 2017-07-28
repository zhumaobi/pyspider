#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 12:44:27
# @Author  : Maobi Zhu (zhumaobi@qq.com)
# @Link    : https://github.com/zhumaobi/pyhtonLearning
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
headers = {
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"
}
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	#print response.read()
except urllib2.URLError as e:
	if(hasattr(e,'code')):
		print e.code
	if(hasattr(e,'reason')):
		print e.reason

content = response.read().decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')

pattern_id = re.compile(r'qiushi_tag_\d+')

#pattern = re.compile('<div.*?clearfix".*?<h2>(.*?)</h2></a>.*?<span>(.*?)</span>.*?<!--.*?-->(.*?)'+
#	'<div class="stats.*?stats-vote.*?number">(.*?)</i>.*?stats-coments.*?number">(.*?)</i>',re.S)
items = soup.find_all('div',id=pattern_id)

pattern_item = re.compile(r'<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<!-- 图片或gif -->(.*?)<div class="stats">.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<a class="qiushi_comments".*?"number">(.*?)</i>',re.S)
for items_iterator in items :
	for item in re.findall(pattern_item, str(items_iterator)):
			haveimg = re.search('img',item[2])
			if(not haveimg):
				print item[0],item[1],item[2],item[3],item[4]


