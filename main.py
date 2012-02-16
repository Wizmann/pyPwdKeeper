#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import sys
import pygtk 
import gtk
from db import dbCtrl
from regWnd import regWnd
from loginWnd import loginWnd

pygtk.require('2.0') 

if(__name__ == "__main__"):
	db=dbCtrl()
	md5Pwd=db.dbGetSuperPwd()
	if(md5Pwd!=None):
		newWnd=regWnd()
		newWnd.main() 
	else:
		newWnd=loginWnd()
		newWnd.main()
