import urllib.request,urllib.parse
import configparser
import SaveResult,Login,DBConn
def HttpAreaCodeInfo():            #获取行政区开关
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('AreaCodeInfo','url')
	responsestring=eval(Login.HttpLoginDriver())
	pdata=''
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	sessionId=responsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page.decode('utf-8')
def AreaCodeInfo():
	resultstr=HttpAreaCodeInfo()
	if '2000000' in resultstr:
		SaveResult.save_result('行政区接口','查询','pass')
	else:
		SaveResult.save_result('行政区接口','查询','fail')
if __name__=='__main__':
	AreaCodeInfo()