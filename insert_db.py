# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 11:11:44 2018

@author: MIKE
"""

import mysql.connector

def conn_db(n,a1,a2,a3,a4,a5,a6,a7):
#def conn_db():
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='pystock')
    a = conn.cursor()
#    sql = "CREATE TABLE "+name+"(id INT PRIMARY KEY,date text, open text,max text,min text,close text,vol text,val text)"
    sql = "INSERT INTO ptt(id,date,open,max,min,close,vol,val) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
#    num = 1
#    add_db = (num,'pp','pp','pp','pp','pp','pp','pp')
    add_db = (n,a1,a2,a3,a4,a5,a6,a7)
    a.execute(sql,add_db)
#    a.execute(sql)
    conn.commit()
    conn.close()
    
#conn_db(input('name stock:'))
#conn_db()
conn_db(2,'pp','pp','pp','pp','pp','pp','pp')