"""Raw operations on abills database"""

import MySQLdb as mdb
import datetime

_CFG = {
    'host':'localhost',
    'user':'abills',
    'pwd':'osipenkoNETltd',
    'db':'abills'
}
_DB = None

def init():
    """Init database conection"""
    global _DB
    _DB = mdb.connect(_CFG['host'], _CFG['user'], _CFG['pwd'], _CFG['db'])
    cur = _DB.cursor()
    cur.execute("SET NAMES utf8")
    cur.execute("SET AUTOCOMMIT=1")
    return cur.fetchone()
    
def get_address(id):
    if  id == 0:
        return None
    else:
        cur = _DB.cursor()
        sql = """SELECT d.id AS district_id, 
                 d.city, 
      		d.name AS address_district, 
      		s.name AS address_street, 
      		b.number AS address_build,
      		s.id AS street_id
     		FROM builds b
     		LEFT JOIN streets s  ON (s.id=b.street_id)
     		LEFT JOIN districts d  ON (d.id=s.district_id)
     		WHERE b.id= %s
 		""" 
        if cur.execute(sql % id) != 0 :
            data = cur.fetchone()
            return '%s, %s, %s'  % (data[2],data[3],data[4])

def check_user(uid):
    """Checking users + return some information"""
    cur = _DB.cursor()
    sql = """
    SELECT 
        id,
        u.uid,
        gid,
        fio,
        phone,
        location_id
    FROM users u, users_pi upi WHERE upi.uid = u.uid AND u.uid = %s """
    if cur.execute(sql % uid) != None :
        data = cur.fetchone()
        if data is not None:
            return {
                        'result':'ok',
                        'id':data[1],
                        'uid':data[1],
                        'gid':data[2],
                        'fio':data[3],
                        'phone':data[4],
                        'addr': get_address(data[5]),
                   }

        else:
           return {'result':'error', 'errno':1, 'status':'unknown user'}
    else:
        return {'result':'error', 'errno':1, 'status':'unknown user'}

def get_deposit(uid):
    """Get user deposit by UID"""
    sql = "SELECT deposit FROM bills WHERE uid= %s "
    cur = _DB.cursor()
    cur.execute(sql % uid)
    data = cur.fetchone()
    return data[0]

def get_deposit2(billid):
    """Get user deposit by BILL_ID"""
    sql = "SELECT deposit FROM bills WHERE id = %s"
    cur = _DB.cursor()
    cur.execute(sql, billid)
    data = cur.fetchone()
    if data  is None:
        sql = "SELECT deposit FROM bills WHERE uid = %s"
        cur = _DB.cursor()
        cur.execute(sql, billid)
        data = cur.fetchone()
    return data[0]

def set_deposit(uid, deposit):
    """Set user deposit by UID"""
    sql = "UPDATE bills SET deposit = %s WHERE uid = %s"
    cur = _DB.cursor()
    return cur.execute(sql, (deposit, uid))

def get_operator_balance(aid):
    """ Operator balance for Unipay protocol. The data is stored in email field of the DB"""
    sql = "SELECT email FROM admins WHERE aid = %s "
    cur = _DB.cursor()
    cur.execute(sql, aid)
    data = cur.fetchone()
    return float(data[0]) if data[0] != '' else 0

def set_operator_balance(aid, balance):
    """ Updates operator balance for Unipay protocol. The data is stored in email field of the DB"""
    sql = "UPDATE admins SET email = %s WHERE aid = %s "
    cur = _DB.cursor()
    cur.execute(sql, (str(balance), aid, ))

def get_uid(billid):
    """Get user UID by BILL_ID"""
    sql = "SELECT uid FROM users WHERE bill_id = %s"
    cur = _DB.cursor()
    cur.execute(sql, billid)
    data = cur.fetchone()
    if data  is None:
        sql = "SELECT uid FROM users WHERE uid = %s"
        cur = _DB.cursor()
        cur.execute(sql, billid)
        data = cur.fetchone()
    return data[0]

def get_uid_by_login(login):
    """Get user UID by LOGIN"""
    sql = "SELECT uid FROM users WHERE id = '%s' "
    cur = _DB.cursor()
    cur.execute(sql % login)
    data = cur.fetchone()
    return data[0]
    if data  is None:
       return -1

def get_dv_status(uid):
    """Set user dv_status by UID"""
    sql = "SELECT disable  FROM dv_main WHERE uid = '%s'" % uid
    cur = _DB.cursor()
    cur.execute(sql)
    data = cur.fetchone()
    return data[0]

def set_dv_status(uid):
    """Set user dv_status by UID"""
    sql = "UPDATE dv_main SET disable = 0 WHERE uid = %s" % uid
    cur = _DB.cursor()
    cur.execute(sql)

def get_abon_fees(uid):
    """Get user tarif fees UID float(summa-(summa*data[0]/100))"""
    sql = "SELECT tarif_plans.month_fee  FROM tarif_plans, dv_main WHERE dv_main.tp_id=tarif_plans.id AND dv_main.uid= '%s'" % uid
    cur = _DB.cursor()
    cur.execute(sql)
    data = cur.fetchone()
    summa=data[0]
    sql = "SELECT reduction FROM users WHERE uid= '%s'" % uid
    cur.execute(sql)
    data = cur.fetchone()
    return summa-(summa*data[0]/100)

def check_tid(tid, prefix="tr_id:"):
    """Check transaction """
    sql = """ SELECT count(*) FROM payments WHERE ext_id = '%s' """
    cur = _DB.cursor()
    if cur.execute(sql % ('tr_id:' + str(tid))) != 0:
        data = cur.fetchone()
        if data[0] != 0:
            return {'result':'ok', 'tid-count':data[0]}
        else:
            return {'result':'error', 'tid-count':data[0], 'errno':3}
    else:
        return {'result':'erorr', 'status':'db_error', 'errno':2}

def get_billid(uid):
    sql = """ select bill_id from users where uid = %s """
    cur = _DB.cursor()
    cur.execute(sql)
    data = cur.fetchone()
    return data[0]

def pay_order(uid, operator, summ, tid, ip_addr, datt=None):
    billid = uid
    deposit = get_deposit(uid)
    if datt == None:
        pay_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        pay_date = datt
    sql = """INSERT INTO payments(bill_id,method,uid,date,sum,amount,last_deposit,
                                  ext_id,inner_describe,aid,ip,reg_date,currency)
              values (%s, 10, %s, %s, %s, %s, %s, %s, %s, %s, INET_ATON(%s), %s, '0')"""
    cur = _DB.cursor()
    if cur.execute(sql, (billid, uid, pay_date, 0, 0, deposit, str(tid), summ, operator, ip_addr, pay_date)) == 1:
        return {'result':'ok'}
    else:
        return {'result':'error', 'status':'fatal', 'errno':2}

def confirm_order(order_id):
    sql = "SELECT inner_describe,date,uid,sum FROM payments WHERE ext_id = '%s' "
    cur = _DB.cursor()
    if cur.execute(sql % order_id) != 0:
        row = cur.fetchone()
        summ = float(row[0])
        pay_date = str(row[1])
        uid = row[2]
        real_sum = float(row[3])
        deposit = get_deposit(uid)
        set_deposit(uid, deposit + summ)
        sql = "UPDATE payments SET sum = %s, amount = %s WHERE ext_id = %s"
        cur.execute(sql, (summ, summ, str(order_id)))
        if get_dv_status(uid) == 5:
            set_dv_status(uid)
            suma = get_abon_fees(uid)
            if suma > 0:
                fees_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                deposit = get_deposit(uid)
                sql = """INSERT INTO fees(date,sum,last_deposit,uid,aid,bill_id,dsc) VALUES (%s ,%s, %s, %s, %s, %s, %s)"""
                cur = _DB.cursor()
                cur.execute(sql, (fees_date,suma,deposit,uid,1,uid,'abonplata_easypay'))
                set_deposit(uid, deposit - suma)
                return {'result':'ok', 'date':pay_date, 'status':'ok'}
            else:
                return {'result':'ok', 'date':pay_date, 'status':'ok'}
        else:
            return {'result':'ok', 'date':pay_date, 'status':'ok'}
    else:
        return {'result':'error', 'status':'tid check error', 'date':''}

#init()
#uid = 300
#data = check_user(uid)
#print data
#print "checkuser: ",data
#print "deposit", get_deposit(uid)
#print "deposit", set_billid(uid)
#print pay('4',65,15,65.01,32113333,'192.168.0.1')
#print set_deposit(uid,1.01)
#print confirm_order(144)
#print check_tid(143)
