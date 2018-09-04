# -*- coding:utf-8 -*-
import urllib.request,urllib.parse
import configparser
import time
import SaveResult
import GetSmsCode,CheckMobile,SendRegMsg,SendRegVoice
import DBConn

def httpPostOwner(account):
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('Reg','url')
	mobile3=str(account)
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
	
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	return the_page
def regMuti(num):
	mobile=19700000200
	end_mobile=mobile+num
	while mobile<end_mobile:
		httpPostOwner(mobile)
		mobile=mobile+1
if __name__=='__main__':
	regMuti(1000)
	