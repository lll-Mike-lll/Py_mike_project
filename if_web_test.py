# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 15:00:59 2018

@author: wuttinun_r
"""
a = input('code: ')
if a == '0':
    print('all')
elif a=='1':
    print('each')
    while True:
        b=input('code2:')
        if b!='0':
            print('oo')
        else:
            print('ll')
            break

#i = input('code:')
#while True:
#    if i =='1':
#        print('oo')
#        break
#    else :
#        print('ll')
#        break