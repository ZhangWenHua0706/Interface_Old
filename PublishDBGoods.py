# -*- coding:utf-8 -*-
import requests
import configparser
import time,json
import SaveResult

def HttpGet():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding='utf-8-sig')
	urlstring=cf.get('PublishDBGoods','url')
	requesttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	loadTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	sendTime=time.time()
	cardict={'boxType':'XS','models':'4.8'}
	dic={'requestEntity':{'added_service':(cf.get('PublishDBGoods','added_service'),),'arrivalTime':cf.get('PublishDBGoods','arrivalTime'),
	'arrivalsName':cf.get('PublishDBGoods','arrivalsName'),'cars':(cardict,),
	'contactsName':cf.get('PublishDBGoods','contactsName'),'contactsPhone':cf.get('PublishDBGoods','contactsPhone'),
	'createDeptName':cf.get('PublishDBGoods','createDeptName'),'declaredValue':cf.get('PublishDBGoods','declaredValue'),
	'departureName':cf.get('PublishDBGoods','departureName'),'dimensional':cf.get('PublishDBGoods','dimensional'),
	'failuretime':cf.get('PublishDBGoods','failuretime'),
	'goodsName':cf.get('PublishDBGoods','goodsName'),'needQuantity':cf.get('PublishDBGoods','needQuantity'),
	'orderCode':cf.get('PublishDBGoods','orderCode'),'packagie':cf.get('PublishDBGoods','packagie'),
	'priceofgoods':cf.get('PublishDBGoods','priceofgoods'),'productType':cf.get('PublishDBGoods','productType'),
	'quantity':cf.get('PublishDBGoods','quantity'),'remarks':cf.get('PublishDBGoods','remarks'),
	'transportPropert':cf.get('PublishDBGoods','transportPropert'),'unifiedCode':cf.get('PublishDBGoods','unifiedCode'),
	'useCarTime':cf.get('PublishDBGoods','useCarTime'),'weight':cf.get('PublishDBGoods','weight')},'type':cf.get('PublishDBGoods','type')}
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	dheaders={'User-Agent':user_agent}
	dicc=json.dumps(dic,ensure_ascii=False)
	response= requests.post(url=urlstring,data=dicc.encode('utf-8'),headers=dheaders) 
	return response
def PublishDBGoods():
	resultstr=HttpGet()
	if '"responseType":"1"' in resultstr.text:
		SaveResult.save_result('发货'.decode('utf-8'),'德邦'.decode('utf-8'),'pass')
	else:
		SaveResult.save_result('发货'.decode('utf-8'),'德邦'.decode('utf-8'),'fail')

if __name__=='__main__':
	PublishDBGoods()
	print ('OK!!!')