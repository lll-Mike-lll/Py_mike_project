# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:27:52 2018

@author: MIKE
"""
import mysql.connector
def up_db():
    conn_up = mysql.connector.connect(host = 'localhost', user = 'root', password='',db='pystock')
    sql = "UPDATE `ea` SET `id`=[value-1],`date`=[value-2],`open`=[value-3],`max`=[value-4],`min`=[value-5],`close`=[value-6],`vol`=[value-7],`val`=[value-8] WHERE 1"