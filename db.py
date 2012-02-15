#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import sqlite3
from Crypto.Hash import MD5
from Crypto.Cipher import AES

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

