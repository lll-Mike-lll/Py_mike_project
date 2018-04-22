# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:09:35 2018

@author: MIKE
"""


def conn_db(name):
    import pymysql
    conn = pymysql.connect(host = 'localhost', user = 'root', password='',db='pystock')
    a = conn.cursor()
    sql = "CREATE TABLE "+name+"(date text, open text,max text,min text,close text,vol text,val text)"
    a.execute(sql)
    conn.close

#conn_db(input('name:'))

def ins_db():
    import pymysql
    name = 'hub4'
    conn2 = pymysql.connect(host = 'localhost', user = 'root', password='',db='pystock')
    ex = conn2.cursor()
#    sql2 = "INSERT INTO hub4(id, open) VALUES (1, 'hhh3');"
#    sql2 = "CREATE TABLE "+name+"(id int primary key, open text)"
    ex.execute("INSERT INTO hub4(id, open) VALUES (1, 'hhh3');")
    conn2.commit()
    conn2.close()
    print('success')
    
ins_db()