#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
概述：
1、EACP初始化与关闭
2、设备管理
3、文档库
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from EThriftException.ttypes import *
from EACP import ncTEACP
from EACP.ttypes import *
from EACP.constants import *


class EACP_Thrift():
# ##########################################
# 1、EACP初始化与关闭
###########################################

    def eacp_setup(self, ip, port):
        try:
            global eacp_transport
            global eacp_client
            eacp_transport = TSocket.TSocket(ip, port)
            eacp_transport = TTransport.TBufferedTransport(eacp_transport)
            eacp_protocol = TBinaryProtocol.TBinaryProtocol(eacp_transport)
            eacp_client = ncTEACP.Client(eacp_protocol)
            eacp_transport.open()
        except Exception, e:
            print 'get an exception', e

    def eacp_teardown(self):
        eacp_transport.close()

# ##########################################
# 2、设备管理
###########################################

    def EACP_AddDevice(self,userId, udid ,osType):
        '''
        添加设备信息
        * @param userId:           用户id
        * @param udid:             设备唯一标识码
        * @param deviceType:       设备类型
        * @ret:                    无返回
        '''
        try:
            re = eacp_client.EACP_AddDevice(userId, udid, osType)
            return "success", re
        except Exception, e:
            return "get an exception" ,e

    def EACP_DeleteDevice(self, userId,udid ):
        '''
        删除设备信息
        * @param userId:           用户id
        * @param udid:             设备唯一标识码
        * @ret:                    无返回
        '''
        try:
            re = eacp_client.EACP_DeleteDevice(userId, udid)
            return "success", re
        except Exception, e:
            return "get an exception" ,e

    def EACP_EnableDevice(self, userId, udid):
        '''
        启用设备
        * @param userId:           用户id
        * @param udid:             设备唯一标识码
        * @ret:                    无返回
        '''
        try:
            re = eacp_client.EACP_EnableDevice(userId, udid)
            return "success", re
        except Exception, e:
            return "get an exception" ,e

    def EACP_DisableDevice(self, userId, udid):
        '''
        禁用设备
        * @param userId:           用户id
        * @param udid:             设备唯一标识码
        * @ret:                    无返回
        '''
        try:
            re = eacp_client.EACP_DisableDevice(userId, udid)
            return "success", re
        except Exception, e:
            return "get an exception" ,e

    def EACP_GetDevicesByUserId(self ,userId):
        '''
        获取用户的设备信息
        '''
        try:
            re = eacp_client.EACP_GetDevicesByUserId(userId)
            return "success", re[0].baseInfo.udid,re
        except Exception, e:
            return "get an exception" ,e

# ##########################################
# 3、文档库
############################################

    def EACP_AddCustomDoc(self,name, typeName, ownerIds,spaceQuota=214748364800,createrId='266c6a42-6131-4d62-8f39-853e7093701c'):
        '''
        创建文档库
        '''
        try:
            Info = ncTAddCustomDocParam()

            Info.name=name
            Info.typeName=typeName
            Info.createrId=createrId
            Info.ownerIds=ownerIds
            Info.spaceQuota=spaceQuota
            Info.createrId=createrId
            re = eacp_client.EACP_AddCustomDoc(Info)
            return "success",re 
        except Exception, e:
            return "get an exception", e



if __name__ == '__main__':
    eacp = EACP_Thrift()
    eacp.eacp_setup("192.168.136.134",9992)
    # eacp.EACP_AddDevice("b8096602-acd6-11e7-92e2-643e8cb593de","00-00-00-00-00-D0",5)
    # eacp.EACP_DeleteDevice("b8096602-acd6-11e7-92e2-643e8cb593de","00-00-00-00-00-D0")
    # re = eacp.EACP_GetDevicesByUserId("b8096602-acd6-11e7-92e2-643e8cb593de")
    # print re[1]
    # re = eacp.EACP_EnableDevice("b8096602-acd6-11e7-92e2-643e8cb593de", "98-5A-EB-DF-99-E3")
    # print re
    ownerIds=[]
    ownerIds.append("650ba17c-afdd-11e7-bd70-643e8cb593de")
    re = eacp.EACP_AddCustomDoc("AnyShare研发部","部门文档",ownerIds)
    #re = eacp.EACP_AddCustomDoc("AnyShar","dep",ownerIds)
    print re

    eacp.eacp_teardown()
