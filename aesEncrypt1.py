#!/usr/bin/python
#coding:utf8
#file:aesEncrypt.py
'''
@author:sir
@date:20170216
实现aes加密，base_64编码
'''

from Crypto.Cipher import AES
import os
import base64

class aesencrypty():
	def  __init__(self,key):
		self.BS=AES.block_size
		#加密
		self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
		#解密
		self.unpad = lambda s : s[0:-ord(s[-1])]
		#秘钥
		self.key=key
		#创建一个AES对象
		self.cryptor = AES.new(key)

	#加密方法
	def encrypt(self,text):
		#AES加密
		encrypted = self.cryptor.encrypt(self.pad(text))
		#base_64编码
		result = base64.b64encode(encrypted)
		return result

	#解密方法
	def decrypt(self,text):
		#base_64解码
		reBase_64=base64.b64decode(text)
		#AES解密
		result=self.unpad(self.cryptor.decrypt(reBase_64))
		return result

if __name__ == "__main__":
	key='884b2fbc1397c37a4f6fe951aa19679d'
	text="13026289914"
	ac=aesencrypty(key)
	encrypted_result=ac.encrypt(text)
	decrypted_result=ac.decrypt(encrypted_result)
	print (AES.block_size)
	print (encrypted_result,decrypted_result)

