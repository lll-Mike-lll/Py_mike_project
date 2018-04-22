# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 08:42:56 2018

@author: MIKE
"""
import mysql.connector

def conn_db():
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='pystock')
    a = conn.cursor()
    #sql = "CREATE TABLE mike_1(id INT PRIMARY KEY,name TEXT)"
    sql = "INSERT INTO mike_1(id,name) VALUES(%s,%s)"
    num = 3
    add_db = (num,'pp')
    a.execute(sql,add_db)
    conn.commit()
    conn.close()
    
conn_db()


