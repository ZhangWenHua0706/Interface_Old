import urllib.request,urllib.parse
import configparser
import SaveResult,Login
def HttpIndexInfoDriver():   #获取司机首页广告语
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('IndexInfo','driver_url')
	reponsestring=eval(Login.HttpLoginDriver())
	pdata=''
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpIndexInfoAgent():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('IndexInfo','agent_url')
	reponsestring=eval(Login.HttpLoginAgent())
	pdata=''
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpIndexInfoOwner():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('IndexInfo','owner_url')
	reponsestring=eval(Login.HttpLoginOwner())
	pdata=''
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')

def IndexInfo():
	resultstr1=HttpIndexInfoDriver()
	if '2000000' in resultstr1:
		SaveResult.save_result('首页广告语','司机','pass')
	else:
		SaveResult.save_result('首页广告语','司机','fail')
	resultstr2=HttpIndexInfoAgent()
	if '2000000' in resultstr2:
		SaveResult.save_result('首页广告语','经纪人','pass')
	else:
		SaveResult.save_result('首页广告语','经纪人','fail')
	resultstr3=HttpIndexInfoOwner()
	if '2000000' in resultstr3:
		SaveResult.save_result('首页广告语','货主','pass')
	else:
		SaveResult.save_result('首页广告语','货主','fail')

if __name__=='__main__':
	IndexInfo()