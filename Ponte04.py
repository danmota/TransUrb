# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:47:10 2018

@author: Koch
"""

'''
criar interface gráfica para ponte.py
txt -> access -> excel
blaze (interface de big data)
linha 1340 onibus 82992 hora 08:42

'''




import xlsxwriter



z = 'C:\\Users\\danielmota\\Documents\\KochTemp\\555.txt'
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


y = 'Vul0.xlsx'
workbook = xlsxwriter.Workbook(y)
sh1 = workbook.add_worksheet('Luke')
sh1.write(0,0,'Data')
sh1.write(0,1,'Hora')
sh1.write(0,2,'Linha')
sh1.write(0,3,'Veiculo')
sh1.write(0,4,'Latitude')
sh1.write(0,5,'Longitude')


h=1
dados_tratados = []
dados_temp = []

#Filtros
vehicle = '82111'
line = '1340'


while h<=count2-1:
    tex = t.__getitem__(h)
    c1,c2,c3,c4,c5,c6 = tex.split(',')

    if (c4 == vehicle) and (c3 == line):
        dados_tratados.append(tex.split(','))


    sh1.write(h,0,c1)
    sh1.write(h,1,c2)
    sh1.write(h,2,c3)
    sh1.write(h,3,c4)
    sh1.write(h,4,float(c5))
    sh1.write(h,5,float(c6))
    h=h+1

workbook.close()    



from matplotlib import pyplot as plt
from datetime import datetime
import copy

X = []
Y = []
labels = []

data_list = []
data_temp = []





for ip in range(len(dados_tratados)):
    data_temp.append(datetime.strptime(dados_tratados[ip][1], '%H:%M'))
    data_temp.append(dados_tratados[ip][4])
    data_temp.append(dados_tratados[ip][5])   
    data_list.append(copy.deepcopy(data_temp))
    del data_temp[:] 
    
data_list.sort(key=lambda tup: tup[0])    


for ip in range(len(data_list)):
    labels.append(data_list[ip][0])
    X.append(float(data_list[ip][1]))
    Y.append(float(data_list[ip][2]))
    

plt.scatter(X,Y)

for label,X_count,Y_count in zip(labels,X,Y):
    plt.annotate(label,
                 xy=(X_count,Y_count),
                 xytext=(5,-5),
                 textcoords='offset points')
    
plt.title("Trajetória do veículo linha "+line)
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.show()


from math import radians, cos, sin, asin, sqrt
import numpy as np

def haversine(lon1, lat1, lon2, lat2):        
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r

dkm = []
for ipx in range(len(data_list)-1):        
    lat1 = float(data_list [ipx][1])
    lon1 = float(data_list [ipx][2])
    lat2 = float(data_list [ipx + 1][1])  #da erro mas funciona
    lon2 = float(data_list [ipx + 1][2])
    dkmtemp = haversine(lon1, lat1, lon2, lat2)
    dkm.append(dkmtemp)

np.array(data_list)
np.array(dkm)
np.append(data_list,dkm,0)





