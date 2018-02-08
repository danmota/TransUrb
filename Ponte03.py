# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:47:10 2018

@author: Koch
"""

import xlsxwriter
#import pandas as pd


z = 'C:\\Users\\danielmota\\Documents\\KochTemp\\010.txt'
data = open(z,'r')


line = data.readlines()
count =  len(line)


alist = []
i=0
while i<=count-1:
    alist.append(line[i])
    i=i+1   


t = list(set(alist))
count2 = len(t)


y = 'V0.xlsx'
workbook = xlsxwriter.Workbook(y)
sh1 = workbook.add_worksheet('Luke')


h=1
while h<=count2-1:
    tex = t.__getitem__(h)
    c1,c2,c3,c4,c5,c6 = tex.split(',')
    sh1.write(h,0,c1)
    sh1.write(h,1,c2)
    sh1.write(h,2,c3)
    sh1.write(h,3,c4)
    sh1.write(h,4,c5)
    sh1.write(h,5,c6)
    h=h+1

