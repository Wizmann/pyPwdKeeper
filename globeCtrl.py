import sys

class globeCtrl:
	def __init__(self):
		self.loginSuccess=False
		self.usrEncodePwd=None
		#Using SHA1 to encode our pwd with AES
		self.quit=False
		
	def setLogin(self,bool_res):
		self.loginSuccess=bool_res
	
	def setUsrEncodePwd(self,str_enPwd):
		self.usrEncodePwd=str_enPwd
		
	def setQuit(self,bool_res):
		self.quit=bool_res

#Using as globe Variable
gCtrl=globeCtrl()
