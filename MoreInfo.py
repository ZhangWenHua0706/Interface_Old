# -*- coding:utf-8 -*-
import requests
import configparser
import SaveResult,UploadPic,Login,VerifyIdcard
def PostDriverInfo():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('MoreInfo','driver_url')
	headPortrait=cf.get('MoreInfo','headPortrait')
	idcardPositive=cf.get('MoreInfo','idcardPositive')
	idcardNuber=cf.get('MoreInfo','idcardNumber1')
	idcardName=cf.get('MoreInfo','idcardName1')
	vehicleLicense=cf.get('MoreInfo','vehicleLicense')
	vhicleType=cf.get('MoreInfo','vhicleType')
	vehicleLong=cf.get('MoreInfo','vehicleLong')
	vehiclePhoto=cf.get('MoreInfo','vehiclePhoto')
	drivingLicense=cf.get('MoreInfo','drivingLicense')
	mainLine=cf.get('MoreInfo','mainLine')
	goodsType=cf.get('MoreInfo','goodsType')
	reponsestring=eval(Login.HttpLoginDriver())
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	data={'headPortrait':headPortrait,'idcardPositive':idcardPositive,'idcardNuber':idcardNuber,'idcardName':idcardName,'vehicleLicense':vehicleLicense,
	'vhicleType':vhicleType,'vehicleLong':vehicleLong,'vehiclePhoto':vehiclePhoto,'drivingLicense':drivingLicense,'mainLine':mainLine,'goodsType':goodsType}
	VerifyIdcard.VerifyIdcardDriver(idcardNuber,idcardName)
	UploadPic.UploadPic()
	response=requests.post(urlstring,data=data,headers=headers)
	return response.text
def PostAgentInfo():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('MoreInfo','agent_url')
	headPortrait=cf.get('MoreInfo','headPortrait')
	idcardPositive=cf.get('MoreInfo','idcardPositive')
	idcardNuber=cf.get('MoreInfo','idcardNumber2')
	idcardName=cf.get('MoreInfo','idcardName2')
	reponsestring=eval(Login.HttpLoginAgent())
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	data={'headPortrait':headPortrait,'idcardPositive':idcardPositive,'idcardNuber':idcardNuber,'idcardName':idcardName}
	VerifyIdcard.VerifyIdcardAgent(idcardNuber,idcardName)
	UploadPic.UploadPic()
	response=requests.post(urlstring,data=data,headers=headers)
	return response.text
def PostOwnerInfo():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	urlstring=cf.get('MoreInfo','owner_url')
	headPortrait=cf.get('MoreInfo','headPortrait')
	idcardPositive=cf.get('MoreInfo','idcardPositive')
	idcardNuber=cf.get('MoreInfo','idcardNumber3')
	idcardName=cf.get('MoreInfo','idcardName3')
	reponsestring=eval(Login.HttpLoginOwner())
	sessionId=reponsestring['data']['customerInfo']['sessionId']
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent,'sessionId':sessionId}
	data={'headPortrait':headPortrait,'idcardPositive':idcardPositive,'idcardNuber':idcardNuber,'idcardName':idcardName}
	VerifyIdcard.VerifyIdcardOwner(idcardNuber,idcardName)
	UploadPic.UploadPic()
	response=requests.post(urlstring,data=data,headers=headers)
	return response.text	
def MoreInfo():
	resultstr1=PostDriverInfo()
	if '2000000' in resultstr1:
		SaveResult.save_result('完善资料','司机','pass')
	else:
		SaveResult.save_result('完善资料','司机','fail')
	resultstr2=PostAgentInfo()
	if '2000000' in resultstr2:
		SaveResult.save_result('完善资料','经纪人','pass')
	else:
		SaveResult.save_result('完善资料','经纪人','fail')
	resultstr3=PostOwnerInfo()
	if '2000000' in resultstr3:
		SaveResult.save_result('完善资料','货主','pass')
	else:
		SaveResult.save_result('完善资料','货主','fail')
if __name__=='__main__':
	MoreInfo()