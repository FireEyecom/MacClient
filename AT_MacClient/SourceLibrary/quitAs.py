#!/usr/bin/python
#coding: UTF-8
import os
import time
import applescript
#def quit_As(application_name="/Applications/Anyshare.app"):
#利用applescript代码，使anyshare客户端退出dock
def quit_As():
    try:
        as_cmd='''      
            echo '
            tell application "System Events"
            tell process "Dock"
            tell UI element "AnyShare" of list 1
            perform action "AXShowMenu"
            delay 1
            tell menu 1 to click menu item "退出"
            delay 2
            end tell
            end tell
            end tell
            tell application "System Events" to tell process "Dock" to tell list 1 to set isRunning to exists (UI element "AnyShare")
            '|osascript'''
        #scpt = 'echo sus'
        #获取错误信息
        #re=subprocess.Popen(scpt, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read() 
        #print re
        scpt='''
            echo '
            tell application "System Events"
            tell process "Dock" to tell list 1 to set isRunning to exists (UI element "AnyShare")
            end tell
            '|osascript'''
        scpt1='''
            echo '
            tell application "System Events" to set isRunning to exists (processes where name is "AnyShare")
            tell application "System Events" to set isRunning to exists (processes where name is "FUSEService")
            '|osascript'''
        res=os.popen(as_cmd).read()
        str=os.popen(scpt).read()
        str1=os.popen(scpt1).read()
        if res == str:
            if res == str1:
                print "quit AS succeed"
                return "success"  
            else:
                print "get an exception"
                return "get an exception",res        
        else:
            print "get an exception"
            return "get an exception",res
    except Exception,e:
        print "get an exception1"
        return "get an exception",e
#res=quit_As(application_name="/Applications/Anyshare.app")
if __name__ == '__main__':
    res=quit_As()
    print "the end"
    print res
#content=os.popen('help').read()
#print content


