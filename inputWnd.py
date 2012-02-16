#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import pygtk 
import gtk
import globeCtrl
from random import randint
from db import dbCtrl

def __pwgen():
	str=""
	for i in xrange(16):
		t=0
		while(not (t>=48 and t<=57 and t>=65 and t<=90 and t>=97 and t<=122)):
			t=randint(48,122)
		
		str.append(chr(t))
	
	return str
	
class inputWnd:
	def __init__(self): 
		self.gladeFile="src_Wnd.glade"
		self.gladeMain = gtk.Builder() 
		self.gladeMain.add_from_file(self.gladeFile) 
		self.gladeMain.connect_signals(self)
		
		self.mainWindow = self.gladeMain.get_object("inputWnd")
		self.mainWindow.set_position(gtk.WIN_POS_CENTER_ALWAYS) 
		self.mainWindow.set_default_size(420, 300) 
		self.mainWindow.show()
		self.entryNameEntry=None
