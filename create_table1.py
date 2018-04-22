# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:55:17 2018

@author: MIKE
"""

import mysql.connector

def conn_db(name):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='pystock')
    a = conn.cursor()
    sql = "CREATE TABLE "+name+"(id INT PRIMARY KEY,date text, open text,max text,min text,close text,vol text,val text)"
#    sql = "INSERT INTO mike_1(id,name) VALUES(%s,%s)"
#    num = 3
#    add_db = (num,'pp')
#    a.execute(sql,add_db)
    a.execute(sql)
    conn.commit()
    conn.close()
    
conn_db(input('name stock:'))