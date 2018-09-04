# -*- coding:utf-8 -*-
import urllib.request,urllib.parse
import configparser
import time
import SaveResult

def HttpGet():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('PublishTDHYOrder','url')
	requesttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	loadTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	sendTime=time.time()
	dict={'apikey':'LINAN','requestid':'9081dfd6d25949c6be1732ccff5b81c7','requesttime':requesttime,
	'data':{'orderId':cf.get('PublishTDHYOrder','orderId'),'priceId':cf.get('PublishTDHYOrder','priceId'),
	'startContactName':cf.get('PublishTDHYOrder','startContactName'),'startContactPhone':cf.get('PublishTDHYOrder','startContactPhone'),
	'endContactName':cf.get('PublishTDHYOrder','endContactName'),'endContactPhone':cf.get('PublishTDHYOrder','endContactPhone'),
	'startAddressDetail':cf.get('PublishTDHYOrder','startAddressDetail'),'endAddressDetail':cf.get('PublishTDHYOrder','endAddressDetail')},
	'sign':'2578fac328e1c273235053a0931b436e'}
	pdata=urllib.parse.urlencode(dict)
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	dheaders={'User-Agent':user_agent}
	
	req= urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=dheaders) 
	response = urllib.request.urlopen(req)
	the_page = response.read()
	return the_page
def PublishTDHYOrder():
	resultstr=HttpGet().decode()
	if 'isok' in resultstr:
		SaveResult.save_result('金牌货主订单','天地华宇中标','pass')
	else:
		SaveResult.save_result('金牌货主订单','天地华宇中标','fail')

if __name__=='__main__':
	PublishTDHYOrder()
	print ("OVER!!!")