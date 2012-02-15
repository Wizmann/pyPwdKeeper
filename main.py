import sys
import sqlite3
import pygtk 
import gtk 

pygtk.require('2.0') 

class HelloWorld:
	def __init__(self): 
		 self.gladeMain = gtk.Builder() 
		 self.gladeMain.add_from_file("src_Wnd.glade") 
		 self.gladeMain.connect_signals(self)
		 self.mainWindow = self.gladeMain.get_object("registerWnd") 
		 self.mainWindow.set_position(gtk.WIN_POS_CENTER_ALWAYS) 
		 self.mainWindow.set_default_size(420, 300) 
		 self.mainWindow.show() 

	def on_cmdQuit_clicked(self, *args): 
		 print "on_cmdCancel_clicked" 
		 gtk.main_quit() 

	def on_cmdOK_clicked(self, *args): 

		 print "on_cmdOK_clicked occurred: Hello World" 
		 self.mainWindow.set_title("Hello World") 

	def main(self): 
		gtk.main() 

if(__name__ == "__main__"): 

	hello = HelloWorld() 

	hello.main() 
