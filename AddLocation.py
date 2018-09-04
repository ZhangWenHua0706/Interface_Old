import requests,time
import configparser
import SaveResult,Login
def httpPost():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('AddLocation','url')
	latitude=cf.get('AddLocation','latitude')
	address=cf.get('AddLocation','address')
	deviceId=cf.get('AddLocation','deviceId')
	locationTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	longitude=cf.get('AddLocation','longitude')
	deviceVersion=cf.get('AddLocation','deviceVersion')
	version=cf.get('AddLocation','version')
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	reponsestring=eval(Login.HttpLoginDriver())
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	data={'latitude':latitude,'address':address,'deviceId':deviceId,'locationTime':locationTime,'longitude':longitude,'deviceVersion':deviceVersion,'version':version}
	response=requests.post(urlstring,data=data,headers=headers)
	return response.text
def AddLocation():
	resultstr=httpPost()
	if '2000000' in resultstr:
		SaveResult.save_result('上报定位','上报定位','pass')
	else:
		SaveResult.save_result('上报定位','上报定位','fail')
if __name__=='__main__':
	AddLocation()