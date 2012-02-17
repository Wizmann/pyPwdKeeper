#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import pygtk 
import gtk
import globeCtrl
from random import randint
from db import dbCtrl

def pwgen():
	pwd=""
	for i in xrange(16):
		t=0
		while(not ( (t>=48 and t<=57) or (t>=65 and t<=90) or (t>=97 and t<=122) ) ):
			t=randint(48,122)
		
		pwd+=chr(t)
	return pwd
	
class inputWnd:
	def __init__(self,str_name=None): 
		self.gladeFile="src_Wnd.glade"
		self.gladeMain = gtk.Builder() 
		self.gladeMain.add_from_file(self.gladeFile) 
		self.gladeMain.connect_signals(self)
		
		self.mainWindow = self.gladeMain.get_object("inputWnd")
		self.mainWindow.set_position(gtk.WIN_POS_CENTER_ALWAYS) 
		self.mainWindow.set_default_size(400,250) 
		self.mainWindow.show()
		
		self.entryName=str_name
		self.entryPwd=None
		self.newEntry=True
		if(str_name!=None):
			self.newEntry=False
			self.gladeMain.get_object('inputEntryName').editable=False
			db=dbCtrl()
			self.entryPwd=db.dbGetPwd(str_name)
			if(self.entryPwd==None):
				print("GetPwd returns a None")
		self.refresh(self.entryName,self.entryPwd)
		self.regenPwd()
	
	def refresh(self,str_name,str_pwd):
		str_name = "" if str_name==None else str_name
		str_pwd = "" if str_pwd==None else str_pwd
		self.gladeMain.get_object('inputEntryName').set_text(str_name)
		self.gladeMain.get_object('inputEntryPwd').set_text(str_pwd)
	
	def regenPwd(self):
		str_genPwd=pwgen()
		self.gladeMain.get_object('inputEntryPwd').set_text(str_genPwd)
		
	def main(self,str_name=None):
		gtk.main()
		
	def gtk_main_quit(self, widget, data=None):
		gtk.main_quit()
		
	def on_inputQuit_clicked(self,*args):
		gtk.Widget.destroy(self.mainWindow)
		
	def on_inputGen_clicked(self,*args):
		self.regenPwd()
		
	def on_inputOK_clicked(self,*args):
		str_name=self.gladeMain.get_object('inputEntryName').get_text()
		str_pwd=self.gladeMain.get_object('inputEntryPwd').get_text()
		
		if(str_name==''):
			errorMsgBox=gtk.MessageDialog(None,gtk.DIALOG_MODAL,
											gtk.MESSAGE_ERROR,gtk.BUTTONS_OK,
											u'错误')
			errorMsgBox.format_secondary_text(u'条目不能为空')
			errorMsgBox.run()
			errorMsgBox.destroy()
			return None
		
		db=dbCtrl()
		if(self.newEntry==True):
			db.dbInsertIntoMainTable(str_name,str_pwd)
		else:
			db.dbUpdateIntoMainTalbe(str_name,str_pwd)
		
		gtk.Widget.destroy(self.mainWindow)
			
