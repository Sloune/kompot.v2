# -- coding: utf-8 --
import MySQLdb as mdb
import datetime
import sys
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config")
host = config.get('mysql','host')
user = config.get('mysql','user')
dbname = config.get('mysql','dbname')
password = config.get('mysql','password')

try:
    db = mdb.connect(host,user,password,dbname)
    db.autocommit(True)
    cursor = db.cursor()
except:
    print "Error Connect To MysqlDB"
 


def check_user(login):
    sql = """select id from users where id = '%s' """ % login
    if cursor.execute(sql) !=0:
        return 1
        sys.exit(0)
    else:
         return "100"

def get_user_detail(login):
    sql = """SELECT fio FROM users_pi, users,bills WHERE users_pi.uid=users.uid AND bills.uid=users.uid AND users.id = '%s' """ % login
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[0]

def get_user_amount(login):
    sql = """SELECT deposit FROM users,bills WHERE bills.uid=users.uid AND users.id = '%s' """ % login
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[0]

def get_uid(billid):
    sql = "SELECT uid FROM users WHERE id = '%s'" % billid
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[0]

def get_bills_id(billid):
    uid=get_uid(billid)
    sql = "SELECT id FROM bills WHERE uid = '%s'" % uid
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[0]

def get_deposit(billid):
    uid=get_uid(billid)
    sql = "SELECT deposit FROM bills WHERE uid = %s"  % uid
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[0]

def set_deposit(uid, deposit):
    """Set user deposit by UID"""
    sql = "UPDATE bills SET deposit = %s WHERE uid = %s" % (deposit, uid)
    return cursor.execute(sql)
    cursor.commit()

def get_abon_fees(uid):
    """Get user tarif fees UID float(summa-(summa*data[0]/100))"""    
    sql = "SELECT tarif_plans.month_fee  FROM tarif_plans, dv_main WHERE dv_main.tp_id=tarif_plans.id AND dv_main.uid= '%s'" % uid
    cursor.execute(sql)
    data = cursor.fetchone()
    summa=data[0]
    sql = "SELECT reduction FROM users WHERE uid= '%s'" % uid
    cursor.execute(sql)
    data = cursor.fetchone()
    return summa-(summa*data[0]/100)

def get_dv_status(uid):
    """Set user dv_status by UID"""
    sql = "SELECT disable  FROM dv_main WHERE uid = '%s'" % uid
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[0]  

def set_dv_status(uid, status):
    """Set user dv_status by UID"""
    sql = "UPDATE dv_main SET disable = %s WHERE uid = %s" % (status, uid)
    return cursor.execute(sql)
    cursor.commit()

def check_tid(tid):
    sql = """ SELECT count(*) FROM payments WHERE ext_id = '%s' """
    if cursor.execute(sql % (str(tid))) != 0:
        data = cursor.fetchone()
        if data[0] == 0:
            return {'result':'ok', 'tid-count':data[0]}
        else:
            return {'result':'error', 'tid-count':data[0], 'errno':3}
    else:
        return {'result':'erorr', 'status':'db_error', 'errno':2}

def pay(billid,type, summ, tid, ip_addr, datt=None):
    res_tid = check_tid(tid)
    if  res_tid['result'] == 'error':
        print 'error, error check tid'
        sys.exit(1)
    uid = get_uid(billid)
    deposit = get_deposit(billid)
    if datt == None:
        pay_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        pay_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = """INSERT INTO payments(bill_id,method,uid,date,sum,amount,last_deposit,
                                  ext_id,inner_describe,aid,ip,reg_date,currency)
              VALUES ('%s',%s ,%s, %s, %s, %s, %s, %s, %s, %s, INET_ATON(%s), %s, %s)"""
    operator = config.get('billing', 'operator_id')
    res = cursor.execute(sql, (get_bills_id(billid),type, uid, pay_date, summ, summ, deposit,
                         str(tid), "", operator, ip_addr, pay_date, '0'))
    if res > 0:
      set_deposit(uid, deposit + summ)
      if get_dv_status(uid) == 5:
        set_dv_status(uid, 0)
        suma=get_abon_fees(uid)        
        if suma>0:
            sql = """INSERT INTO fees(date,sum,dsc,ip,last_deposit,uid,aid,bill_id) VALUES (%s ,%s, %s, INET_ATON(%s), %s, %s, %s,%s)"""
            res = cursor.execute(sql, (pay_date, suma, 'Активовано. Зняття місячної абонплати', ip_addr, get_deposit(billid), uid, operator,get_bills_id(billid)))
            set_deposit(uid, get_deposit(billid) - suma)                
      return {'result':'ok'}
    else:
        return {'result':'error', 'status':'fatal', 'errno':2}
