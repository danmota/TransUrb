# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:23:59 2018

@author: Koch
"""


z = 'C:\\Users\\danielmota\\Documents\\KochTemp\\000.txt'
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


'''----------------------------'''


h=1
dados_tratados = []
dados_temp = []

#Filtros
vehicle = '82111'
line = '1340'


k = 'k' #Solucao para o ) que vinha depois de y no segundo while
while h<=count2-1:
    tex = t.__getitem__(h)
    c1,c2,c3,c4,c5,c6 = tex.split(',')    
    if (c4 == vehicle) and (c3 == line):  
        dados_temp = c1,c2,float(c5),float(c6), k
        dados_tratados.append(dados_temp)
    h=h+1   
    
dados_tratados.sort(key=lambda tup: tup[1])


X = []
Y = []
hh = 0
while hh<=len(dados_tratados)-1:
    t1,t2,x,y,k = str(dados_tratados.__getitem__(hh)).split(',')    
    X.append(float(x))
    Y.append(float(y))
    hh=hh+1


'''---------------------------'''


from matplotlib import pyplot as plt

labels = []


plt.scatter(X,Y)

for label,X_count,Y_count in zip(labels,X,Y):
    plt.annotate(label,
                 xy=(X_count,Y_count),
                 xytext=(5,-5),
                 textcoords='offset points')
    
plt.title("Trajetoria do veiculo linha " + line)
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.show()


'''---------------------------'''


from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):        
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r


Velm = []
for ipx in range(len(dados_tratados)-1):
    lat1 = (dados_tratados [ipx][2])
    lon1 = (dados_tratados [ipx][3])
    lat2 = (dados_tratados [ipx + 1][2])
    lon2 = (dados_tratados [ipx + 1][3])
    vmtemp = (((haversine(lon1, lat1, lon2, lat2))*1000)/60)
    Velm.append(vmtemp)

    
'''---------------------------'''


import pandas as pd

Tabela = pd.DataFrame(dados_tratados)
Velm = pd.DataFrame(Velm)
dfx_temp = pd.DataFrame(['-'])
Velocidade = dfx_temp.append(Velm)
Tabela = Tabela.assign(Velocidade=Velocidade.values)
Tabela = Tabela.drop([4], axis=1)





