# -*- coding:utf-8 -*-
import xlrd,xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import configparser
import time
def save_result(module_name,feature,result): 
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	dirhome=cf.get('TestResult','dirhome')
	filename=dirhome+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.xlsx'
	rb=open_workbook(filename)
	sheet1=rb.sheets()[0]
	wb=copy(rb)
	ws=wb.get_sheet(0)
	ws.write(sheet1.nrows,0,module_name)
	ws.write(sheet1.nrows,1,feature)
	ws.write(sheet1.nrows,2,result)
	wb.save(filename)
if __name__=='__main__':
	save_result('发货'.decode('utf-8'),'tt','pass')
