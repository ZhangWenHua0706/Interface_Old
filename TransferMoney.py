# -*- coding:utf-8 -*-
import requests
import configparser
import Login
def TransferMoney():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('TransferMoney','url')
	mobile=19922220002
	tradingAmount=1
	transferType=0
	reponsestring=eval(Login.HttpLoginAgent())
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	data={'mobile':mobile,'tradingAmount':tradingAmount,'transferType':transferType}
	response=requests.post(urlstring,data=data,headers=headers)


if __name__=='__main__':
	i=0
	while i<1000:
		TransferMoney()
		i=i+1