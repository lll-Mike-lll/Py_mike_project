# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 20:32:33 2018

@author: MIKE
"""

import pymysql
connection = pymysql.connect(host='localhost',user='root',password='',db='test1')
a = connection.cursor()
sql = 'SELECT * from `ptt`;'
a.execute(sql)
countrow = a.execute(sql)
print("Number of row:",countrow)
data = a.fetchall()
#print(type(data))
#print(data[0][0])
#datalist = list(data)
#print(datalist[3][2])
#print(datalist[0][0])
ptt_date=[]
for row in data:
#    print(row[1])
    ptt_date.append(row[1])
ptt_close=[]
#print(ptt_date)

for row in data:
    ptt_close.append(float(row[3]))
#print(ptt_close)

#print(len(ptt_close))

sign1 = [20,40,50,60,80,100,105]

for j in sign1:
    print(ptt_close[j])

xa = 100000
xc = ptt_close[sign1[0]]
xb = (xa-(xa%xc))/xc
xd = 
#xd = int(xc)
#
#print(xd)
#xb = float(xc)
print(type(xc))
print(xb)
#print(data)

#for row in a:
   #print(row[0])
   #print(row[2])
   
