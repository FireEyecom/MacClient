#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
概述：
1、sharemgnt初始化与关闭
2、生成参数
3、自定义函数，方便robotframework的调用
4、用户管理
5、部门管理
6、用户登录访问控制

'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
from ShareMgnt import ncTShareMgnt
from ShareMgnt.ttypes import *
from ShareMgnt.constants import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from EThriftException.ttypes import *



class ShareMgnt_Thrift():

# ##########################################
# 1、sharemgnt初始化与关闭
###########################################

    def shareMgnt_setup(self, ip, port):
        try:
            global share_transport
            global share_client
            share_transport = TSocket.TSocket(ip, port)
            share_transport = TTransport.TBufferedTransport(share_transport)
            share_protocol = TBinaryProtocol.TBinaryProtocol(share_transport)
            share_client = ncTShareMgnt.Client(share_protocol)
            share_transport.open()
        except Exception, e:
            print 'get an exception', e

    def shareMgnt_teardown(self):
        share_transport.close()

# ##########################################
# 2、生成参数
###########################################

    def ncTAddOrgParam(self, orgName, siteId='', priority=999):
        '''
        新建组织操作参数
        '''
        addorginfo = ncTAddOrgParam()
        if orgName is None:
            addorginfo.orgName = orgName
        else:
            addorginfo.orgName = orgName.encode('utf-8')
        addorginfo.siteId = siteId
        addorginfo.priority = priority
        return addorginfo

    def ncTAddDepartParam(self, parentId, departName, siteId='', priority=999):
        """
        新建部门操作参数
        """
        adddepartinfo = ncTAddDepartParam()
        if departName is None:
            adddepartinfo.departName = departName
        else:
            adddepartinfo.departName = departName.encode('utf-8')
        adddepartinfo.parentId = parentId
        adddepartinfo.siteId = siteId
        adddepartinfo.priority = priority
        return adddepartinfo

    def ncTUsrmPasswordConfig(self,strongStatus=0,expireTime=-1,lockStatus=0,passwdErrCnt=3,passwdLockTime=60):
        '''
        设置密码配置信息参数
        '''
        pwdConfig=ncTUsrmPasswordConfig()
        pwdConfig.strongStatus=strongStatus
        pwdConfig.expireTime=expireTime
        pwdConfig.lockStatus=lockStatus
        pwdConfig.passwdErrCnt=passwdErrCnt
        pwdConfig.passwdLockTime=passwdLockTime
        return pwdConfig

    def ncTAccessorInfo(self, accessorId ,accessorType, accessorName):
        '''
        生成网段访问者信息参数 
        1: string id;                       // 访问者id
        2: i32 type;                        // 访问者类型 1:用户, 2:部门
        3: string name;                     // 访问者名称
        '''
        accessors = ncTAccessorInfo()
        accessors.id = accessorId 
        accessors.type = accessorType
        if accessorName is None:
            accessors.name = accessorName
        accessors.name = accessorName.decode("utf-8")
        return accessors



# ##########################################
# 3、自定义函数，方便robotframework的调用
###########################################
# 简写添加用户
    def Add_User(self, loginName, email, departmentIds,password):
        try:
            userInfo = ncTUsrmUserInfo(loginName=loginName.encode('utf8'),
                                       displayName=loginName.encode('utf8'),
                                       email=email, userType=1,
                                       departmentIds=departmentIds,
                                       departmentNames='',
                                       space=50 * 1024 * 1024 * 1024,
                                       csfLevel=5,
                                       pwdControl=False)
            userInfo.loginName = loginName.encode('utf8')
            addUserInfo = ncTUsrmAddUserInfo(user=userInfo,
                                             password=password)
            uuid = share_client.Usrm_AddUser(addUserInfo,
                                       '266c6a42-6131-4d62-8f39-853e7093701c')
            return 'success', uuid
        except Exception, e:
            return 'get an exception',e


    def createOrg(self):
        try:
            addorginfo = self.ncTAddOrgParam(u'爱数')
            cc = self.Usrm_CreateOrganization(addorginfo)
            adddepartinfo = self.ncTAddDepartParam(cc[1], u'AnyShare')
            mm = self.Usrm_AddDepartment(adddepartinfo)
            adddepartinfo = self.ncTAddDepartParam(mm[1], u'研发部')
            subDep = self.Usrm_AddDepartment(adddepartinfo)
            adddepartinfo = self.ncTAddDepartParam(mm[1], u'测试部')
            subsub = self.Usrm_AddDepartment(adddepartinfo)
            adddepartinfo = self.ncTAddDepartParam(mm[1], u'产品部')
            self.Usrm_AddDepartment(adddepartinfo)
            adddepartinfo = self.ncTAddDepartParam(subsub[1], u'AT部')
            re3 = self.Usrm_AddDepartment(adddepartinfo)
            adddepartinfo = self.ncTAddDepartParam(subDep[1], u'基础研发')
            re1=self.Usrm_AddDepartment(adddepartinfo)
            adddepartinfo = self.ncTAddDepartParam(subDep[1], u'云存储')
            re2=self.Usrm_AddDepartment(adddepartinfo)
            print 'create orgDepartment' +'success.'
            return re1,re2,re3
        except Exception, e:
            return "get an exception",e


    def initEnvironment(self):
        try:
            re=self.createOrg()
            depId0=re[0][1]
            depId1=re[1][1]
            for x in xrange(2):
                self.Add_User("test"+str(x), "test"+str(x)+"@eisoo.com",[depId0],"EISOO.com123")
            for x in xrange(2,4):
                self.Add_User("test"+str(x), "test"+str(x)+"@eisoo.com",[depId1],"EISOO.com123")
            depId2=re[2][1]
            self.Add_User("test4", "test4"+"@eisoo.com",[depId2],"111111")
            return "success"

        except Exception, e:
            return e



# ##########################################
# 4、用户管理
###########################################

    def Usrm_AddUser(self, addUserInfo, responsiblePersonId):
        '''
        新建用户
        '''
        try:
            returnList = []
            print dir(client)
            uuid = share_client.Usrm_AddUser(addUserInfo, responsiblePersonId)
            returnList.extend((uuid, 'success')) 
            return returnList
        except Exception, e:
            returnList.extend((e, 'get an exception'))
            return returnList

    def Usrm_SetPasswordConfig(self,pwdConfig):
        '''
        设置用户密码配置信息
        '''
        try:
            re = share_client.Usrm_SetPasswordConfig(pwdConfig)
            return "success",re
        except Exception, e:
            return "get an exception",e

    def Usrm_SetUserStatus(self, userId, status):
        '''
        启用|禁用用户
        '''
        try:
            re = share_client.Usrm_SetUserStatus(userId, status)
            return "success", re
        except Exception, e:
            return "get an exception", e



###########################################
# 5、部门管理
###########################################
    def Usrm_CreateOrganization(self, addorginfo):
        '''
        创建组织
        '''
        try:
            returnList = []
            uuid = share_client.Usrm_CreateOrganization(addorginfo)
            returnList.append('success')
            returnList.append(uuid)
            return returnList
        except Exception, e:
            returnList.append('get an exception')
            return returnList

    def Usrm_AddDepartment(self, adddepartinfo):
        '''
        新建部门
        '''
        try:
            returnList = []
            depId = share_client.Usrm_AddDepartment(adddepartinfo)
            returnList.append('success')
            returnList.append(depId)
            return returnList
        except Exception, e:
            returnList.append('get an exception')
            return returnList


###########################################
# 6、用户登录访问控制
###########################################

    def Usrm_AddNetAccessorsInfo(self, ip, subNetMask):
        '''
        添加用户网段设置
        '''
        try:
            netAccessorsInfo = ncTNetAccessorsInfo()
            netAccessorsInfo.id=''
            net = ncTNetInfo()
            net.ip = ip
            net.subNetMask = subNetMask
            netAccessorsInfo.net=net
            netAccessorsInfo.accessors=[]
            re = share_client.Usrm_AddNetAccessorsInfo(netAccessorsInfo)
            return "success",re
        except Exception, e:
            return "get an exception", e

    def Usrm_EditNetAccessorsInfo(self ,accessorsList, netId, netIp, subNetMask):
        '''
        编辑用户网段设置
        '''
        try:
            netAccessorsInfo = ncTNetAccessorsInfo()
            netAccessorsInfo.accessors=accessorsList
            netAccessorsInfo.id=netId
            net = ncTNetInfo()
            net.id = ''
            net.ip = netIp
            net.subNetMask = subNetMask
            netAccessorsInfo.net=net           
            re = share_client.Usrm_EditNetAccessorsInfo(netAccessorsInfo)
            return "success",re
        except Exception, e:
            return "get an exception", e

    def Usrm_GetNet(self):
        '''
        获取网段设置信息
        '''
        try:
            re = share_client.Usrm_GetNet()
            return "success", re[0].id , re
        except Exception, e:
            return "get an exception" ,e

    def Usrm_DeleteNetAccessorsInfo(self, netAccessorsId):
        '''
        删除用户网段设置
        '''
        try:
            re= share_client.Usrm_DeleteNetAccessorsInfo(netAccessorsId)
            return "success", re
        except Exception, e:
            return "get an exception" ,e
 



if __name__ == '__main__':
    sharemgnt=ShareMgnt_Thrift()
    sharemgnt.shareMgnt_setup("192.168.136.134", '9600')
    # sharemgnt.initEnvironment()
    re = sharemgnt.Usrm_AddNetAccessorsInfo("192.168.245.55", "255.255.255.0")
    print re
    sharemgnt.shareMgnt_teardown
    # sharemgnt=ShareMgnt_Thrift()
    # sharemgnt.shareMgnt_setup("192.168.137.211", '9600')
    # re=sharemgnt.createOrg()
    # print re
    # depId0=re[0][1]
    # depId1=re[1][1]
    # for x in xrange(2):
    #     sharemgnt.Add_User("test"+str(x), "test"+str(x)+"@eisoo.com",[depId0])
    # for x in xrange(2,4):
    #     sharemgnt.Add_User("test"+str(x), "test"+str(x)+"@eisoo.com",[depId1])
    # sharemgnt.shareMgnt_teardown
