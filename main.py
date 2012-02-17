#!/usr/bin/env python
# -*- encoding: utf-8 -*- 

import sys
import os
import pygtk 
import gtk
import globeCtrl
from db import dbCtrl
from regWnd import regWnd
from loginWnd import loginWnd
from mainWnd import mainWnd

pygtk.require('2.0') 

if(__name__ == "__main__"):
	db=dbCtrl()
	md5Pwd=db.dbGetSuperPwd()
	if(md5Pwd==None):
		newRegWnd=regWnd()
		newRegWnd.main()
	
	if(globeCtrl.gCtrl.quit==True):
		exit(0)
	
	#如果没有用户的密码，则要求注册
	#然后登录	
	newloginWnd=loginWnd()
	newloginWnd.main()
	
	if(globeCtrl.gCtrl.quit==True or 
			globeCtrl.gCtrl.loginSuccess==False):
		exit(0)
	
	newMainWnd=mainWnd()
	newMainWnd.main()
