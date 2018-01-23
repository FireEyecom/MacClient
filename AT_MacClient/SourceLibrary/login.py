#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
#概述
#一、登录
#启动应用程序                              activate_application 
#关闭登录窗口                              CloseLoginWindow
#设置登录服务器以及端口号                    loginset_serverIpAndPort 
#输入用户名密码并登录AnyShare               login_WithUsernameAndPassword
#设置登录方式为自动登录                      loginset_AutoLogin
#检查是否为自动登录                          isLoginAutomatically
#取消自动登录                               loginset_cancelAutoLogin
#设置密码保存方式：记住密码或取消记住密码       loginset_passwordMode
#检查密码保存方式                            isPasswordRemembered
#未输入登录用户名以及密码，直接登录AnyShare    login_WithoutUsernameAndPassword
#退出登录                                   logoff

#更改输入法为美国输入法                      setInputMethod



#启动应用程序
def activate_application(application_name="/Applications/AnyShare.app"):

	try:
		cmd = 'open {0}'.format(application_name)
		result = os.popen(cmd).read()
		activate_aplication_cmd='''
		echo '
		tell application "System Events"
			tell process "CoreServicesUIAgent"
				delay 3
				click button "打开" of window 1
			end tell
		end tell
		delay 10
		tell application "System Events"
		tell process "AnyShare"
		UI elements of window 1
		end tell
		end tell
		'|osascript'''
		re= os.popen(activate_aplication_cmd).read()
		ui='button Cut of window 1 of application process AnyShare, button Paste of window 1 of application process AnyShare, button Undo of window 1 of application process AnyShare, button Copy of window 1 of application process AnyShare, checkbox \xe8\xae\xb0\xe4\xbd\x8f\xe5\xaf\x86\xe7\xa0\x81 of window 1 of application process AnyShare, static text \xe7\xbb\x9f\xe4\xb8\x80\xe7\x9a\x84\xe6\x96\x87\xe6\xa1\xa3\xe4\xba\x91 of window 1 of application process AnyShare, checkbox \xe8\x87\xaa\xe5\x8a\xa8\xe7\x99\xbb\xe5\xbd\x95 of window 1 of application process AnyShare, button 5 of window 1 of application process AnyShare, image 1 of window 1 of application process AnyShare, group 1 of window 1 of application process AnyShare, group 2 of window 1 of application process AnyShare, button \xe7\x99\xbb  \xe5\xbd\x95 of window 1 of application process AnyShare, button 7 of window 1 of application process AnyShare, static text 2 of window 1 of application process AnyShare\n'
		if re==ui:
			return "success","manuaLogin"
		elif re=='':
			return "success","autoLogin"
		else:
			return "get an exception",re

	except Exception, e:
		return "get an exception",e

#关闭登录窗口
def CloseLoginWindow():
	try:
		cmd='''
		echo '
		tell application "System Events"
		tell process "AnyShare"
		click button 7 of window 1
		end tell
		end tell
		'|osascript
		'''
		
		re = os.popen(cmd).read()	

		return "success",re
		
	except Exception, e:
		return "get an exception",e

#设置登录服务器以及端口号
def loginset_serverIpAndPort(server_addr,authPort=9998,filePort=9123):
	try:
		set_serverIpAndPort_cmd='''
		echo '
		tell application "System Events"
		tell process "AnyShare"
		click button 5 of window 1
		delay 1
		keystroke "{0}"
		delay 1
		key code 48
		keystroke "{1}"
		delay 1
		key code 48
		keystroke "{2}"
		delay 1
		click button "确定" of window 1
		delay 1
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''.format(server_addr,authPort,filePort)
		ui='button Cut of window 1 of application process AnyShare, button Paste of window 1 of application process AnyShare, button Undo of window 1 of application process AnyShare, button Copy of window 1 of application process AnyShare, checkbox \xe8\xae\xb0\xe4\xbd\x8f\xe5\xaf\x86\xe7\xa0\x81 of window 1 of application process AnyShare, static text \xe7\xbb\x9f\xe4\xb8\x80\xe7\x9a\x84\xe6\x96\x87\xe6\xa1\xa3\xe4\xba\x91 of window 1 of application process AnyShare, checkbox \xe8\x87\xaa\xe5\x8a\xa8\xe7\x99\xbb\xe5\xbd\x95 of window 1 of application process AnyShare, button 5 of window 1 of application process AnyShare, image 1 of window 1 of application process AnyShare, group 1 of window 1 of application process AnyShare, group 2 of window 1 of application process AnyShare, button \xe7\x99\xbb  \xe5\xbd\x95 of window 1 of application process AnyShare, button 7 of window 1 of application process AnyShare, static text 2 of window 1 of application process AnyShare\n'
		re = os.popen(set_serverIpAndPort_cmd).read()	
		if re==ui:
			return "success",re
		else:
			return "get an exception", re
		
	except Exception, e:
		return "get an exception",e

#输入用户名密码并登录AnyShare
def login_WithUsernameAndPassword(username,password):
	try:
		set_usernameAndPassword_cmd='''
		echo '
		tell application "System Events"
		tell process "AnyShare"
		delay 3
		keystroke "{0}"
		delay 1
		key code 48
		keystroke "{1}"
		click button "登  录" of window 1
		delay 5
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''.format(username,password)
		re = os.popen(set_usernameAndPassword_cmd).read()	
		re1 = shouldBeEqual1(re,"sheet")
		if re == '':
			return "success",re
		elif re1 =='success':
			cmd = '''
			echo '
			tell application "System Events"
			tell process "AnyShare"
			UI elements of sheet 1 of window 1
			end tell
			end tell
			'|osascript
			'''
			re2 = os.popen(cmd).read()
			return "get an exception",re2
		else:
			return "get an exception",re
		
	except Exception, e:
		return "get an exception",e

#设置登录方式为自动登录（appscript）
def loginset_AutoLogin(username,password):
	try:
		
		set_autoLogin_cmd='''
		echo '
		tell application "System Events"
		tell process "AnyShare"
		keystroke "{0}"
		delay 1
		key code 48
		keystroke "{1}"
		delay 1
		click checkbox "自动登录" of window 1
		delay 1
		click button "登  录" of window 1
		delay 1
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''.format(username,password)
		re = os.popen(set_autoLogin_cmd).read()	
		logoff()
		if re=='':
			return "success",re
		else:
			return "get an exception",re
		
	except Exception, e:
		return "get an exception",e
	
#检查是否为自动登录（查看数据库）
def isLoginAutomatically():
	pass
#取消自动登录(数据库取消)
def loginset_cancelAutoLogin():
	pass
#设置密码保存方式：记住密码或取消记住密码（appscript）
def loginset_passwordMode(username,password):
	try:
		set_isPasswordRemembered_cmd='''
		echo '
		tell application "System Events"
		tell process "AnyShare"
		keystroke "{0}"
		delay 1
		key code 48
		delay 1
		keystroke "{1}"
		delay 1
		click checkbox "记住密码" of window 1
		delay 1
		click button "登  录" of window 1
		delay 1
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''.format(username,password)
		re = os.popen(set_isPasswordRemembered_cmd).read()	
		logoff()
		if re=='':
			return "success",re
		else:
			return "get an exception",re
		
	except Exception, e:
		return "get an exception",e
#检查密码保存方式（查看数据库）
def isPasswordRemembered():
	pass
#未输入登录用户名以及密码，直接登录AnyShare
def login_WithoutUsernameAndPassword():
	try:
		login_WithoutUsernameAndPassword_cmd='''
		echo '
		tell application "System Events"
		tell process "AnyShare"
		delay 1
		click button "登  录" of window 1
		delay 5
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''
		re = os.popen(login_WithoutUsernameAndPassword_cmd).read()	
		re1 = shouldBeEqual1(re,"sheet")
		if re == '':
			return "success",re
		elif re1 =='success':
			cmd = '''
			echo '
			tell application "System Events"
			tell process "AnyShare"
			UI elements of sheet 1 of window 1
			end tell
			end tell
			'|osascript
			'''
			re2 = os.popen(cmd).read()
			return "get an exception",re2
		else:
			return "get an exception",re
		
	except Exception, e:
		return "get an exception",e
#退出登录
def logoff():
	try:
		logoff_cmd='''
		isFUSEServiceProcssExist=`ps auxc | grep AnyShare | awk '{print $2}'`
		if [ $isFUSEServiceProcssExist -ge 0 ];then
			kill -HUP $isFUSEServiceProcssExist
		fi
		isAnyshareProcssExist=`ps auxc | grep FUSEService | awk '{print $2}'`
		if [ $isAnyshareProcssExist -ge 0 ];then
			kill -HUP $isAnyshareProcssExist
		fi
		'''	
		re = os.popen(logoff_cmd).read()
		cmd = '''
		echo '
		tell application "System Events"
			tell process "FUSEService"
				delay 1
				click button "清除缓存" of window 1
			end tell
		end tell
		'|osascript
		'''
		os.popen(cmd)
		return "success",re
	except Exception, e:
		return "get an exception",e	


#更改输入法为美国输入法
# def setInputMethod(username,password,server_addr,authPort="9998",filePort="9123"):
# 	try:
# 		# #取消自动登录
# 		# loginset_cancelAutoLogin()
# 		# #取消记住密码
# 		# status=isPasswordRemembered()
# 		# if status:
# 		# 	loginset_passwordMode(username,password)			
# 		#设置服务器地址以及端口号
# 		re = activate_application()
# 		# if re[0]=="get an exception":
# 		# 	re1 = shouldBeEqual1(re[1],"无法连接服务器")
# 		# 	if re1 =="success":
# 		# 		loginset_serverIpAndPort(server_addr)

# 		loginset_serverIpAndPort(server_addr)
# 		re0 = login_WithUsernameAndPassword(username,password)
# 		logoff()
# 		#登录客户端
# 		activate_application()
# 		re1 = login_WithUsernameAndPassword(username,password)
# 		print re1
# 		logoff()
# 		# #切换中英文后再次登录客户端
# 		# cmd='''
# 		# echo '
# 		# tell application "System Events"
# 		# key code 56
# 		# end tell
# 		# '|osascript
# 		# '''
# 		# os.popen(cmd).read()
# 		# time.sleep(3)
# 		activate_application()
# 		re2 = login_WithUsernameAndPassword(username,password)
# 		print re2
# 		logoff()
# 		#若两次都登录成功，说明当前输入法为美国输入法，若只有一次成功，说明当前输入法不是美国输入法，则切换输入源为美国输入法
# 		if re1[1]=='' and re2[1]=='':
# 			return 'success'
# 		else:
# 			cmd='''
# 			echo '
# 			tell application "System Events"
# 			key code 49 using {command down}
# 			end tell
# 			'|osascript
# 			'''
# 			os.popen(cmd).read()
# 			return 'success'
		
# 	except Exception, e:
# 		return e


#更改输入法为美国输入法
def setInputMethod():
	try:
		cmd = '''
		echo '
		tell application "System Events" to tell process "SystemUIServer"
		click (menu bar items of menu bar 1 whose description is "text input")
		delay 1
		tell (menu bar items of menu bar 1 whose description is "text input")
        click menu item "美国" of menu 1
		end tell
		end tell
		'|osascript
		'''
		re = os.popen(cmd).read()
		return "success",re
	except Exception, e:
		return "get an exception",re


def shouldBeEqual1(UIinfo,errorMessage):
	try:
		if errorMessage in UIinfo:
		   return "success"
		else:
			return "get an exception"
	except Exception, e:
		return e

#登录失败时弹出的提示窗口有是和否按钮，clickButton功能：点击是或否
def clickButton(buttonName):
	try:
		cmd='''
		echo '
		tell application "System Events"
		tell process "AnyShare"
		click button "{0}" of sheet 1 of window 1
		end tell
		end tell
		'|osascript
		'''.format(buttonName)
		re = os.popen(cmd).read()
		return "success",re
	except Exception, e:
		return "get an exception",e



if __name__ == '__main__':


	re = activate_application()	
	print re		
	#re = loginset_serverIpAndPort("192.168.136.134")
	# print "loginset_serverIpAndPort:",re
	# re = login_WithUsernameAndPassword("test5","111111")
	# print re[1]
	# re = shouldBeEqual1(re[1],"您的密码安全系数过低，是否立即修改密码？")
	# print re
	# clickButton("否")

	# logoff()
	# re = loginset_AutoLogin("test1@xendesktop.com","EISOO.com123")
	# print "loginset_autoLogin:",re
	# re = loginset_isPasswordRemembered("test1@xendesktop.com","EISOO.com123")
	# print "loginset_isPasswordRemembered",re
	# logoff()
	# re = login_WithoutUsernameAndPassword()
	# print "loginWithoutUsernameAndPassword:",re
	# logoff()
	# re = loginset_isPasswordRemembered("test1@xendesktop.com","EISOO.com123")
	# print "loginset_isPasswordRemembered",re
	# logoff()
	# re = login_WithoutUsernameAndPassword()
	# print "loginWithoutUsernameAndPassword:",re
	#re = setInputMethod()
	#print re
	# re = login_WithUsernameAndPassword("admin","eisoo.com")
	# re = shouldBeEqual(re[1],"您是管理员角色，无法登录Mac客户端。")
	# #re = shouldBeEqual(re[1],"你")
	# print "shouldBeEqual:",re
