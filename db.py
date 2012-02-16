#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import sqlite3
import globeCtrl
from Crypto.Hash import MD5,SHA
from Crypto.Cipher import AES

PADDING = '\0' 
padIt = lambda s: s+(16 - len(s)%16)*PADDING 

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
		try:
			cur.execute("INSERT INTO mainPwd (pwdName,pwd) VALUES\
							(\""+str_name+"\",\""+str_pwd+"\")")
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
			retStr=AES_Decode(resList[1],globeCtrl.gCtrl.usrEncodePwd)
			print retStr
			return retStr
		except:
			print("GetPwd ERROR")
			db.close()
			return None
		

