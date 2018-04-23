# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 06:28:57 2018

@author: MIKE
"""
import pandas as pann
data_ex = pann.read_excel("D:\ptt_data_1.xlsx")
print(data_ex)
print(type(data_ex))
print(len(data_ex))

ptt_data_date = []
ptt_data_sign = []
n = len(data_ex)
for i in range(n):
    ptt_data_date.append(data_ex.iloc[i,0])
    
for i in range(n):
    ptt_data_sign.append(data_ex.iloc[i,1])
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
for i in range(len(ptt_sellect_date)):
    print("{} , {}".format(ptt_sellect_date[i],ptt_sellect_sign[i]))

import mysql.connector

def se_db(name):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='pystock')
    cur = conn.cursor()
    sql = "SELECT * FROM "+name+" ORDER BY id"
    cur.execute(sql)
    row_db  = cur.fetchall()
#    print(row_db)
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
    conn.close()
    return row_db
    
    
data_fet = se_db('ptt')
print(type(data_fet))
print(data_fet[0][1])
print(type(data_fet[0][1]))
print(type(ptt_sellect_date[1]))
collect_n = []
print(len(data_fet))
oper_ptt = []
oper_ptt.append(100000)
vol_ptt = []
vol_ptt.append(0)
d=0
for i in range(len(data_fet)):
    for j in range(len(ptt_sellect_date)):
        if ptt_sellect_date[j] == data_fet[i][1]:
            collect_n.append(i)
#            if ptt_sellect_sign[i] == 1:
#                p = int(float(data_fet[i][2]))
#                op=oper_ptt[d-1]
#                vol_ptt.append((op-(op%p))/p)
#                d = d+1
#            elif ptt_sellect_sign[i] == -1:
#                p2 = int(float(data_fet[i][2]))
#                oper_ptt.append(p2*vol_ptt[d-1])
#                d = d+1

print('xxxxxxxxxxxxxxx')
print(vol_ptt[0])
print(oper_ptt)
print(collect_n)
print(len(collect_n))
print(type(collect_n[0]))
print(data_fet[11][2])
print(collect_n[11])

for i in range(len(collect_n)):
    if i%2 == 0: 
        print(data_fet[i][1])
        p = int (float(data_fet[collect_n[i]][2]))
        op = oper_ptt[d]
        vol_ptt.append((op-(op%p))/p)
        d=d+1
        p2 = int (float(data_fet[collect_n[i+1]][2]))
        vl = vol_ptt[d]
        oper_ptt.append(p2*vl)

print(oper_ptt)
roi = (oper_ptt[0]/oper_ptt[len(oper_ptt)-1])*100

for i in collect_n:
    print(data_fet[i][2])
    
print(roi)
#money = 100000
#for i in collect_n:
#    if 

#print(ptt_sellect_date)
#print(ptt_sellect_sign)
#print(ptt_close)
#print(ptt_date)