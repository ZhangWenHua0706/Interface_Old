# -*- coding:utf-8 -*-
import base64
from Crypto.Cipher import AES

BS=AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]
class MyCrypt():
	def __init__(self):
		self.key = '884b2fbc1397c37a4f6fe951aa19679d'
#		self.mode = AES.MODE_CBC

	def encrypt(self, text):
		cryptor = AES.new(self.key)
		self.ciphertext = cryptor.encrypt(pad(text))
		self.result = base64.b64encode(self.ciphertext)
		return self.result

	def decrypt(self, text):
		cryptor = AES.new(self.key)
		rbase64=base64.b64decode(text)
		self.plain_text = unpad(cryptor.decrypt(rbase64).decode('utf-8'))
		return self.plain_text

if __name__ == '__main__':
	data = "linan@0256"
	ec = MyCrypt()
	encrpt_data = ec.encrypt(data)
	decrpt_data = ec.decrypt(encrpt_data)
	b64encrpt_data=base64.b64encode(encrpt_data)
	print (encrpt_data.decode('utf-8'),decrpt_data)