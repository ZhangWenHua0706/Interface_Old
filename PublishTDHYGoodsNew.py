# -*- coding:utf-8 -*-
import requests
import configparser
import time
import SaveResult

def HttpGet():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	url=cf.get('PublishTDHYGoods','url')
	requesttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	loadTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	sendTime=time.time()
	dicc={'billnumber':cf.get('PublishTDHYGoods','billnumber'),'remark':cf.get('PublishTDHYGoods','remark'),
	'startAddress':cf.get('PublishTDHYGoods','startAddress'),'orderType':cf.get('PublishTDHYGoods','orderType'),
	'endAddress':cf.get('PublishTDHYGoods','endAddress'),'goodsName':cf.get('PublishTDHYGoods','goodsName'),
	'needBack':cf.get('PublishTDHYGoods','needBack'),'startAddressDetail':cf.get('PublishTDHYGoods','startAddressDetail'),
	'endAddressDetail':cf.get('PublishTDHYGoods','endAddressDetail'),'goodsWeight':cf.get('PublishTDHYGoods','goodsWeight'),
	'goodsVolume':cf.get('PublishTDHYGoods','goodsVolume'),'deliveryTime':'1478919669000',
	'expectCarType':cf.get('PublishTDHYGoods','expectCarType'),'expectCarLength':cf.get('PublishTDHYGoods','expectCarLength'),
	'startContactName':cf.get('PublishTDHYGoods','startContactName'),'startContactPhone':cf.get('PublishTDHYGoods','startContactPhone'),
	'endContactName':cf.get('PublishTDHYGoods','endContactName'),'endContactPhone':cf.get('PublishTDHYGoods','endContactPhone'),
	'needInvoice':cf.get('PublishTDHYGoods','needInvoice'),'loadTime':loadTime,'sendTime':sendTime}
	pdata={'apikey':'LINAN','requestid':'9081dfd6d25949c6be1732ccff5b81c7','requesttime':requesttime,
	'data'=dicc,'sign':'2578fac328e1c273235053a0931b436e'}
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	response= requests.post(url,data=pdata,headers=headers) 
	return response.text
def PublishTDHYGoods():
	resultstr=HttpGet()
	if 'isok' in resultstr:
		SaveResult.save_result('货主货源','TDHY发货成功','pass')
	else:
		SaveResult.save_result('货主货源','TDHY发货成功','fail')

if __name__=='__main__':
	PublishTDHYGoods()
	print ("OVER!!!")