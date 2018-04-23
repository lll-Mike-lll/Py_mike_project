# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:15:27 2018

@author: MIKE
"""
import pandas as pann
data_ex = pann.read_excel("D:\ptt_data_3.xlsx")
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
n_se = len(ptt_sellect_sign)
if ptt_sellect_sign[n_se-1] == 1:
    nloop = len(ptt_sellect_sign)-1
else:
    nloop = len(ptt_sellect_sign)
ptt_sellect_sign2 = []
ptt_sellect_date2 = []
print(n_se)
print(nloop)

for i in range(nloop):
    ptt_sellect_sign2.append(ptt_sellect_sign[i])
    ptt_sellect_date2.append(ptt_sellect_date[i])
    
    
    
    
#for i in range(50):
#    print("{},{} : {},{}".format(ptt_sellect_date[i],ptt_sellect_sign[i],ptt_sellect_date2[i],ptt_sellect_sign2[i]))
#for i in range(len(ptt_sellect_date)):
#    print("{},{}".format(ptt_sellect_date[i],ptt_sellect_sign[i]))
#print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#for i in range(len(ptt_sellect_date2)):
#    print("{},{}".format(ptt_sellect_date2[i],ptt_sellect_sign2[i]))    
    
    
    
    