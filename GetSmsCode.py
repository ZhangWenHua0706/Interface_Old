# -*- coding:utf-8 -*-
import urllib.request,urllib.parse
import configparser
import time
import SaveResult
def httpPost(account):
	values={'mobile':account}
	pdata=urllib.parse.urlencode(values)
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('GetSmsCode','url')
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page
def getSmsCode(account):
	resultstr=httpPost(account).decode()
	if '2000000' in resultstr:
		SaveResult.save_result('用户注册','获取验证码','pass')
	else:
		SaveResult.save_result('用户注册','获取验证码','fail')
if __name__=='__main__':
	getSmsCode('19933331111')