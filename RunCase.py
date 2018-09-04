import CrateResultFile,RegUser,MoreInfo,GetLatest,getFindPictureList,MyInfo,IndexInfo,AreaCodeInfo,AddLocation




if __name__=='__main__':
	CrateResultFile.create_excel()                              #创建测试结果文件
	RegUser.RegUser()                                           #注册用户
	GetLatest.getLatestVersion()								#升级接口
	getFindPictureList.getADPictures()							#banner广告接口
	MyInfo.MyInfo()												#个人资料
	IndexInfo.IndexInfo()										#首页文字广告
	AreaCodeInfo.AreaCodeInfo()									#行政区接口
	AddLocation.AddLocation()									#上报定位
	MoreInfo.MoreInfo()											#完善资料
