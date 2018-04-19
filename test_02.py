# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:55:10 2018

@author: wuttinun_r
"""

for i in range(5):
    print(i)

print('mike')

a = []
for i in range(3,10):
    a.append (2)
    
print(a)

a[2]=10
print(a)
print(type(a))

b = [2,3,5,7,9]
print(b.index(5))

c = 'mike'
d= 'mike'
if c==d:
    print('ok')