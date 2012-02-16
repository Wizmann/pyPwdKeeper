#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import pygtk 
import gtk
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
		self.mainWindow.set_default_size(420, 300) 
		self.mainWindow.show()
	
	def gtk_main_quit(self, widget, data=None):
		gtk.main_quit()
