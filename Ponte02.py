# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:47:10 2018

@author: Koch
"""

import xlsxwriter




data = open('C:\\Users\\danielmota\\Documents\\KochTemp\\010.txt','r')


line = data.readlines()
count =  len(line)


alist = []
i=0
while i<=count-1:
    alist.append(line[i])
    i=i+1   


t = list(set(alist))
count2 = len(t)


workbook = xlsxwriter.Workbook('V0.xlsx')
worksheet1 = workbook.add_worksheet('Luke')


h=1
while h<=count2-1:
    worksheet1.write(h,0,t.__getitem__(h))
    h=h+1


'''
j=0
while j<=300:
    worksheet1.write(1,0,'AAA')    
    j+1

#(list.__getitem__(t,1))
'''