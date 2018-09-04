import urllib.request,urllib.parse
import configparser
import SaveResult,Login,DBConn
def HttpMyInfoDriver():            #获取司机个人信息
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('MyInfo','driver_url')
	reponsestring=eval(Login.HttpLoginDriver())
	customerId=reponsestring['data']['customerInfo']['customerId']
	values={'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpMyInfoAgent():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('MyInfo','agent_url')
	reponsestring=eval(Login.HttpLoginAgent())
	customerId=reponsestring['data']['customerInfo']['customerId']
	values={'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpMyInfoOwner():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('MyInfo','owner_url')
	reponsestring=eval(Login.HttpLoginOwner())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')

def MyInfo():
	resultstr1=HttpMyInfoDriver()
	if '2000000' in resultstr1:
		SaveResult.save_result('个人资料','司机','pass')
	else:
		SaveResult.save_result('个人资料','司机','fail')
	resultstr2=HttpMyInfoAgent()
	if '2000000' in resultstr2:
		SaveResult.save_result('个人资料','经纪人','pass')
	else:
		SaveResult.save_result('个人资料','经纪人','fail')
	resultstr3=HttpMyInfoOwner()
	if '2000000' in resultstr3:
		SaveResult.save_result('个人资料','货主','pass')
	else:
		SaveResult.save_result('个人资料','货主','fail')

if __name__=='__main__':
	MyInfo()