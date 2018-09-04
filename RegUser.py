import urllib.request,urllib.parse
import configparser
import time
import SaveResult
import GetSmsCode,CheckMobile,SendRegMsg,SendRegVoice
import DBConn

def httpPostDriver():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('Reg','url')
	mobile1=cf.get('Reg','mobile1')
	password=cf.get('Reg','password')
	CheckMobile.CheckMobile(mobile1)
	SendRegMsg.SendRegMsg(mobile1)
	SendRegVoice.SendRegVoice(mobile1)
	sqlscript='SELECT verification_code from sms_sms where mobile='+ mobile1+' and valid=1 and source_id=1'
	smscode=DBConn.GetConnection(sqlscript)
	customerRoleId=1
	customerType=1
	registeSource=1
	values={'mobile':mobile1,'customerPwd':password,'customerRoleId':customerRoleId,'customerType':customerType,'registeSource':registeSource,'smsCode':smscode}
	pdata=urllib.parse.urlencode(values)
	
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page
def httpPostAgent():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('Reg','url')
	mobile2=cf.get('Reg','mobile2')
	password=cf.get('Reg','password')
	CheckMobile.CheckMobile(mobile2)
	SendRegMsg.SendRegMsg(mobile2)
	SendRegVoice.SendRegVoice(mobile2)
	sqlscript='SELECT verification_code from sms_sms where mobile='+ mobile2+' and valid=1 and source_id=1'
	smscode=DBConn.GetConnection(sqlscript)
	customerRoleId=2
	customerType=2
	registeSource=1
	values={'mobile':mobile2,'customerPwd':password,'customerRoleId':customerRoleId,'customerType':customerType,'registeSource':registeSource,'smsCode':smscode}
	pdata=urllib.parse.urlencode(values)
	
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page
def httpPostOwner():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('Reg','url')
	mobile3=cf.get('Reg','mobile3')
	password=cf.get('Reg','password')
	CheckMobile.CheckMobile(mobile3)
	SendRegMsg.SendRegMsg(mobile3)
	SendRegVoice.SendRegVoice(mobile3)
	sqlscript='SELECT verification_code from sms_sms where mobile='+ mobile3+' and valid=1 and source_id=1'
	smscode=DBConn.GetConnection(sqlscript)
	customerRoleId=3
	customerType=2
	registeSource=1
	values={'mobile':mobile3,'customerPwd':password,'customerRoleId':customerRoleId,'customerType':customerType,'registeSource':registeSource,'smsCode':smscode}
	pdata=urllib.parse.urlencode(values)
	
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page
def RegUser():
	resultstr1=httpPostDriver().decode()
	if '2000000' in resultstr1:
		SaveResult.save_result('用户注册','注册司机','pass')
	else:
		SaveResult.save_result('用户注册','注册司机','fail')
	resultstr2=httpPostAgent().decode()
	if '2000000' in resultstr2:
		SaveResult.save_result('用户注册','注册经纪人','pass')
	else:
		SaveResult.save_result('用户注册','注册经纪人','fail')
	resultstr3=httpPostOwner().decode()
	if '2000000' in resultstr3:
		SaveResult.save_result('用户注册','注册货主','pass')
	else:
		SaveResult.save_result('用户注册','注册货主','fail')
	
if __name__=='__main__':
	httpPostOwner()
	