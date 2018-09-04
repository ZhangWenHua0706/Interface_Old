import configparser
import pymysql
def GetConnection(sqlscript):
	cf=configparser.ConfigParser()
	cf.read('config.ini',encoding="utf-8-sig")
	host=cf.get('MySqlDB','host')
	user=cf.get('MySqlDB','user')
	password=cf.get('MySqlDB','password')
	port=cf.get('MySqlDB','port')
	db=cf.get('MySqlDB','dbname')
	Conn = pymysql.connect(host=host,user=user,passwd=password,port=int(port),db=db)
	cur=Conn.cursor()
	cur.execute(sqlscript)
	print (1)
	for r in cur.fetchall():
		pass
	cur.close()
	Conn.close()
	return r[0]
if __name__=='__main__':
	GetConnection('SELECT verification_code from sms_sms where mobile=19211223344 and valid=1 and source_id=1')