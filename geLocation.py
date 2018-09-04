import urllib.request,urllib.parse
import configparser
import time
import SaveResult
def getLocation():
	urlstring="http://localhost/cmd.svc/Api/Vehicle/ApiVehicleManager/QuerySingleLastPosition"
	values="{\"PlateNo\":\"冀JV1082\"}"
	pdata=urllib.parse.urlencode(values)
	#user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	req=urllib.request.Request(url=urlstring,data=pdata.encode("UTF-8"),headers=headers)
	response = urllib.request.urlopen(req) 
	the_page = response.read()
	print (the_page)


if __name__=='__main__':
	getLocation()