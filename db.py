#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import sqlite3
import globeCtrl
import binascii 
from Crypto.Hash import MD5,SHA
from Crypto.Cipher import AES

PADDING = '\0' 

def padIt(inStr):
	retStr=""
	for i in xrange(32):
		if(i<len(inStr)):
			retStr+=inStr[i]
		else:
			retStr+='\0'
	return retStr

def AES_Encode(str_key,str_inputText):
	obj = AES.new(self.key, AES.MODE_ECB)     
	crypt = obj.encrypt(inputText)
	print crypt
	return crypt
	
def AES_Decode(str_key,str_inputText):
	inputText=binascii.a2b_hex(inputText)
	obj = AES.new(self.key, AES.MODE_ECB)     
	crypt = obj.decrypt(inputText)
	tempStr=''
	for item in crypt:
		if(item!='\0'): tempStr += str(item)
	print tempStr
	return tempStr

class dbCtrl:
	def __init__(self):
		self.dbFile="./pwd.db"
		self.key=None
		if(globeCtrl.gCtrl.usrEncodePwd!=None):
			self.key=padIt(globeCtrl.gCtrl.usrEncodePwd)
		
		
	def dbGetSuperPwd(self):
		db=sqlite3.connect(self.dbFile)
		cur=db.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS usr\
					(\
						pwd TEXT NOT NULL\
					)")
		cur.execute("SELECT * from usr")
		resList=cur.fetchone()
		db.close()
		#print(resList)
		if(resList==None): return None
		else: return resList[0]
	
	def dbSetSuperPwd(self,str_pwd):
		db=sqlite3.connect(self.dbFile)
		cur=db.cursor()
		encodePwd = MD5.new()
		encodePwd.update(str_pwd)
		try:
			#print("INSERT INTO usr (pwd) VALUES (\""+encodePwd.hexdigest()+"\")")
			cur.execute("INSERT INTO usr (pwd) VALUES (\""+encodePwd.hexdigest()+"\")")
			db.commit() 
		except:
			print("ERROR")

		db.close()
	
	def dbCheckSuperPwd(self,str_pwd):
		encodePwd = MD5.new()
		encodePwd.update(str_pwd)
		encodePwd=encodePwd.hexdigest()
		if(self.dbGetSuperPwd()==encodePwd):
			returnCode = SHA.new()
			returnCode.update(str_pwd)
			return returnCode.hexdigest()
		else: return None
		
	def dbInitMainTable(self):
		db=sqlite3.connect(self.dbFile)
		cur=db.cursor()
		
		try:
			cur.execute("CREATE TABLE IF NOT EXISTS mainPwd\
						(\
							pwdName TEXE UNIQUE NOT NULL,\
							pwd TEXT NOT NULL\
						)")
		except:
			print("InitMainTable Error")
		
		db.close()
	def dbInsertIntoMainTable(self,str_name,str_pwd):
		db=sqlite3.connect(self.dbFile)
		cur=db.cursor()
		
		str_pwd=padIt(str_pwd)
		obj = AES.new(self.key, AES.MODE_ECB)     
		crypt = obj.encrypt(str_pwd)
		print binascii.b2a_hex(crypt)
		try:
			cur.execute("INSERT INTO mainPwd (pwdName,pwd) VALUES\
							(\""+str_name+"\",\""+binascii.b2a_hex(crypt)+"\")")
			db.commit() 
		except:
			print("InsertIntoMainTable Error")
		
		db.close()
	
	def dbGetMainTableName(self):
		db=sqlite3.connect(self.dbFile)
		cur=db.cursor()
		
		try:
			cur.execute("SELECT pwdName FROM mainPwd")
			resList=cur.fetchall()
			print resList
			db.close()
			return resList
		except:
			print("GetMainTableName ERROR")
			db.close()
			return None
			
	def dbGetPwd(self,str_name):
		db=sqlite3.connect(self.dbFile)
		cur=db.cursor()
		
		try:
			cur.execute("SELECT * FROM mainPwd where pwdName==\""+str_name+"\"")
			resList=cur.fetchone()
			db.close()
			inputText=binascii.a2b_hex(resList[1])
			obj = AES.new(self.key, AES.MODE_ECB)     
			crypt = obj.decrypt(inputText)
			pwd=''
			for item in crypt:
				if(item!='\0'): pwd += str(item)
			return pwd
		except:
			print("GetPwd ERROR")
			db.close()
			return None
	
	def dbDelPwd(self,str_name):
		db=sqlite3.connect(self.dbFile)
		cur=db.cursor()
		
		try:
			print("DELETE FROM mainPwd where pwdName==\""+str_name+"\"")
			cur.execute("DELETE FROM mainPwd where pwdName==\""+str_name+"\"")
			db.commit()
		except:
			print("DelPwd Error")
		
		db.close()
		
	def dpUpdatePwd(self,str_name,str_pwd):
		db=sqlite3.connect(self.dbFile)
		cur=db.cursor()
		str_pwd=padIt(str_pwd)
		obj = AES.new(self.key, AES.MODE_ECB)     
		crypt = obj.encrypt(str_pwd)
		try:
			cur.execute("UPDATE mainPwd \
							SET pwd=\""+binascii.b2a_hex(crypt)+"\" where pwdName==\""+str_name+"\"")
			db.commit()
		except:
			print("UpdatePwd Error")
		
		db.close()

