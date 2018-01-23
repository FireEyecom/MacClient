#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from eisoo.tclients import TClient
from NetAgent.ttypes import ncTIfAddr

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from ShareMgnt import ncTShareMgnt
from ShareMgnt.ttypes import *
from ShareMgnt.constants import *

def sharemgnt_init(ip):
    try:
        global share_transport
        global share_client
        share_transport = TSocket.TSocket(ip,9600)
        share_transport = TTransport.TBufferedTransport(share_transport)
        share_protocol = TBinaryProtocol.TBinaryProtocol(share_transport)
        share_client = ncTShareMgnt.Client(share_protocol)
        share_transport.open()

    except Exception as e:
        return e
def sharemgnt_teardown():
    try:
        share_transport.close()
    except Exception as e:
        return e

def Ifaddr(ipaddr, netmask, gateway, nic_dev_name, label):
    """
   构造网络结构体
    """
    if_info = ncTIfAddr()
    if_info.ipaddr = ipaddr
    if_info.netmask = netmask
    if_info.gateway = gateway
    if_info.nic_dev_name = nic_dev_name
    if_info.label = label
    return if_info

def active_cluster(ip, inner_vip, outer_vip, iptables, node_ipaddr, node_alias):
    """
    激活集群
    """
    with TClient('DeployManager', ip) as client:
        print "Active node %s" % ip
        client.active_cluster_complete(inner_vip, outer_vip, iptables, node_ipaddr, node_alias)

def init_storage_pool(ip, replicas):
    """
    初始化存储池
    """
    with TClient('StorageManager', ip) as client:
        print "init cluster storage pool, replicas %s" % replicas
        client.init_storage_pool(int(replicas))

def add_node_to_storage_pool(ip, inner_rip):
    """
    添加节点设备到存储池
    """
    with TClient('StorageManager', ip) as client:
        print "Add node %s all disk to storage pool" % inner_rip
        client.add_node_devices_to_pool(inner_rip)

def install_solr(ip):
    """
    安装全文检索
    """
    print "安装全文检索".decode("utf-8")
    with TClient("ESearchMgnt", ip) as client:
        client.Setup()

def Licensem_AutoAuthorized(ip):
    '''
    自动授权产品
    '''
    print "自动授权产品".decode("utf-8")
    try:
        sharemgnt_init(ip)
        share_client.Licensem_AutoAuthorized("eisoo.com123")
        sharemgnt_teardown()
        return 'success'
    except Exception, e:
        sharemgnt_teardown()
        print 'get a e error', e
        return 'get an exception'

def Usrm_SetPasswordConfig(ip,strongStatus,expireTime,lockStatus,passwdErrCnt,passwdLockTime):
    """
    设置用户密码配置信息
    """
    print "设置用户密码配置信息".decode("utf-8")
    try:
        sharemgnt_init(ip)
        passwdConfig=ncTUsrmPasswordConfig()
        passwdConfig.strongStatus=strongStatus
        passwdConfig.expireTime=expireTime
        passwdConfig.lockStatus=lockStatus
        passwdConfig.passwdErrCnt=passwdErrCnt
        passwdConfig.passwdLockTime=passwdLockTime
        re = share_client.Usrm_SetPasswordConfig(passwdConfig)
        sharemgnt_teardown()
        return "success",re
        
    except Exception as e:
        sharemgnt_teardown()
        return "get an exception",e

def InitCSFLevels(ip,csflevels):
    """
    初始化密级枚举
    """
    print "初始化密级枚举".decode("utf-8")
    try:
        sharemgnt_init(ip)
        re = share_client.InitCSFLevels(csflevels)
        sharemgnt_teardown()
        return "success",re
    except Exception as e:
        sharemgnt_teardown()
        return "get an exception",e

def Usrm_InitSystem(ip):
    """
    初始化系统
    """
    print "初始化系统".decode("utf-8")
    try:
        sharemgnt_init(ip)
        re = share_client.Usrm_InitSystem()
        sharemgnt_teardown()
        return "success",re
    except Exception as e:
        sharemgnt_teardown()
        return "get an exception",e

def SetSysCSFLevel(ip,level):
    """
    设置系统密级
    """
    print "设置系统密级".decode("utf-8")
    try:
        sharemgnt_init(ip)
        re = share_client.SetSysCSFLevel(level)
        sharemgnt_teardown()
        return "success",re
    except Exception as e:
        sharemgnt_teardown()
        return "get an exception",e



if __name__ == '__main__':
    inner_vip = Ifaddr("6.5.4.9", "255.255.255.0","", "eth0", "")
    outer_vip = Ifaddr("192.168.137.211", "255.255.255.0", "", "eth0", "")
    active_cluster("192.168.137.210", inner_vip, outer_vip, False, "6.5.4.8", "")
    init_storage_pool("192.168.137.210", 1)
    add_node_to_storage_pool("192.168.137.210", "6.5.4.8")
    install_solr("192.168.137.210")
    re = Licensem_AutoAuthorized("192.168.137.211")
    print re
    #初始化配置
    re = Usrm_SetPasswordConfig("192.168.137.211",False,-1,False,3,60)
    print re
    re = InitCSFLevels("192.168.137.211",["非密", "内部", "秘密", "机密"])
    print re
    re = Usrm_InitSystem("192.168.137.211")
    print re
    re = SetSysCSFLevel("192.168.137.211",5)
    print re

