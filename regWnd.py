#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import pygtk 
import gtk
from db import dbCtrl

pygtk.require('2.0') 

class regWnd:
	def __init__(self): 
		self.gladeFile="src_Wnd.glade"
		self.gladeMain = gtk.Builder() 
		self.gladeMain.add_from_file(self.gladeFile) 
		self.gladeMain.connect_signals(self)
		self.mainWindow = self.gladeMain.get_object("registerWnd")
		self.mainWindow.set_position(gtk.WIN_POS_CENTER_ALWAYS) 
		self.mainWindow.set_default_size(420, 300) 
		self.mainWindow.show()
		self.pwdEntryA=None
		self.pwdEntryB=None
		
	def gtk_main_quit(self, widget, data=None):
		gtk.main_quit()
		
	def on_cmdQuit_clicked(self, *args): 
		 print "on_cmdCancel_clicked" 
		 gtk.main_quit() 

	def getPwdEntry(self):#获取窗口密码框的文字
		self.pwdEntryA=self.gladeMain.get_object('pwdEntryA').get_text()
		self.pwdEntryB=self.gladeMain.get_object('pwdEntryB').get_text()
		#print self.pwdEntryA
		#print self.pwdEntryB
		
	def on_cmdOK_clicked(self, *args): 
		self.getPwdEntry()
		if(len(self.pwdEntryA)>=8 and len(self.pwdEntryA)<=16 and
				len(self.pwdEntryB)>=8 and len(self.pwdEntryB)<=16):
			if(self.pwdEntryA != self.pwdEntryB):
				errorMsgBox=gtk.MessageDialog(None,gtk.DIALOG_MODAL,
											gtk.MESSAGE_ERROR,gtk.BUTTONS_OK,
											u'错误')
				errorMsgBox.format_secondary_text(u'两次输入的密码不一致')
				errorMsgBox.run()
				errorMsgBox.destroy()
			else:
				db=dbCtrl()
				db.dbSetSuperPwd(self.pwdEntryA)
		else:
			errorMsgBox=gtk.MessageDialog(None, gtk.DIALOG_MODAL,
										gtk.MESSAGE_ERROR, gtk.BUTTONS_OK,
										u'错误')
			errorMsgBox.format_secondary_text(u"密码长度错误！")
			errorMsgBox.run()
			errorMsgBox.destroy()
	def main(self): 
		gtk.main() 
