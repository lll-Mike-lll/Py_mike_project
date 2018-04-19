# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 22:48:18 2018

@author: MIKE
"""
#a = '334'
#b = int(a)
#print(b)
import pymysql
connection1 = pymysql.connect(host='localhost',user='root',password='',db='test1')
a = connection1.cursor()
sql = 'SELECT * from `ptt`;'
a.execute(sql)
countrow = a.execute(sql)
print("Number of row:",countrow)
data = a.fetchall()
ptt_date=[]
for row in data:
     ptt_date.append(row[1])
    
ptt_close=[]
for row in data:
    ptt_close.append(float(row[3]))

import pandas as pd
df = pd.read_excel("D:\ptt_data_1.xlsx")
#print(df)
n =len(df)
print(len(df))
print(df.iloc[0,0])
ptt_data_date = []
ptt_data_sign = []
for i in range(n):
    ptt_data_date.append(df.iloc[i,0])
    
for i in range(n):
    ptt_data_sign.append(df.iloc[i,1])
print(ptt_data_date)
print(ptt_data_sign)

print(type(ptt_data_sign))
print(len(ptt_data_date))
print(len(ptt_data_sign))


ptt_sellect_date = []
ptt_sellect_sign = []

print(ptt_data_sign.index(1))
print('xxxx')
check = -1
for i in range(len(ptt_data_date)):
    if ptt_data_sign[i] == (-check):
#        print("%d - %d" % (i , ptt_data_sign[i]))
        ptt_sellect_date.append(ptt_data_date[i])
        ptt_sellect_sign.append(ptt_data_sign[i])
        check = check*(-1)

print(ptt_close)
print(ptt_date)

for i in range(len(ptt_sellect_date)):
    for j in range(len(ptt_date)):
        if ptt_sellect_date[i] == ptt_date[j]:
            print(j)
#print(ptt_sellect_date)
#for i in range(len(ptt_sellect_date))    :    
#   print('{}, {}'.format(ptt_sellect_date[i],ptt_sellect_sign[i]))