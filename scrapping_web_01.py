# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:50:05 2018

@author: wuttinun_r
"""
import mysql.connector
import pandas as pan
def inp(a):
    
    url = 'http://www.panphol.com/data/page/stockprice/'+a+'#'
    data = pan.read_html(url)
    return data


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
    
def conn_db2(name,n,a1,a2,a3,a4,a5,a6,a7):
#def conn_db():
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='pystock')
    a = conn.cursor()
#    sql = "CREATE TABLE "+name+"(id INT PRIMARY KEY,date text, open text,max text,min text,close text,vol text,val text)"
    sql = "INSERT INTO "+name+"(id,date,open,max,min,close,vol,val) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
#    num = 1
#    add_db = (num,'pp','pp','pp','pp','pp','pp','pp')
    add_db = (n,a1,a2,a3,a4,a5,a6,a7)
    a.execute(sql,add_db)
#    a.execute(sql)
    conn.commit()
    conn.close()
    
#conn_db(input('name stock:'))
#conn_db()

    
name = input('name: ')
data_stock = inp(name)
print(type(data_stock))
data_stock_db = tuple(data_stock)
print(type(data_stock_db))
inp(name)
conn_db(name)
nrow = len(data_stock[0])
data_list1 = []
data_list2 = []
data_list3 = []
data_list4 = []
data_list5 = []
data_list6 = []
data_list7 = []
for j in range(nrow):
    data_list1.append(data_stock[0].iloc[j,0])
    data_list2.append(data_stock[0].iloc[j,1])
    data_list3.append(data_stock[0].iloc[j,2])
    data_list4.append(data_stock[0].iloc[j,3])
    data_list5.append(data_stock[0].iloc[j,4])
    data_list6.append(data_stock[0].iloc[j,7])
    data_list7.append(data_stock[0].iloc[j,8])

#print(data_list)
for i in range(nrow):
    conn_db2(name,i,data_list1[i],'pp','pp','pp','pp','pp','pp')

#a = input('code (#0 for all),(#1 for each): ')
#if a == '0':
#    print('all')
#elif a=='1':
#    print('each')
#    while True:
#        b=input('name stock (if need to stop put #0):')
#        if b!='0':
#            print(b)
#            print(inp(b))
#        else:
#            print('End program')
#            break


