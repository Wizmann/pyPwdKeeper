#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import pygtk 
import gtk
import globeCtrl
from db import dbCtrl

pygtk.require('2.0') 

class loginWnd:
	def __init__(self): 
		self.gladeFile="src_Wnd.glade"
		self.gladeMain = gtk.Builder() 
		self.gladeMain.add_from_file(self.gladeFile) 
		self.gladeMain.connect_signals(self)
		self.mainWindow = self.gladeMain.get_object("loginWnd")
		self.mainWindow.set_position(gtk.WIN_POS_CENTER_ALWAYS) 
		self.mainWindow.set_default_size(200, 120) 
		self.mainWindow.show()
		self.pwdEntry=None
	
	def gtk_main_quit(self, widget, data=None):
		globeCtrl.gCtrl.setQuit(True)
		gtk.main_quit()
	
	def on_loginWndOK_clicked(self,*args):
		self.pwdEntry=self.gladeMain.get_object('loginPwdEntry').get_text()
		db=dbCtrl()
		ret=db.dbCheckSuperPwd(self.pwdEntry)
		if(ret!=None):
			globeCtrl.gCtrl.setLogin(True)
			globeCtrl.gCtrl.setUsrEncodePwd(ret)
		else:
			errorMsgBox=gtk.MessageDialog(None,gtk.DIALOG_MODAL,
											gtk.MESSAGE_ERROR,gtk.BUTTONS_OK,
											u'错误')
			errorMsgBox.format_secondary_text(u'密码错误')
			errorMsgBox.run()
			errorMsgBox.destroy()
	
	def on_loginWndQuit_clicked(self,*args):
		 gtk.main_quit() 
	
	def main(self): 
		gtk.main() 
