#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
import time 
import sys

def nsfile(dir,s):
    '''创建多个文件'''
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
    print "ALL Down"
    time.sleep(1)

if __name__ == '__main__':
    s = input("请输入需要生成的文件数：")
    re = nsfile("/Volumes/AnyShare/MyDocuments.localized/t1/TMP",s)