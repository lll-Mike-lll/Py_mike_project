# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:27:44 2018

@author: MIKE
"""

import pymysql
conn = pymysql.connect(host = 'localhost', user = 'root', password='')
try:
    with conn.cursor() as cursors:
        cursors.execute('CREATE DATABASE MIKE_PYTHON')

finally:
    conn.close()