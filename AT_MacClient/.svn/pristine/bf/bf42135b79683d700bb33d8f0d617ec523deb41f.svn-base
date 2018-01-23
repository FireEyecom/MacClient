#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

def copy(SourceFile,destination):
	'''
	复制文件
	'''
	try:
		cmd='''
		cp -rf {0} {1}
		'''.format(SourceFile, destination)
		print cmd
		os.popen(cmd)
		cmd='''
		echo '
		tell application "System Events"
		tell process "FUSEService"
		delay 1
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''
		re = os.popen(cmd).read()
		print re
		if re=='':
			return "success",re
		else:
			return "get an exception",re

	except Exception, e:
		return "get an exception",e


#文件操作失败时弹出的提示窗口有”好“按钮，clickButton1功能：点击按钮
def clickButton1(buttonName="好"):
	try:
		cmd='''
		echo '
		tell application "System Events"
		tell process "FUSEService"
		delay 1
		click button "{0}" of window 1
		end tell
		end tell
		'|osascript
		'''.format(buttonName)
		re = os.popen(cmd).read()
		return "success",re
	except Exception, e:
		return "get an exception",e

def deleteFile(DocName):
	'''
	删除文档
	'''
	try:
		cmd='''
		rm -rf {0}
		'''.format(DocName)
		print cmd
		os.popen(cmd)
		cmd='''
		echo '
		tell application "System Events"
		tell process "FUSEService"
		delay 1
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''
		re = os.popen(cmd).read()
		if re=='':
			return "success",re
		else:
			return "get an exception",re

	except Exception, e:
		return "get an exception",e
def listDir(parentPath,dirName):
	'''
	模拟mac客户端浏览目录
	parentPath:待浏览目录的父目录   例：AnyShare:个人文档
	dirName:待浏览目录名称          例：test0
	'''
	try:
		if dirName=='':
			cmd='''
			echo '
			tell application "Finder"
			open "{0}"
			end tell
			tell application "System Events"
			tell process "FUSEService"
			delay 1
			UI elements of window 1
			end tell
			end tell
			'|osascript
			'''.format(parentPath)
			re = os.popen(cmd).read()
			print re
			if re=='':
				cmd='''
				echo '
				tell application "System Events"
				tell process "Finder"
				click button 1 of window "{0}"
				end tell
				end tell
				'|osascript
				'''.format(parentPath)
				re = os.popen(cmd).read()
				return "success",re
			else:
				return "get an exception", e
		else:
			cmd='''
			echo '
			tell application "Finder"
			open "{0}:{1}"
			end tell
			tell application "System Events"
			tell process "FUSEService"
			delay 1
			UI elements of window 1
			end tell
			end tell
			'|osascript
			'''.format(parentPath,dirName)
			re = os.popen(cmd).read()
			if re=='':
				cmd='''
				echo '
				tell application "System Events"
				tell process "Finder"
				click button 1 of window "{0}"
				end tell
				end tell
				'|osascript
				'''.format(dirName)
				re = os.popen(cmd).read()
				return "success",re		
			else:
				return "get an exception", e		

	except Exception, e:
		return "get an exception", e


def makeDir(dirName):
	'''
	新建文件夹
	'''
	try:
		cmd ='''
		mkdir {0}
		'''.format(dirName)
		os.popen(cmd)
		cmd='''
		echo '
		tell application "System Events"
		tell process "FUSEService"
		delay 1
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''
		re = os.popen(cmd).read()
		
		if re=='':
			return "success",re
		else:
			return "get an exception",re

	except Exception, e:
		return "get an exception",e

def delCache(username):
	'''
	清除客户端缓存
	username指的是mac机器账户名
	'''
	try:
		path = "/Users/%s/Library/Containers/com.eisoo.anyshare.FinderHelper1/Data/Library/Application\ Support/com.eisoo.anyshare"%(username)
		cmd = '''
		cd {0}
		rm -rf anyshare.globe
		rm -rf BACKUP
		rm -rf COREDATA
		'''.format(path)
		re = os.popen(cmd).read()
		return "success",re
	except Exception, e:
		return "get an exception",e

def fileOperation(function, fileName ,application):
	'''
	操作文件
	function取值：1、preview 预览文件 2、edit 编辑文件
	application取值：1、Microsoft Word 2、Microsoft Excel 3、Microsoft PowerPoint 4、TextEdit 5、Sublime Text
	                6、Pages 7、Numbers 8、Keynote
	'''
	try:
		closeButton={'Microsoft Word':1,"Microsoft Excel":5,"Microsoft PowerPoint":1,"TextEdit":1,"Sublime Text":1,\
		             "Pages":1,"Numbers":6,"Keynote":1}
		cmd ='''
		open {0}
		'''.format(fileName)
		os.popen(cmd).read()
		#执行os.popen(cmd).read()后有三种情况 1、打开文件过程中 2、已打开文件 3、打开文件失败，出现1则休眠直至文件打开再执行下一步，出现2，直接执行下一步，出现3，结束。
		#time.sleep(5)
		while 1:
			cmd1 = '''
			echo '
			tell application "System Events"
			tell process "{0}"
			UI elements of window 1
			end tell
			end tell
			'|osascript
			'''.format(application)	
			re1 = os.popen(cmd1).read()
			substring = '''System Events”遇到一个错误：不能获得“process'''
			print re1
			flag = substring in re1
			print flag
			if not flag:
				#有application进程，则文件已打开，跳出循环执行下一步
				break
			else:
				#没有application进程，可能是文件在打开过程中或者打开文件失败
				cmd2='''
				echo '
				tell application "System Events"
				tell process "FUSEService"
				delay 1
				UI elements of window 1
				end tell
				end tell
				'|osascript
				'''
				re2 = os.popen(cmd2).read()
				if re2 == '':
					#文件在打开过程中，休眠直至文件打开
					time.sleep(2)
				else:
					#文件打开失败，存在部分应用程序打开空文件的情况，故而执行操作：关闭文件
					cmd3 = '''
					echo '
					tell application "System Events"
					tell process "{0}"
					click button {1} of window 1
					end tell
					end tell
					'|osascript
					'''.format(application,closeButton[application])
					os.popen(cmd3).read()
					return "get an exception",re2
		#成功打开文件后执行操作
		if function == "preview":
			#虽然函数返回值显示文件已打开，但实际文件有可能处于正在打开中，故休眠2s
			time.sleep(2)
			cmd = '''
			echo '
			tell application "System Events"
			tell process "{0}"
			click button {1} of window 1
			end tell
			end tell
			'|osascript
			'''.format(application,closeButton[application])
			re = os.popen(cmd).read()
			#执行上述关闭命令后，文件关闭，但文件锁状态可能还没有改变，所以休眠5s
			time.sleep(5)
			return "success",re
		elif function=="edit":
			time.sleep(2)
			#编辑文件
			cmd='''
			echo '
			tell application "System Events"
			tell process "{0}"
			keystroke "abcdefg"
			end tell
			end tell
			'|osascript
			'''.format(application)
			os.popen(cmd).read()
			#保存
			cmd='''
			echo '
			tell application "System Events"
			key code 1 using {command down}
			end tell
			'|osascript
			'''
			os.popen(cmd).read()
			#关闭文件
			cmd = '''
			echo '
			tell application "System Events"
			tell process "{0}"
			click button {1} of window 1
			end tell
			end tell
			'|osascript
			'''.format(application,closeButton[application])
			os.popen(cmd).read()
			time.sleep(5)
			#查看是否成功关闭文件
			cmd='''
			echo '
			tell application "System Events"
			tell process "FUSEService"
			UI elements of window 1
			end tell
			end tell
			'|osascript
			'''
			re = os.popen(cmd).read()
			if re =='':
				return "success",re
			else:
				return "get an exception",re

		else:
			pass
			
	except Exception, e:
		return "get an exception",e

def isFileExist(dir1, docName):
	'''
	检查mac机器某个路径下的文件是否存在
	'''
	try:
		cmd = '''
		cd {0}
		ls
		'''.format(dir1)
		re = os.popen(cmd).read()
		flag = docName in re
		if flag:		 
			return "success", re
		else:
			return "get an exception",re
	except Exception, e:
		return "get an exception",e

def moveAndRename(SourceFile,destination):
	'''
	移动或重命名文档
	'''
	try:
		cmd='''
		mv {0} {1}
		'''.format(SourceFile, destination)
		print cmd
		os.popen(cmd)
		cmd='''
		echo '
		tell application "System Events"
		tell process "FUSEService"
		delay 1
		UI elements of window 1
		end tell
		end tell
		'|osascript
		'''
		re = os.popen(cmd).read()
		print re
		if re=='':
			return "success",re
		else:
			return "get an exception",re

	except Exception, e:
		return "get an exception",e

def OpenExternalLink(fileName,filePath):
	'''
	简写开启外链：（1）只配置预览权限（2）开启访问密码（3）开启外链打开次数限制
	'''
	try:
		cmd = '''
		echo '
		tell application "Finder" to select file "{0}" of folder "{1}"
		--tell application "Finder" to select file "test.docx" of folder "AnyShare:My Documents:test0"
		tell application "System Events"
			tell process "Finder"
				delay 2
				set _selection to value of attribute "AXFocusedUIElement"
				tell _selection to perform action "AXShowMenu"
				delay 3
				keystroke "AnyShare"
				key code 124
				key code 76
			end tell
		end tell
		tell application "System Events"
			tell process "FUSEService"
				delay 1
				tell UI element 1 of scroll area 1 of window 1			
					click button "开启链接" of group 2
					delay 5
					click button "复制链接" of group 4
					--点击下载复选框
					perform action "AXPress" of checkbox 1 of group 1 of group 7
					--点击访问密码复选框
					perform action "AXPress" of checkbox 1 of group 1 of group 10
					--点击限制外链打开次数复选框
					perform action "AXPress" of checkbox 1 of group 1 of group 12
					--点击保存按钮
					click button "保存" of group 1 of group 14
				end tell
				--点击关闭按钮
				click button 1 of window 1
			end tell
		end tell

		'|osascript
		'''.format(fileName,filePath)
		re = os.popen(cmd).read()
		if re =="button 1 of window AnyShare of application process FUSEService\n":
			return "success",re
		else:
			return "get an exception",re

	except Exception, e:
		return "get an exception",re

def ClickExternalShare(fileName,filePath):
	'''
	点击外链共享
	'''
	try:
		cmd = '''
		echo '
		tell application "Finder" to select file "{0}" of folder "{1}"
		tell application "System Events"
			tell process "Finder"
				delay 2
				set _selection to value of attribute "AXFocusedUIElement"
				tell _selection to perform action "AXShowMenu"
				delay 2
				keystroke "AnyShare"
				key code 124
				key code 76
			end tell
		end tell

		tell application "System Events"
			tell process "FUSEService"
				delay 2
				UI elements of group 2 of UI element 1 of scroll area 1 of window 1
			end tell
		end tell
		'|osascript
		'''.format(fileName,filePath)
		re = os.popen(cmd).read()
		cmd = '''
		echo '
		tell application "System Events"
			tell process "FUSEService"
				click button 1 of window 1
			end tell
		end tell
		'|osascript
		'''
		os.popen(cmd)
		return "success",re
	except Exception, e:
		return "get an exception",re

def CloseExternalLink(fileName,filePath):
	'''
	关闭外链
	'''
	try:
		cmd = '''
		echo '
		tell application "Finder" to select file "{0}" of folder "{1}"
		tell application "System Events"
			tell process "Finder"
				delay 2
				set _selection to value of attribute "AXFocusedUIElement"
				tell _selection to perform action "AXShowMenu"
				delay 3
				keystroke "AnyShare"
				key code 124
				key code 76		
			end tell
		end tell

		tell application "System Events"
			tell process "FUSEService"
				delay 1
				tell UI element 1 of scroll area 1 of window 1		
					click button "关闭链接" of group 2
				end tell
				click button 1 of window 1		
			end tell
		end tell
		'|osascript
		'''.format(fileName,filePath)
		re = os.popen(cmd).read()
		if re =="button 1 of window AnyShare of application process FUSEService\n":
			return "success",re
		else:
			return "get an exception",re
	except Exception, e:
		return "get an exception",re

def OpenInternalLink(fileName,filePath):
	'''
	简写添加内链访问者 :(1)添加一个访问用户 （2）配置显示权限 （3）复制链接
	'''
	try:
		cmd = '''
		echo '
		tell application "Finder" to select file "{0}" of folder "{1}"
		tell application "System Events"
			tell process "Finder"
				delay 2
				set _selection to value of attribute "AXFocusedUIElement"
				delay 2
				tell _selection to perform action "AXShowMenu"
				delay 3
				keystroke "AnyShare"
				delay 1
				key code 124
				key code 125
				key code 76				
			end tell
		end tell

		tell application "System Events"
			tell process "FUSEService"
				delay 2
				--输入用户名test3
				tell text field 1 of group 1 of group 1 of group 1 of group 5 of UI element 1 of scroll area 1 of window 1
					set p to value of attribute "AXFrame"
					click at p
					keystroke "test3"
				end tell
				
				delay 3
				--点击选择用户
				perform action "AXPress" of group 1 of group 2 of group 1 of group 1 of group 5 of UI element 1 of scroll area 1 of window 1
				delay 1
				--点击三角按钮显示所有的权限配置
				perform action "AXPress" of UI element "显示/预览/下载/复制 " of group 1 of group 1 of group 1 of UI element 3 of row 1 of table 2 of UI element 1 of scroll area 1 of window 1
				--配置显示权限
				tell group 1 of UI element 3 of row 1 of table 2 of UI element 1 of scroll area 1 of window 1
					tell static text "显示" of group 2
						UI elements
						actions
						set p to value of attribute "AXFrame"
						click at p
					end tell
				end tell
				
				--点击复制链接按钮
				click button "复制链接" of group 3 of UI element 1 of scroll area 1 of window "AnyShare"
				--点击确定按钮
				click button "确定" of group 8 of UI element 1 of scroll area 1 of window "AnyShare"
			end tell
		end tell
		'|osascript
		'''.format(fileName,filePath)
		re = os.popen(cmd).read()
		if re=="button \xe7\xa1\xae\xe5\xae\x9a of group 8 of UI element 1 of scroll area 1 of window AnyShare of application process FUSEService\n":
			return "success",re
		else:
			return "get an exception",re

	except Exception, e:
		return "get an exception",re

def DelInternalLinkAccessor(fileName,filePath):
	'''
	删除内链访问者
	（函数实现的功能为删除第二行的访问者）

	'''
	try:
		cmd = '''
		echo '
		tell application "Finder" to select file "{0}" of folder "{1}"
		tell application "System Events"
			tell process "Finder"
				delay 1
				set _selection to value of attribute "AXFocusedUIElement"
				tell _selection to perform action "AXShowMenu"
				delay 1
				keystroke "AnyShare"
				key code 124
				key code 125
				key code 76
			end tell
		end tell

		tell application "System Events"
			tell process "FUSEService"
				delay 3
				tell static text "" of group 1 of UI element 5 of row 2 of table 2 of UI element 1 of scroll area 1 of window 1
					perform action "AXPress"
				end tell
				--点击确定按钮
				click button "确定" of group 8 of UI element 1 of scroll area 1 of window "AnyShare"		
			end tell
		end tell
		'|osascript
		'''.format(fileName,filePath)
		re = os.popen(cmd).read()
		if re=="button \xe7\xa1\xae\xe5\xae\x9a of group 8 of UI element 1 of scroll area 1 of window AnyShare of application process FUSEService\n":
			return "success",re
		else:
			return "get an exception",re

	except Exception, e:
		return "get an exception",re
	


if __name__ == '__main__':
	#copy("/Users/elvis/desktop/com.eisoo.anyshare.plist","/Users/elvis/desktop/未命名文件夹")
	# re = copy("/Users/elvis/desktop/3","/Volumes/AnyShare/Libraries.localized/1/to0")
	# print re[1]
	# clickButton1()
	# clickButton1()
	# re = listDir("AnyShare","")
	# print re
	# re= makeDir("/Volumes/AnyShare/MyDocuments.localized/test0/TMP")
	# print re
	# re = delCache("elvis")
	# re = fileOperation("edit","/Users/elvis/desktop/访问控制开.docx","Microsoft Word")
	# re = isFileExist("/Users/elvis/desktop","1.plist")
	#moveAndRename("/Users/elvis/desktop/1.plist","/Users/elvis/desktop/2.plist")


	# re = OpenExternalLink("test.docx","AnyShare:个人文档:test0")
	# print re
	re = ClickExternalShare("test.docx","AnyShare:个人文档:test0")
	print re

	# re = CloseExternalLink("test.docx","AnyShare:个人文档:test0")
	# print re
	#re = OpenInternalLink("test.docx","AnyShare:个人文档:test0")
	#print re
	# re = DelInternalLinkAccessor("test.docx","AnyShare:个人文档:test0")
	# print re

