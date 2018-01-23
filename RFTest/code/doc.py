#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
import time 
import sys
import zipfile
'''模拟文件的上传、下载、创建多个文件以及删除、重命名等'''
def login():
	'''登录客户端'''
	try:
		cmd='''
		echo '
		tell application "System Events" to set isRunning to exists (process "AnyShare")
		get isRunning
		try
			if isRunning is equal to false then
				tell application "AnyShare"
					activate
				end tell
				delay 1
				set isRunning to false
			end if
			delay 1
			if isRunning is equal to false then
			--切换输入法
			tell application "System Events" to tell process "SystemUIServer"
				click (menu bar items of menu bar 1 whose description is "text input")
				delay 1
				tell (menu bar items of menu bar 1 whose description is "text input")
					click menu item "美国" of menu 1
				end tell
			end tell
			delay 1
			tell application "System Events"
				tell process "AnyShare"
					tell window 1
						click button 5
						delay 1
						keystroke "10.254.0.200"
						delay 1
						key code 48
						keystroke "9998"
						delay 1
						key code 48
						keystroke "9123"
						delay 1
						click button "确定"
						delay 1
						keystroke "t2"
						delay 1
						key code 48
						keystroke "eisoo.com"
						delay 1
						--click checkbox "记住密码"
						click button "登  录"
					end tell
				end tell
			end tell
		end if
		end try
		'|osascript
		'''
		res=os.popen(cmd).read()
		print res
	except Exception, e:
		return "get an Exception",e

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
		--UI elements of window 1
		UI elements of menu bar 1
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
		UI elements of menu bar 1
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
		UI elements of menu bar 1
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
		UI elements of menu bar 1
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

def nsfile(dir,s):
    '''创建多个文件,s为需要生成的文件数'''
    b = os.path.exists("{0}")
    if b:
        print "File Exist!"
    else:
        os.mkdir("{0}")
    #生成文件
    for i in range(1,s+1):
        localTime = time.strftime("%Y%m%d%H%M%S",time.localtime())
        print localTime
        filename = dir+"/"+localTime+".txt"
        #a:以追加模式打开（必要时可以创建）append;b:表示二进制
        f = open(filename,'ab')
        testnote = '测试文件'
        f.write(testnote)
        f.close()
        #输出第几个文件和对应的文件名称
        print "file"+" "+str(i)+":"+str(localTime)+".txt"
        time.sleep(1)
        cmd='''
        echo '
        tell application "System Events"
        tell process "FUSEService"
        delay 1
        UI elements of menu bar 1
        end tell
        end tell
        '|osascript
        '''
    re = os.popen(cmd).read()
    print "ALL Done"
    time.sleep(1)

def Zip(dir,newdir):
	#https://www.cnblogs.com/defineconst/p/6014165.html
	#单个文件压缩
	#dir为要压缩的文件路径,newdir为新创建的文件及路径
	# 新建压缩包，放文件进去,若压缩包已经存在，将覆盖。可选择用a模式，追加
	azip = zipfile.ZipFile('test.zip','w')
	# 必须保证路径存在,如将bb件夹（及其下aa.txt）添加到压缩包,压缩算法LZMA
	azip.write(dir,compress_type=zipfile.ZIP_LZMA)
	# 写入一个新文件到压缩包中，data是该文件的具体内容，可以是str或者是byte。
	# 这里是新建一个bb文件夹，其下再新建一个cc.txt,将hello world写入到文本中
	azip.writestr(newdir,data='hello world',compress_type=zipfile.ZIP_DEFLATED)
	# 关闭资源
	azip.close()

def zip_dir(dirname,zipfilename):
	#压缩文件夹,dirname为要压缩的文件，zipfilename为压缩后文件名
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        print arcname
        zf.write(tar,arcname)
        print tar
    zf.close()
    #移动文件或重命名
    #https://www.cnblogs.com/kaituorensheng/archive/2013/03/18/2965766.html
    #shutil.move(arcname,'/Volumes/AnyShare/MyDocuments.localized/t2')
def zip_undo(zipfilename):
    #zip_dir(dirname,zipfilename).zf.extractall(path)
    #解压
    print 'unpack'
    zip_file = zipfile.ZipFile(zipfilename)  
    if os.path.isdir(zipfilename + "_files"):  
        pass  
    else:  
        os.mkdir(zipfilename + "_files")  
    for names in zip_file.namelist():  
        zip_file.extract(names,zipfilename + "_files/")  
    zip_file.close()  


if __name__ == '__main__':
	re=login()
	print re
	#res=makeDir("/Volumes/AnyShare/MyDocuments.localized/t1/TMP")
	#copy("/Users/elvis/Desktop/AS问题反馈.docx","/Volumes/AnyShare/MyDocuments.localized/t1/TMP")
	#s=input("请输入需要生成的文件数：")
	#re=nsfile("/Volumes/AnyShare/MyDocuments.localized/t1/TMP",s)
	#zip_dir('/Volumes/AnyShare/MyDocuments.localized/t2/zip','compress.zip')
	zip_undo('/Volumes/AnyShare/MyDocuments.localized/t2/zip/compress.zip')
