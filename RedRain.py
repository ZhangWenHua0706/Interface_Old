#-*- coding: utf-8 -*-
import sys
import urllib.request,urllib.parse
import json
import random
from selenium import webdriver
#filename='session1000.txt'
def HttpReq(urlstring):    #发送http请求
	req = urllib.request.Request(urlstring)
	response = urllib.request.urlopen(req) 
def GetScreenings():                  #获取最新场次
	StrUrl='http://114.55.186.63:8081/front/f/tpl/activity/getActivityStatus.act'
	req = urllib.request.Request(StrUrl)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	d=eval(the_page.decode('ascii'))
	screenings=d.get("screenings")
	return screenings
def GetHttpUrl(filename):    #组装url并调用http请求函数
	f=open(filename,'r')
	try:
		line=f.readline()
		while line:
			str1=line[0:69]
			para1=random.randint(3, 30)
			str2=line[69:81]
			para2=GetScreenings()
			str3=line[81:142]
			fullstr=str1+str(para1)+str2+str(para2)+str3
			line=f.readline()
			HttpReq(fullstr)
	finally:
		f.close()
	
def HttpReq2(urlstring,amount,screenings,sessionid,customer_id):
	values={'amount':amount,'screenings':screenings,'sessionId':sessionid,'customer_id':customer_id}
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	pdata=urllib.parse.urlencode(values)
	req=urllib.request.Request(url=urlstring,data=pdata,headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	print (the_page)
def GetHttpUrl2(filename):    #组装url并调用http请求函数
	f=open(filename,'r')
	num=0
	try:
		line=f.readline()
		while line:
			str1=line[0:69]
			para1=GetScreenings()
			str2=line[69:130]
			fullstr=str1+str(para1)+str2
			print (fullstr)
			HttpReq(fullstr)
			num=num+1
			print (num)
			line=f.readline()
	finally:
		f.close()
	
if __name__=='__main__':
	#GetHttpUrl('session1000.txt')
	GetHttpUrl2('session350.txt')
	#HttpReq2('http://114.55.186.63:8081/front/f/tpl/activity/saveReward.act','22','23','77c74a10ff89ff937ab5b1a37c31b556','160249')

	print ("OVER!!!")