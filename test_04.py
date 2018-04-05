# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:27:44 2018

@author: MIKE
"""

#import pymysql
#conn = pymysql.connect(host = 'localhost', user = 'root', password='')
#try:
#    with conn.cursor() as cursors:
#        cursors.execute('CREATE DATABASE MIKE_PYTHON')
#
#finally:
#    conn.close()

import pymysql
conn = pymysql.connect(host = 'localhost', user = 'root', password='',db='MIKE_PYTHON')
a = conn.cursor()
sql = "CREATE TABLE mike3(date varchar(50), open varchar(50),close varchar(50))"
a.execute(sql)