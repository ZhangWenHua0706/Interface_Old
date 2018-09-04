# -*- coding:utf-8 -*-
import AESEncrypt
import requests
import configparser
import SaveResult

class RobotLogin():
    def __init__(self):
        pass
    def HttpLoginDriver(self):
        cf=configparser.ConfigParser()
        cf.read('D:\Python27\interface\config.ini',encoding="utf-8-sig")
        urlstring=cf.get('login','url')
        mobile1=cf.get('login','mobile1')
        password=cf.get('login','password')
        usertype=1
        mobile=AESEncrypt.MyCrypt().encrypt(mobile1).decode('utf-8')
        customerPwd=AESEncrypt.MyCrypt().encrypt(password).decode('utf-8')
        values={'mobile':mobile,'customerPwd':customerPwd,'type':usertype}
        #user_agent='Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'
        user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
        headers={'User-Agent':user_agent}
        response=requests.post(url=urlstring,data=values,headers=headers)
        return response.text

    def LoginUser(self):
        resultstr1=self.HttpLoginDriver()
        if '2000000' in resultstr1:
            SaveResult.save_result('用户登录'.decode('utf-8'),'登录司机'.decode('utf-8'),'pass')
        else:
            SaveResult.save_result('用户登录'.decode('utf-8'),'登录司机'.decode('utf-8'),'fail')

if __name__=='__main__':
    rl=RobotLogin()
    rl.LoginUser()