import requests
import configparser
import SaveResult,Login
cf=configparser.ConfigParser()
cf.read('config.ini',encoding="utf-8-sig")
def httpPostDriver(idcardnumber,idcardname):
	urlstring=cf.get('VerifyIdcard','url')
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	reponsestring=eval(Login.HttpLoginDriver())
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	idcardnumber=idcardnumber
	idcardname=idcardname
	data={'idcardName':idcardname,'idcardNumber':idcardnumber}
	response=requests.post(urlstring,data=data,headers=headers)
	return response.text
def httpPostAgent(idcardnumber,idcardname):
	urlstring=cf.get('VerifyIdcard','url')
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	reponsestring=eval(Login.HttpLoginAgent())
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	idcardnumber=idcardnumber
	idcardname=idcardname
	data={'idcardName':idcardname,'idcardNumber':idcardnumber}
	response=requests.post(urlstring,data=data,headers=headers)
	return response.text
def httpPostOwner(idcardnumber,idcardname):
	urlstring=cf.get('VerifyIdcard','url')
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	reponsestring=eval(Login.HttpLoginOwner())
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	idcardnumber=idcardnumber
	idcardname=idcardname
	data={'idcardName':idcardname,'idcardNumber':idcardnumber}
	response=requests.post(urlstring,data=data,headers=headers)
	return response.text
def VerifyIdcardDriver(idcardnumber,idcardname):
	resultstr=httpPostDriver(idcardnumber,idcardname)
	if '2000000' in resultstr:
		SaveResult.save_result('完善资料','身份验证司机','pass')
	else:
		SaveResult.save_result('完善资料','身份验证司机','fail')
def VerifyIdcardAgent(idcardnumber,idcardname):
	resultstr=httpPostAgent(idcardnumber,idcardname)
	if '2000000' in resultstr:
		SaveResult.save_result('完善资料','身份验证经纪人','pass')
	else:
		SaveResult.save_result('完善资料','身份验证经纪人','fail')
def VerifyIdcardOwner(idcardnumber,idcardname):
	resultstr=httpPostOwner(idcardnumber,idcardname)
	if '2000000' in resultstr:
		SaveResult.save_result('完善资料','身份验证货主','pass')
	else:
		SaveResult.save_result('完善资料','身份验证货主','fail')
if __name__=='__main__':
	VerifyIdcardDriver(cf.get('MoreInfo','idcardNumber1'),cf.get('MoreInfo','idcardName1'))
	VerifyIdcardAgent(cf.get('MoreInfo','idcardNumber2'),cf.get('MoreInfo','idcardName2'))
	VerifyIdcardOwner(cf.get('MoreInfo','idcardNumber3'),cf.get('MoreInfo','idcardName3'))