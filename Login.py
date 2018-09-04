# -*- coding:utf-8 -*-
import AESEncrypt
import requests
import configparser
import SaveResult

def HttpLoginDriver():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('login','url')
	mobile1=cf.get('login','mobile1')
	password=cf.get('login','password')
	usertype=1
	mobile=AESEncrypt.MyCrypt().encrypt(mobile1).decode('utf-8')
	customerPwd=AESEncrypt.MyCrypt().encrypt(password).decode('utf-8')
	values={'mobile':mobile,'customerPwd':customerPwd,'type':usertype}
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	response=requests.post(url=urlstring,data=values,headers=headers)
	return response.text
def HttpLoginAgent():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('login','url')
	mobile2=cf.get('login','mobile2')
	password=cf.get('login','password')
	usertype=1
	mobile=AESEncrypt.MyCrypt().encrypt(mobile2).decode('utf-8')
	customerPwd=AESEncrypt.MyCrypt().encrypt(password).decode('utf-8')
	values={'mobile':mobile,'customerPwd':customerPwd,'type':usertype}

	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	response = requests.post(url=urlstring, data=values, headers=headers)
	return response.text

def HttpLoginOwner():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('login','url')
	mobile3=cf.get('login','mobile3')
	password=cf.get('login','password')
	usertype=1
	mobile=AESEncrypt.MyCrypt().encrypt(mobile3).decode('utf-8')
	customerPwd=AESEncrypt.MyCrypt().encrypt(password).decode('utf-8')
	values={'mobile':mobile,'customerPwd':customerPwd,'type':usertype}
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	response=requests.post(url=urlstring,data=values,headers=headers)
	return response.text
def LoginUser():
	resultstr1=HttpLoginDriver()
	if '2000000' in resultstr1:
		SaveResult.save_result('用户登录'.decode('utf-8'),'登录司机'.decode('utf-8'),'pass')
	else:
		SaveResult.save_result('用户登录'.decode('utf-8'),'登录司机'.decode('utf-8'),'fail')
	resultstr2=HttpLoginAgent()
	print (resultstr2)
	if '2000000' in resultstr2:
		SaveResult.save_result('用户登录'.decode('utf-8'),'登录经纪人'.decode('utf-8'),'pass')
	else:
		SaveResult.save_result('用户登录'.decode('utf-8'),'登录经纪人'.decode('utf-8'),'fail')
	resultstr3=HttpLoginOwner()
	if '2000000' in resultstr3:
		SaveResult.save_result('用户登录'.decode('utf-8'),'登录货主'.decode('utf-8'),'pass')
	else:
		SaveResult.save_result('用户登录'.decode('utf-8'),'登录货主'.decode('utf-8'),'fail')

if __name__=='__main__':
	LoginUser()