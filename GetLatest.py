import AESEncrypt
import urllib.request,urllib.parse
import configparser
import SaveResult,Login,DBConn
def HttpGetLatestADDriver():  #安卓司机升级接口请求
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getLatest','url')
	device=cf.get('getLatest','device1')
	versionType=cf.get('getLatest','versiontype1')
	sqlscript='SELECT version from app_version where device='+device+' and version_type='+versionType
	current=DBConn.GetConnection(sqlscript)
	reponsestring=eval(Login.HttpLoginDriver())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'device':device,'versionType':versionType,'current':current,'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetLatestADAgent():  #安卓经纪人升级接口请求
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getLatest','url')
	device=cf.get('getLatest','device1')
	versionType=cf.get('getLatest','versiontype2')
	sqlscript='SELECT version from app_version where device='+device+' and version_type='+versionType
	current=DBConn.GetConnection(sqlscript)
	reponsestring=eval(Login.HttpLoginAgent())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'device':device,'versionType':versionType,'current':current,'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetLatestADOwner():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getLatest','url')
	device=cf.get('getLatest','device1')
	versionType=cf.get('getLatest','versiontype3')
	sqlscript='SELECT version from app_version where device='+device+' and version_type='+versionType
	current=DBConn.GetConnection(sqlscript)
	reponsestring=eval(Login.HttpLoginOwner())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'device':device,'versionType':versionType,'current':current,'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetLatestIOSDriver():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getLatest','url')
	device=cf.get('getLatest','device2')
	versionType=cf.get('getLatest','versiontype1')
	sqlscript='SELECT version from app_version where device='+device+' and version_type='+versionType
	current=DBConn.GetConnection(sqlscript)
	reponsestring=eval(Login.HttpLoginDriver())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'device':device,'versionType':versionType,'current':current,'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetLatestIOSAgent():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getLatest','url')
	device=cf.get('getLatest','device2')
	versionType=cf.get('getLatest','versiontype2')
	sqlscript='SELECT version from app_version where device='+device+' and version_type='+versionType
	current=DBConn.GetConnection(sqlscript)
	reponsestring=eval(Login.HttpLoginAgent())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'device':device,'versionType':versionType,'current':current,'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetLatestIOSOwner():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getLatest','url')
	device=cf.get('getLatest','device2')
	versionType=cf.get('getLatest','versiontype3')
	sqlscript='SELECT version from app_version where device='+device+' and version_type='+versionType
	current=DBConn.GetConnection(sqlscript)
	reponsestring=eval(Login.HttpLoginOwner())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'device':device,'versionType':versionType,'current':current,'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetLatestPCAgent():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getLatest','url')
	device=cf.get('getLatest','device3')
	versionType=cf.get('getLatest','versiontype2')
	sqlscript='SELECT version from app_version where device='+device+' and version_type='+versionType
	current=DBConn.GetConnection(sqlscript)
	reponsestring=eval(Login.HttpLoginAgent())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'device':device,'versionType':versionType,'current':current,'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def HttpGetLatestPCOwner():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('getLatest','url')
	device=cf.get('getLatest','device3')
	versionType=cf.get('getLatest','versiontype3')
	sqlscript='SELECT version from app_version where device='+device+' and version_type='+versionType
	current=DBConn.GetConnection(sqlscript)
	reponsestring=eval(Login.HttpLoginOwner())
	customerId=reponsestring['data']['customerInfo']['customerId']

	values={'device':device,'versionType':versionType,'current':current,'customerId':customerId}
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def getLatestVersion():
	resultstr1=HttpGetLatestADDriver()
	if '2000000' in resultstr1:
		SaveResult.save_result('用户升级','升级安卓司机','pass')
	else:
		SaveResult.save_result('用户升级','升级安卓司机','fail')
	resultstr2=HttpGetLatestADAgent()
	if '2000000' in resultstr2:
		SaveResult.save_result('用户升级','升级安卓经纪人','pass')
	else:
		SaveResult.save_result('用户升级','升级安卓经纪人','fail')
	resultstr3=HttpGetLatestADOwner()
	if '2000000' in resultstr3:
		SaveResult.save_result('用户升级','升级安卓货主','pass')
	else:
		SaveResult.save_result('用户升级','升级安卓货主','fail')
	resultstr4=HttpGetLatestIOSDriver()
	if '2000000' in resultstr4:
		SaveResult.save_result('用户升级','升级IOS司机','pass')
	else:
		SaveResult.save_result('用户升级','升级IOS司机','fail')
	resultstr5=HttpGetLatestIOSAgent()
	if '2000000' in resultstr5:
		SaveResult.save_result('用户升级','升级IOS经纪人','pass')
	else:
		SaveResult.save_result('用户升级','升级IOS经纪人','fail')
	resultstr6=HttpGetLatestIOSOwner()
	if '2000000' in resultstr6:
		SaveResult.save_result('用户升级','升级IOS货主','pass')
	else:
		SaveResult.save_result('用户升级','升级IOS货主','fail')
	resultstr7=HttpGetLatestPCAgent()
	if '2000000' in resultstr7:
		SaveResult.save_result('用户升级','升级PC货主','pass')
	else:
		SaveResult.save_result('用户升级','升级PC货主','fail')
	resultstr8=HttpGetLatestPCOwner()
	if '2000000' in resultstr8:
		SaveResult.save_result('用户升级','升级PC货主','pass')
	else:
		SaveResult.save_result('用户升级','升级PC货主','fail')
if __name__=='__main__':
	getLatestVersion()