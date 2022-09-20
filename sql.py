from re import S
from unicodedata import category
import pymysql as p
 
def getconnection():
   
    return p.connect(host="localhost",user="root",password="",database="ayurveda")
 
 
#insert record
def insertrec(t):
    db=getconnection()
    cr=db.cursor()
    sql="insert into medicine values(%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    print(t)
    db.commit()
    db.close()
#edit record
def updaterec(t):
    db=getconnection()
    cr=db.cursor()
    sql="update medicine set id=%s,category=%s,problem=%s,details=%s,image=%s,link=%s where id=%s"
    cr.execute(sql,t)
    db.commit()
    db.close()
 
 
#display record
def displayrec():
    db=getconnection()
    cr=db.cursor()
    sql="select * from medicine"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
 
#delete record 
def deleterec(id):
    db=getconnection()
    cr=db.cursor()
    sql="delete from medicine where id=%s"
    cr.execute(sql,id)
    db.commit()
    db.close()
 
 
 
#select record
def selectr(id):
    db=getconnection()
    cr=db.cursor()
    sql="select * from medicine where id=%s"
    cr.execute(sql,id)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data[0]


#display category
def displayrec1(category):
    db=getconnection()
    cr=db.cursor()
    sql="select * from medicine where category=%s"
    cr.execute(sql,category)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
