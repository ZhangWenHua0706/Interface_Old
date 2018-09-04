# -*- coding:utf-8 -*-
import xlrd,xlwt
import time
import configparser,sys


def set_style(name,height,bold=False):
	style = xlwt.XFStyle() # 初始化样式
	font = xlwt.Font() # 为样式创建字体
	font.name = name # 'Times New Roman'
	font.bold = bold
	font.colour_index = 0 # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta
	font.height = height
	style.font = font
	return style
	 
#写excel
def create_excel():
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	dirhome=cf.get('TestResult','dirhome')
	result_file=dirhome+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.xlsx'
	print (result_file)
	f = xlwt.Workbook() #创建工作簿
	sheet1 = f.add_sheet('sheet1',cell_overwrite_ok=True) #创建sheet
	row0 = ['模块'.decode('utf-8'),'功能'.decode('utf-8'),'结果'.decode('utf-8')]
	for i in range(0,len(row0)):
		sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
	f.save(result_file)
if __name__=='__main__':
	create_excel()