#!/usr/local/bin/python2
import cgi
import cgitb
import json
import dbmanager
import os
import datetime
import hashlib
import math
import syslog
from xml.dom.minidom import *

cgitb.enable(format='text')
operator = 17
legal_ip = "93.183.196.26"
dbmanager.init()

####errno : 1 - unknown user
####errno : 2 - error making payment
####errno : 3 - transaction exists
####errno : 4 - transaction not exists
####errno : 5 - bad chacksum

def process(xml_data):
    syslog.syslog('Processing started')
    dt = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    aResult = ""
    xml = parseString(xml_data)
    check = xml.getElementsByTagName('Check')
    pay = xml.getElementsByTagName('Payment')
    confirm = xml.getElementsByTagName('Confirm')
    syslog.syslog(syslog.LOG_DEBUG,xml_data)
    if(check != []):
        service_id = xml.getElementsByTagName('ServiceId')[0]
        account = xml.getElementsByTagName('Account')[0].firstChild.nodeValue
        #print account.nodeValue
        uid = dbmanager.get_uid_by_login(account)
        result = dbmanager.check_user(uid)
        if (result['result'] == 'ok'):
            deposit = dbmanager.get_deposit(uid)
        #print result
        if(result['result'] == 'ok'):
            aResult = """
            <Response>
                <StatusCode>0</StatusCode>
                <StatusDetail>Ok</StatusDetail>
                <DateTime>%(dt)s</DateTime>
                <AccountInfo>
                <Name>%(fio)s</Name>
                <Address>%(addr)s</Address>
                <Balance>%(deposit)2g</Balance>
                <Account>%(account)s</Account>
                </AccountInfo>
            </Response>""" % {'fio':result['fio'],'addr':result['addr'],'deposit':math.floor(deposit),'dt':dt,'account':str(account)}
        else:
            aResult = """
            <Response>
                <StatusCode>-1</StatusCode>
                <StatusDetail>%(result)s</StatusDetail>
            </Response>""" % {'result':result['status']}
    elif(pay != []):
        service_id = int(xml.getElementsByTagName('ServiceId')[0].firstChild.nodeValue)
        account = xml.getElementsByTagName('Account')[0].firstChild.nodeValue
        pkey = xml.getElementsByTagName('OrderId')[0].firstChild.nodeValue
        summ = float(xml.getElementsByTagName('Amount')[0].firstChild.nodeValue)
        datt = xml.getElementsByTagName('DateTime')[0].firstChild.nodeValue
        ip = os.environ['REMOTE_ADDR']
        uid = dbmanager.get_uid_by_login(account)
        result = dbmanager.pay_order(uid,operator,summ,pkey,ip,datt)
        if(result['result'] == 'ok'):
            aResult = """
                <Response>
                    <StatusCode>0</StatusCode>
                    <StatusDetail>Order Created</StatusDetail>
                    <DateTime>%(dt)s</DateTime>
                    <PaymentId>%(tid)s</PaymentId>
                </Response>""" % {'dt':dt,'tid':pkey}
        else:
            aResult = """
                <Response>
                    <StatusCode>-1</StatusCode>
                    <StatusDetail>%(result)s</StatusDetail>
                </Response>""" % {'result':result['status']}
    elif( confirm != []):
        service_id = int(xml.getElementsByTagName('ServiceId')[0].firstChild.nodeValue)
        payment_id = xml.getElementsByTagName('PaymentId')[0].firstChild.nodeValue
        result = dbmanager.confirm_order(payment_id)
        if(result['result'] == 'ok'):
            aResult = """
                <Response>
                    <StatusCode>0</StatusCode>
                    <StatusDetail>Confirmed</StatusDetail>
                    <DateTime>%(dt)s</DateTime>
                    <OrderDate>%(ddt)s</OrderDate>
                </Response>""" % {'dt':dt,'ddt':result['date']}
        else:
            aResult = """
                <Response>
                    <StatusCode>-1</StatusCode>
                    <StatusDetail>%(status)s</StatusDetail>
                    <DateTime>%(dt)s</DateTime>
                    <OrderDate>%(ddt)s</OrderDate>
                </Response>""" % {'dt':dt,'status':result['status'],'ddt':result['date']}
    syslog.syslog(syslog.LOG_DEBUG,aResult)
    return aResult

print "Content-type: text/xml\n";
storage = cgi.FieldStorage()
xml_data = storage.file.read()
ip = os.environ['REMOTE_ADDR']
if(ip == legal_ip): 
    aResult = process(xml_data)
print aResult

