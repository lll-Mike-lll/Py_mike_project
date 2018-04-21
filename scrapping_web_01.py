# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:50:05 2018

@author: wuttinun_r
"""

a = input('name:')

def inp(a):
    import pandas as pan
    url = 'http://www.panphol.com/data/page/stockprice/'+a+'#'
    data = pan.read_html(url)
    return data
    
print(inp(a))
