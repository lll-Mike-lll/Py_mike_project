# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:50:05 2018

@author: wuttinun_r
"""
def inp(a):
    import pandas as pan
    url = 'http://www.panphol.com/data/page/stockprice/'+a+'#'
    data = pan.read_html(url)
    return data

print(inp(input('name:')))





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


