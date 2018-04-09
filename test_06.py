# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 22:48:18 2018

@author: MIKE
"""
#a = '334'
#b = int(a)
#print(b)
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
check = 1
for i in range(len(ptt_data_date)):
    if ptt_data_sign[i] == (-check):
        print("%d - %d" % (i , ptt_data_sign[i]))
        check = check*(-1)