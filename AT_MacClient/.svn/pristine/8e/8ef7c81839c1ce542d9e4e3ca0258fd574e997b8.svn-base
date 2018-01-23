#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

import requests
import os
import json
import time


def user_login(username, password, ip, port=9998):
	'''
	用户身份验证
	'''
	url = "http://%s:%s/v1/auth?method=get" %(ip,port)
	data = {"account":username,"password":password}
	# data = json.dumps(data)
	try:
		re = requests.request("POST",url,json=data,verify=False)
		result = re.content
		result = json.loads(result)
		return re.status_code ,result["userid"], result["tokenid"],result
	except Exception, e:
		return "get an exception",e

def getEntrydoc(userid,tokenid,doctype,ip,port=9998):
	'''
	获取入口文档
	doctype
	1： 用户个人文档
	2： 用户群组文档
	3： 用户自定义文档库
	4： 共享文档库
	5： 归档库 
	'''
	try:
		url = "http://%s:%s/v1/entrydoc?method=getbytype&userid=%s&tokenid=%s"%(ip,port, userid,tokenid)
		data = {"doctype":doctype}
		re = requests.request("POST",url,json=data,verify=False)
		result = re.content
		result = json.loads(result)
		docinfos = result["docinfos"]
		return re.status_code, docinfos
	except Exception, e:
		return "get an exception" ,e

def dirList(docid,ip,userid,tokenid,attr=True,port=9123):
	'''
	浏览目录
	by: 指定按哪个字段排序,若不指定，默认按docid升序排序  name，按文件名称（中文按拼音）排序 size，按大小排序（目录按name升序） time，按服务器修改时间排序
	sort:升序还是降序，默认为升序 asc，升序  desc，降序
	attr 默认为false,即不取文件或者目录属性信息,为true时,则取文件或者目录的属性信息
	'''
	try:
		url = "http://%s:%s/v1/dir?method=list&userid=%s&tokenid=%s"%(ip,port, userid,tokenid)
		data = {"docid":docid,"attr":attr}
		#data = {"docid":docid,"by":by,"sort":sort,"attr":attr}
		re = requests.request("POST",url,json=data,verify=False)
		result = re.content
		result = json.loads(result)
		dirs = result["dirs"]
		files = result["files"]
		return re.status_code ,dirs, files
	except Exception, e:
		return "get an exception", e
def getFromDictionary(var,key):
	try:
		re = var[key]
		return re
	except Exception, e:
		return "get an exception",e

def fileDelete(docid,ip,userid,tokenid,port=9123):
	'''
	删除文件，此接口未经过mac客户端删除文件，因此mac客户端本地数据库仍保存有已删除文件的gns，
	将与已删除文件的同名文件 复制至  已删除文件未删除前所在目录，会报错：请求的文件或文件夹不存在 
	这是因为复制文件时，mac客户端会检查文件是否存在，mac客户端本地数据库未与服务端数据同步，故而未检测到
	目标路径同名文件已删除，调用上传接口时会传递已删除文件的gns。
	
	'''
	try:
		url = "http://%s:%s/v1/file?method=delete&userid=%s&tokenid=%s"%(ip,port,userid,tokenid)
		data = {"docid":docid}
		re = requests.request("POST",url,json=data,verify=False)
		return re.status_code ,re.content
	except Exception, e:
		return "get an exception", e
		
def dirDelete(docid, userid ,tokenid ,ip , port=9123):
	'''
	删除目录
	'''
	try:
		url = "http://%s:%s/v1/dir?method=delete&userid=%s&tokenid=%s"%(ip,port,userid,tokenid)
		data = {"docid":docid}
		re = requests.request("POST", url, json=data,verify=False )
		return re.status_code ,re.content
	except Exception, e:
		return "get an exception", e

def generatePermconfig(isallowed, permvalue, accessorid, accessortype, endtime, inheritpath=''):
	'''
	生成一条权限配置项
	id int N 表示需要编辑的权限配置项的id，新版无视
	isallowed bool Y true表示允许权限，false表示拒绝权限
	permvalue int Y 0x00000001, 显示 0x00000002，预览 0x00000004，下载 0x00000008，新建 0x00000010，修改 0x00000020，删除 0x00000040，复制
	accessorid string Y 表示访问者id，可能是用户，部门
	accessortype string Y 表示访问者类型，值域为【”user“，”department“,”contactor”】
	endtime int Y 到期时间，如果为-1，表示无限期 如果entime对应的时间为：2015-10-16，15:30:33 后端自动会将时间调整为：2015-10-1623:59:59
	inheritpath string Y 表示继承的docid路径，被设置是当前目录则为空
	'''
	permconfig={"isallowed":isallowed,"permvalue":permvalue,"accessorid":accessorid,"accessortype":accessortype,"endtime":endtime,"inheritpath":inheritpath}
	return permconfig

def setPerm(userid, tokenid ,docid, permconfigs, ip, port=9998):
	'''
	批量设置权限
	'''
	try:
		url = "http://%s:%s/v1/perm1?method=set&userid=%s&tokenid=%s"%(ip,port,userid,tokenid)
		data = {"docid":docid,"permconfigs":permconfigs}
		re =requests.request("POST",url,json=data,verify=False)
		return re.status_code,re.content
	except Exception, e:
		return "get an exception",e

def generateOwnerconfig(userid, inheritpath=''):
    '''
    生成一条所有者配置项
    '''
    userconfig = {"userid":userid, "inheritpath":inheritpath}
    return userconfig


def setOwner(docid, userid, tokenid, userconfigs,ip,port=9998):
    '''
    批量设置所有者
    '''
    try:
        url = "http://%s:%s/v1/owner?method=set&userid=%s&tokenid=%s"%(ip, port, userid, tokenid)
        data = {"docid":docid,"userconfigs":userconfigs}
        re =requests.request("POST",url,json=data,verify=False)
        return re.status_code,re.content        
    except Exception, e:
        return "get an exception",e

def eossurl(requrl, method, auth, content='', filename='', downloadpath=''):
    dict1 = {}
    for i in auth:
        temp = i.split(': ')
        dict1[str(temp[0])]= str(temp[1])
    r = requests.request(method, requrl, data=content, headers=dict1, verify=False, stream=True)
    if method == 'GET':
        body = open(downloadpath +'/' + filename, 'wb')
        for chunk in r.iter_content(chunk_size=1048576): 
            if chunk:
                body.write(chunk) 
    if r.status_code == 201 or r.status_code == 200:
        if method == 'PUT' or method == 'POST':
            header = r.headers
            print header
            try:
                if 'Etag' in header:
                    etag = header['Etag']
                else:
                    etag = header['ETag']
                return r.status_code, etag
            except:
                pass
    else: 
        return r.status_code, ''

def new_file_upload(ip, gnsobject, userid, tokenid, file1, iscomplete, versionid, isexist, ondup=0, md5='', crc32='', slice_md5='', csflevel=0, https=0, uploadid='',port=9123):
    '''
    上传文件
    '''
    # file1 = file1.encode('utf-8')
    print 'uploadid %s' % uploadid
    gnsobject = gnsobject.replace('\\', '')
    firstdatabl=''
    clienttime = int(time.time())
    if isexist != True:
        name = os.path.basename(file1)
        isexist = False
    else:
        name = os.path.basename(file1)
        name = ''
        isexist = True
    flag = True
    input1 = open(file1, 'rb')
    filesize = os.path.getsize(file1)
    sn = 0  
    if filesize <= 4*1024*1024:
        filegns, rev, uploadid, respondcode = uploadsmallfile(ip, gnsobject, userid, tokenid, file1, isexist, ondup, csflevel, https)
    else:
        filegns, rev, uploadid, respondcode = uploadbigfile(ip, gnsobject, userid, tokenid, file1, versionid, iscomplete, isexist, ondup, uploadid, csflevel, https)
    if respondcode == 200 or respondcode == 201:
        return 'success', filegns, rev, uploadid
    else:
        return 'get an exception', filegns, rev, uploadid

def uploadsmallfile(ip, gns, userid, tokenid, file1, isexist, ondup, csflevel, https=0):
    '''
    上传小文件
    '''
    filesize = os.path.getsize(file1)
    name = os.path.basename(file1)
    if isexist:
        respondcode, filegns, rev, authrequest = osbeginupload(ip, gns, filesize, '',  userid, tokenid, ondup, https)
        print "1"
    else:
        respondcode, filegns, rev, authrequest = osbeginupload(ip, gns, filesize, name,  userid, tokenid, ondup, https)
        print "2"
    if respondcode == 200:
        pass
    else:
        return filegns, rev, authrequest, respondcode
    print filegns, rev, authrequest
    if 'gns' in str(filegns):
        input1 = open(file1, 'rb')
        content = input1.read()
        requrl = authrequest[1]
        method = authrequest[0]
        auth = authrequest[2:]
        status_code, tag = eossurl(requrl, method, auth, content)
        print status_code
        if status_code == 503:
            return status_code, '', '', status_code
        osendstatus, osendcontent = osendupload(ip, filegns, rev, '', '', '', csflevel, userid, tokenid)
        if osendstatus == 200:
            return filegns, rev, '', status_code
        else:
            return '', osendcontent, '', osendstatus
    return filegns, rev, '', status_code

def uploadbigfile(ip, filegns, userid, tokenid, file1, versionid, iscomplete, isexist, ondup, uploadid='', csflevel=0, https=0):
    '''
    上传大文件
    '''
    size = ospartminsize(ip, userid, tokenid)
    if size <= 4 * 1024 * 1024:
        size = 4 * 1024 * 1024
    filesize = os.path.getsize(file1)
    name = os.path.basename(file1)
    if not versionid:
        if isexist:
            filegns, versionid, uploadid = osinitmultiupload(ip, filegns, filesize, '',  userid, tokenid, ondup, https)
        else:
            filegns, versionid, uploadid = osinitmultiupload(ip, filegns, filesize, name,  userid, tokenid, ondup, https)
    count = filesize / size
    partsdictbegin = '{'
    partsdictend = '}'
    partsdict = ''
    input1 = open(file1, 'rb')
    if filesize % size:
        count = count + 1
    if 'gns://' in str(filegns):
        respondcode, authrequest= osuploadpart(ip, filegns, versionid, uploadid, '1-%s'% (count), userid, tokenid, https)
    else:
        return filegns, versionid, uploadid
    if respondcode == 200:
        for i in xrange(count):
            chunk = input1.read(size)
            requrl = authrequest[str(i+1)][1]
            method = authrequest[str(i+1)][0]
            auth = authrequest[str(i+1)][2:]
            status_code, tag = eossurl(requrl, method, auth, chunk)
            partstag = [tag, len(chunk)]
            partsdict += '"%s":%s,'  % (str(i+1), partstag)
        partinfo =  partsdictbegin + partsdict[:-1] +partsdictend
        partinfo = eval(partinfo)
        respondecode, body, authrequest = oscompleteupload(ip, filegns, versionid, uploadid, partinfo, userid, tokenid, https)
        if respondecode == 200: 
            requrl = str(authrequest[1])
            method = str(authrequest[0])
            auth = authrequest[2:]
            eossurl(requrl, method, auth, body)
            if iscomplete:
                osendupload(ip, filegns, versionid, '', '', '', csflevel, userid, tokenid, https)
        else:
            return respondecode, '', ''
        return filegns, versionid, uploadid, respondcode
    else:
        return respondcode, authrequest, '', respondcode

def osbeginupload(ip, gns, length, name, userid, tokenid, ondup=0, https=0):
    '''
    开始上传
    '''
    if https:
        requrl = 'https://%s:%s/v1/file?method=osbeginupload&userid=%s&tokenid=%s' %(ip, 9124, userid, tokenid)
    else:
        requrl = 'http://%s:%s/v1/file?method=osbeginupload&userid=%s&tokenid=%s' %(ip, 9123, userid, tokenid)
    clienttime = time.time() * 1000000
    uploadjson = {'docid' : gns, 'length' : length, 'name':name, 'client_mtime':clienttime, 'ondup':ondup} 
    r = requests.request('POST', requrl, json=uploadjson, verify=False)
    respondcode, content= r.status_code, r.content 
    print content
    if respondcode == 200:
        content = json.loads(content)     
        authrequest = content['authrequest']
        filegns = content['docid']
        rev = content['rev']
        name = content['name']
        return respondcode, filegns, rev, authrequest
    else:
        return respondcode, json.loads(content),'',''

def osinitmultiupload(ip, gns, length, name, userid, tokenid, ondup=0, https=0):
    '''
    开始上传大文件
    '''
    if https:
        requrl = 'https://%s:%s/v1/file?method=osinitmultiupload&userid=%s&tokenid=%s' %(ip, 9124, userid, tokenid) 
    else:
        requrl = 'http://%s:%s/v1/file?method=osinitmultiupload&userid=%s&tokenid=%s' %(ip, 9123, userid, tokenid)
    clienttime = time.time() * 1000000
    uploadjson = {'docid' : gns, 'length': length, 'name':name, 'client_mtime':clienttime, 'ondup':ondup} 
    print uploadjson
    r = requests.request('POST', requrl, json=uploadjson, verify=False)
    respondcode, content= r.status_code, r.content 
    if respondcode == 200:
        content = json.loads(content)
        uploadid = content['uploadid']
        filegns = content['docid']
        rev = content['rev']
        return filegns, rev, uploadid
    else:
        return respondcode, json.loads(content),''

def osuploadpart(ip, gns, rev, uploadid, parts, userid, tokenid, https=0):
    '''
    上传大文件的分块协议
    '''
    if https:
        requrl = 'https://%s:%s/v1/file?method=osuploadpart&userid=%s&tokenid=%s' %(ip, 9124, userid, tokenid)
    else:   
        requrl = 'http://%s:%s/v1/file?method=osuploadpart&userid=%s&tokenid=%s' %(ip, 9123, userid, tokenid)
    uploadjson = {'docid' : gns, 'rev' : rev, 'uploadid':uploadid, 'parts':parts} 
    print uploadjson
    r = requests.request('POST', requrl, json=uploadjson, verify=False)
    respondcode, content= r.status_code, r.content 
    if respondcode == 200:
        content = json.loads(content)
        authrequests = content['authrequests']
        return respondcode, authrequests
    else:
        return respondcode, json.loads(content)

def oscompleteupload(ip, gns, rev, uploadid, partinfo, userid, tokenid, https=0):
    '''
    上传大文件的分块完成协议
    '''
    if https:
        requrl = 'https://%s:%s/v1/file?method=oscompleteupload&userid=%s&tokenid=%s' %(ip, 9124, userid, tokenid)
    else:
        requrl = 'http://%s:%s/v1/file?method=oscompleteupload&userid=%s&tokenid=%s' %(ip, 9123, userid, tokenid)
    uploadjson = {'docid' : gns, 'rev' : rev, 'uploadid':uploadid, 'partinfo':partinfo} 
    r = requests.request('POST', requrl, json=uploadjson, verify=False)
    headers = r.headers
    contenttype = headers['content-type']
    respondcode, content= r.status_code, r.content 
    if respondcode == 200:
        boundry = sub_boundry(contenttype)
        body,jsondata = sub_body(content, boundry)
        print type(jsondata)
#        body = result[0]
#        result = json.loads(result[1])
        authrequest = jsondata['authrequest']
        return respondcode, body, authrequest
    else:
        return respondcode, json.loads(content), ''
def sub_boundry(str1):
    boundry = str1.split(';')
    boundry = boundry[1]
    boundry = boundry[9:]
    return boundry
def sub_body(str1, boundry):
    length = len('--' + boundry)
    temp = str1[length + 2:]
    i = temp.find('--' + boundry)
    body = temp[0: i - 2]
    temp = temp[i + length + 2:]
    i = temp.find('--' + boundry)
    jsondata = temp[0: i - 2]
    jsondata = json.loads(jsondata)
    return body, jsondata
def ospartminsize(ip, userid, token):
    '''
    上传大文件的分块大小
    '''
    requrl = "http://%s:%s/v1/file?method=ospartminsize&userid=%s&tokenid=%s" %(ip, 9123, userid, token)
    r = requests.request('POST', requrl, verify=False)
    content = json.loads(r.content)
    if r.status_code == 200:
        size = content['size']
        return size
    else:
        return respondcode

def osendupload(ip, gns, rev, md5, crc32, slice_md5, csflevel, userid, tokenid, https=0):
    '''
    上传完成
    '''
    if https:
        requrl = 'https://%s:%s/v1/file?method=osendupload&userid=%s&tokenid=%s' %(ip, 9124, userid, tokenid)
    else:
        requrl = 'http://%s:%s/v1/file?method=osendupload&userid=%s&tokenid=%s' %(ip, 9123, userid, tokenid)  
    uploadjson = {'docid' : gns, 'rev' : rev, 'md5':md5, 'crc32':crc32, 'slice_md5':slice_md5, "csflevel":csflevel} 
    print 'json:', uploadjson
    print 'url:', requrl
    r = requests.request('POST', requrl, json=uploadjson, verify=False)
    respondcode, content= r.status_code, r.content 
    print respondcode, content
    return respondcode, json.loads(content)

def fileMetadata(userid,tokenid,docid,ip,port=9123):
    try:
        url = "http://%s:%s/v1/file?method=metadata&userid=%s&tokenid=%s"%(ip,port,userid,tokenid)
        data = {"docid":docid}
        re = requests.request("POST",url,json=data,verify=False)
        result = re.content
        result = json.loads(result)
        return re.status_code , result
    except Exception, e:
        return "get an exception",e


if __name__ == '__main__':
	# re = user_login("test0", "EISOO.com123", "192.168.136.134")
	# re1 = getEntrydoc(re[1],re[2],1,"192.168.136.134")
	# re2 = dirList(re1[1][0]["docid"],"192.168.136.134",re[1],re[2])
	# print re2[1]
	# print re2[2]
    re = fileMetadata



