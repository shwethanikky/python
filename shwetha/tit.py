# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 22:28:26 2022

@author: SPTINT-08
"""

import pandas as pd
df={'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack','Lee','Chanchal','Gasper','Naviyar','Andres']),
       'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df=pd.DataFrame(df)
print("Mean values in the Distribution")
print(df.mean())
print("*********************************")
print("Mean values in the Distribution")
print(df.median())