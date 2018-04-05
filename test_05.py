# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 20:32:33 2018

@author: MIKE
"""

import pymysql
connection = pymysql.connect(host='localhost',user='root',password='',db='test1')
a = connection.cursor()
sql = 'SELECT * from `aot`;'
a.execute(sql)
countrow = a.execute(sql)
print("Number of row:",countrow)
data = a.fetchall()
print(type(data))
print(data[0][0])
datalist = list(data)
print(datalist)
#print(data)

#for row in a:
   #print(row[0])
   #print(row[2])
   
