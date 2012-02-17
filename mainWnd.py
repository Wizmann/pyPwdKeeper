#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import pygtk 
import gtk
import globeCtrl
from db import dbCtrl
from inputWnd import inputWnd

pygtk.require('2.0')

class mainWnd:
	def __init__(self): 
		self.gladeFile=sys.path[0]+"/src_Wnd.glade"
		self.gladeMain = gtk.Builder() 
		self.gladeMain.add_from_file(self.gladeFile) 
		self.gladeMain.connect_signals(self)
		self.mainWindow = self.gladeMain.get_object("mainWnd")
		self.mainWindow.set_position(gtk.WIN_POS_CENTER_ALWAYS) 
		self.mainWindow.set_default_size(400, 320) 
		self.mainWindow.set_icon_from_file(sys.path[0]+"/src/mainIcon.ico")

		self.mainTreeView=self.gladeMain.get_object('mainTreeView')
		column = gtk.TreeViewColumn('pwd', gtk.CellRendererText(),text=0)
		column.set_resizable(True)
		column.set_sort_column_id(0)
		self.mainTreeView.append_column(column)		
		self.mainList = gtk.ListStore(str)
		self.mainTreeView.set_model(self.mainList)
		
		self.refreshMainTreeView()
		self.selectedRow=-1
		self.mainWindow.show()
		
	def main(self):
		gtk.main()
	
	def on_mainTreeView_row_activated(self, view, path, column):
		self.selectedRow=path
		self.on_mainGetPwd_clicked()
	
	def on_mainGetPwd_clicked(self,*args):
		iter=self.mainList.get_iter(self.selectedRow)
		value=self.mainList.get_value(iter,0)
		db=dbCtrl()
		pwd=db.dbGetPwd(value)
		infoMsgBox=gtk.MessageDialog(None,gtk.DIALOG_MODAL,
											gtk.MESSAGE_INFO,gtk.BUTTONS_OK,
											u'您的密码')
		infoMsgBox.format_secondary_text(pwd)
		infoMsgBox.run()
		infoMsgBox.destroy()
		
	def on_mainDelPwd_clicked(self,*args):
		if(self.selectedRow==-1):
			return
		iter=self.mainList.get_iter(self.selectedRow)
		value=self.mainList.get_value(iter,0)
		db=dbCtrl()
		#print(value)
		db.dbDelPwd(value)
		self.refreshMainTreeView()
		self.selectedRow=-1
		
	
	def on_mainTreeView_cursor_changed(self,*args):
		try:
			self.selectedRow = self.mainTreeView.get_cursor()[0][0]
		except:
			self.selectedRow = -1
		#print self.selectedRow
	
	def refreshMainTreeView(self):
		self.mainList.clear()
		db=dbCtrl()
		db.dbInitMainTable()
		pwdList=db.dbGetMainTableName()
		for item in pwdList:
			self.mainList.append(item)
	
	def on_mainModifyPwd_clicked(self,*args):
		iter=self.mainList.get_iter(self.selectedRow)
		value=self.mainList.get_value(iter,0)
		newInputWnd=inputWnd(value)
		newInputWnd.main()
		self.refreshMainTreeView()
	
	def gtk_main_quit(self, widget, data=None):
		gtk.main_quit()
	
	def on_mainAddNew_clicked(self,*args):
		newInputWnd=inputWnd()
		newInputWnd.main()
		self.refreshMainTreeView()
		
	def on_mainAbout_clicked(self,*args):
		aboutDialog = self.gladeMain.get_object("aboutWnd")
		response=aboutDialog.run()
		aboutDialog.hide()
	
	def on_mainTreeView_unselect_all(self,*args):
		self.selectedRow = -1
		
	def gtk_main_quit(self, widget, data=None):
		gtk.main_quit()
	
