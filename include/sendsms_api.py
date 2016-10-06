#!/bin/env python
#-*-coding:utf-8-*-
import os
import sys
import time
import string
import ast
import requests
reload(sys) 
sys.setdefaultencoding('utf8')
import ConfigParser

def send_sms(sms_to_list,sms_msg,db_type,application,host,port,level,alarm_item,alarm_value,message):
    '''
    sms_to_list:发给谁
    sms_msg:短信内容
    sms_msg='['+level+'] '+db_type+'-'+tags+'-'+server+' '+message+' Time:'+create_time.strftime('%Y-%m-%d %H:%M:%S')
    sms_to_list_comma:多个短信接收者，用逗号拼接
    sms_to_list_semicolon:多个短信接收者，用分号拼接
    sms_to_list_comma = ",".join(sms_to_list)
    sms_to_list_semicolon = ";".join(sms_to_list)
    payload = {'mobiles':sms_to_list_comma,'content':sms_msg}
    '''
    sms_msg = sms_msg+'[Lepus]'
    arr = sms_to_list.split(',')
    try:
        for i in arr:
            payload = {'mobiles':i,'content':sms_msg}
            try:
                r = requests.post('http://service-sms.d.pa.com/interface/send/costom.html',data=payload)
            except Exception, e:
                print str(e)
        return True
    except Exception, e:
        print str(e)
        return False

