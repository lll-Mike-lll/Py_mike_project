# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:49:02 2018

@author: MIKE
"""
import pandas as pan
def inp(a):
    url = 'http://www.panphol.com/data/page/stockprice/'+a+'#'
    data = pan.read_html(url)
    return data

name = input('name')
data_1 = inp(name)
n =len(data_1[0])
data_list1 = []
for i in range(9):
    data_list1.append([])
for i in range(9):
    for j in range(n):
        data_list1[i].append(data_1[0].iloc[j,i])
    
print(data_list1[1])
print(type(data_list1[1][0]))
#print(data_list1)
print(data_1)


