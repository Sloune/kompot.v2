#!/usr/local/bin/python2
# -- coding: utf-8 --
import cgi
import cgitb
import json
import db
import os
import datetime
import hashlib
import math
import sys
from datetime import datetime
import time
from subprocess import Popen, PIPE
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config")
persent_commission = config.get('liqpay','commission')
key = config.get('liqpay','public_key')
your_site = config.get('liqpay','your_site')
server_url = config.get('liqpay','server_url')
remote_ipaddr1 = config.get('liqpay','remote_ipaddr1')
remote_ipaddr2 = config.get('liqpay','remote_ipaddr2')

remote_ipaddr = os.environ["REMOTE_ADDR"]

cgitb.enable()
date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
Info_Client=dict()
Answer_Liqpay=dict()
form = cgi.FieldStorage()

if (form.getvalue('action') is not None and form.getvalue('login') is not None and form.getvalue('summ')) :

  if form.getvalue('action') ==  'check' :
    Info_Client['server'] = db.check_user(form.getvalue('login'))
    Info_Client['login'] = form.getvalue('login')
    commission = float(form.getvalue('summ')) / 100 * float(persent_commission) + float(form.getvalue('summ')) / 100 * float(persent_commission)  /100 * float(persent_commission)
    Info_Client['summ'] = float(form.getvalue('summ')) + commission
    Info_Client['summ'] = float(form.getvalue('summ')) + commission + 0.01
    url="""https://www.liqpay.ua/api/pay?public_key=%s\
&amount=%s&currency=UAH\
&description=%s\
&type=buy&pay_way=card,delayed\
&language=ru\
&server_url=http://%s""" % ( key, Info_Client['summ'], Info_Client['login'], server_url)
    aResult="""Content-type: text/html \n\n
                       <!DOCTYPE html>
                       <head>
                       <meta http-equiv="refresh" content="0; url=%s" />
                       <html>
                       </head>
                       <body>
                       </body>
                       </html>""" % url
    print aResult

  else:
    if form.getvalue('action') ==  'confirm' :
      if db.check_user(form.getvalue('login')) != '100':
        User_Detail = db.get_user_detail(form.getvalue('login'))
        if db.get_dv_status(db.get_uid(form.getvalue('login'))) ==0:
          Amount_Detail = float(db.get_user_amount(form.getvalue('login')))
        else:
          Amount_Detail = float(db.get_user_amount(form.getvalue('login')))-float(db.get_abon_fees(db.get_uid(form.getvalue('login'))))
        Pay_Detail = float(form.getvalue('summ'))
        aResult= """Content-type: text/html; charset=utf-8\n
                       <!DOCTYPE html>
                       <head>
                       <html>
                       </head>
                       <body>
                       <h1>Логін: %s<h1>
                       <h1>Дані користувача: %s<h1>
                       <h1>Стан рахунку: %.2f грн.<h1>
                       <h1>Сума поповнення: %.0f грн.<h1>
                       <form method="POST" accept-charset="utf-8" action="http://%s">
                       <input type="hidden" name="action" value="check">
                       <input type="hidden" name="login" value=%s>
                       <input type="hidden" name="summ" value=%s>
                       <br>
                       <input type=image src="//static.liqpay.ua/buttons/p1ru.radius.png" name="btn_text">
                       </br>
                       </form>
                       </body>
                       </html>""" % (form.getvalue('login'), User_Detail, Amount_Detail, Pay_Detail, server_url, form.getvalue('login'), form.getvalue('summ'))
        print aResult
      else:
        aResult= """Content-type: text/html; charset=utf-8 \n\n
                   <!DOCTYPE html>
                   <head>
                   <meta http-equiv="refresh" content="3; url=http://%s" />
                   <html>
                   </head>
                   <body>
                   <h1>Такого користувача не існує<h1>
                   </body>
                   </html>"""  % your_site
        print aResult      

elif (form.getvalue('status') == 'success' and (remote_ipaddr == remote_ipaddr1 or remote_ipaddr == remote_ipaddr2 )) :
  payfile='/usr/abills/payments/liqpay/Liqpay' + datetime.now().strftime("%Y-%m-%d")
  if os.path.isfile(payfile) != True: 
    Popen('/usr/bin/touch %s' % payfile, shell=True, stdout=PIPE).communicate()
  commission = float(form['amount'].value) / 100 * float(persent_commission)
  report='\n %s		%s		%s		%s		%s	%s		' % (form['sender_phone'].value,\
  form['description'].value,  form['amount'].value, commission,  form['order_id'].value, form['status'].value)
  paysumm=float(form['amount'].value) - commission
  server = db.check_user(form['description'].value)
  f=open(payfile,'a')
  f.write(str(report))
  f.close()
  db.pay(form['description'].value,9, paysumm, form['order_id'].value, '127.0.0.1', datt=None)
  aResult= """Content-type: text/html \n\n <!DOCTYPE html><head><html></head><body><h1>ok<h1></body></html>"""
  print aResult

else:
  aResult= """Content-type: text/html \n\n <!DOCTYPE html><head><html></head><body><h1>No any keys define<h1></body></html>"""
  print aResult
