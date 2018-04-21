# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:09:35 2018

@author: MIKE
"""
import pymysql

def conn_db(name):
    conn = pymysql.connect(host = 'localhost', user = 'root', password='',db='MIKE_PYTHON',utf8)
    a = conn.cursor()
    sql = "CREATE TABLE "+name+"(date text, open text,max text,min text,close text,vol text,val text)"
    a.execute(sql)
    conn.close

conn_db(input('name:'))