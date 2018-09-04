# -*- coding:utf-8 -*-
import urllib.request,urllib.parse
import configparser
import SaveResult,Login,DBConn
def HttpGetFindPictureListDriver():  #获取司机首页广告banner图
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getFindPictureList','url')
	pageNum=cf.get('getFindPictureList','pageNum')
	pageSize=cf.get('getFindPictureList','pageSize')
	placements=cf.get('getFindPictureList','placements')
	reponsestring=eval(Login.HttpLoginDriver())

	values={'pageNum':pageNum,'pageSize':pageSize,'placements':placements}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetFindPictureListAgent(): #获取经纪人首页广告banner图
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getFindPictureList','url')
	pageNum=cf.get('getFindPictureList','pageNum')
	pageSize=cf.get('getFindPictureList','pageSize')
	placements=cf.get('getFindPictureList','placements')
	reponsestring=eval(Login.HttpLoginAgent())

	values={'pageNum':pageNum,'pageSize':pageSize,'placements':placements}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetFindPictureListOwner():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getFindPictureList','url')
	pageNum=cf.get('getFindPictureList','pageNum')
	pageSize=cf.get('getFindPictureList','pageSize')
	placements=cf.get('getFindPictureList','placements')
	reponsestring=eval(Login.HttpLoginOwner())

	values={'pageNum':pageNum,'pageSize':pageSize,'placements':placements}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')

def getADPictures():
	resultstr1=HttpGetFindPictureListDriver()
	if '2000000' in resultstr1:
		SaveResult.save_result('广告','司机广告','pass')
	else:
		SaveResult.save_result('广告','司机广告','fail')
	resultstr2=HttpGetFindPictureListAgent()
	if '2000000' in resultstr2:
		SaveResult.save_result('广告','经纪人广告','pass')
	else:
		SaveResult.save_result('广告','经纪人广告','fail')
	resultstr3=HttpGetFindPictureListOwner()
	if '2000000' in resultstr3:
		SaveResult.save_result('广告','货主广告','pass')
	else:
		SaveResult.save_result('广告','货主广告','fail')

if __name__=='__main__':
	getADPictures()