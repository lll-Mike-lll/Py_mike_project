# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 05:47:31 2018

@author: MIKE
"""
import mysql.connector

def se_db(name):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='pystock')
    cur = conn.cursor()
    sql = "SELECT * FROM "+name+" ORDER BY id"
    cur.execute(sql)
    row_db  = cur.fetchall()
    print(row_db)
    print(type(row_db))
    n = len(row_db)
    print(len(row_db))
    for i in range(8):
        if i==0:
            print('oldest')
        print(row_db[0][i])
    for i in range(8):
        if i==0:
            print('newest')
        print(row_db[n-1][i])
    return row_db
    
    
data_fet = se_db(input('name: '))
print(type(data_fet))

