# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:35:08 2018

@author: wuttinun_r
"""

import pandas as pd
url = "http://www.panphol.com/data/page/stockprice/ADVANC#"
data1 = pd.read_html(url);

#print(data1[0])
print(data1[0].iloc[1:0])
