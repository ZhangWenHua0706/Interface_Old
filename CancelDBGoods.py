# -*- coding:utf-8 -*-
import requests
import configparser
import time,json
import SaveResult

def HttpGet():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding='utf-8-sig')
	urlstring=cf.get('CancelDBGoods','url')
	dic={'requestEntity':{
	'orderCode':cf.get('CancelDBGoods','orderCode'),'orderStauts':cf.get('CancelDBGoods','orderStauts'),
	'uniqueId':cf.get('CancelDBGoods','uniqueId')},'type':cf.get('CancelDBGoods','type')}
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	dheaders={'User-Agent':user_agent}
	dicc=json.dumps(dic,ensure_ascii=False)
	response= requests.post(url=urlstring,data=dicc.encode('utf-8'),headers=dheaders) 
	return response
def CancelDBGoods():
	resultstr=HttpGet()
	print (resultstr.text)
	if '"responseType":"1"' in resultstr.text:
		SaveResult.save_result('货主货源','德邦关闭','pass')
	else:
		SaveResult.save_result('货主货源','德邦关闭','fail')

if __name__=='__main__':
	CancelDBGoods()
	print ('OVER!!!')