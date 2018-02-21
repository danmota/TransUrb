# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 00:48:55 2018

@author: DMota e Koch
"""



#Bibliotecas
import pandas as pd
from matplotlib import pyplot as plt
import datetime as dt
from math import radians, cos, sin, asin, sqrt


##Entrada de dados
file_x = '000'

#data = open('C:\\Users\\danielmota\\Documents\\GitHub\\TransUrb\\' + file_x + '.txt','r')
data = open('C:\\Users\\Gabriel\\Documents\\GitHub\\TransUrb\\' + file_x + '.txt','r')

##Tranasformar dados em lista
lst_data_txt = list(set(data.readlines()))

##Transformar lista em Dataframe
df1 = pd.Series(lst_data_txt).str.split(',', expand = True)
df1 = df1.sort_values(by = [0,1])
del lst_data_txt

##Nomear colunas
df1.columns = ['Dia','Hora','Linha',u'Veiculo','Latitude','Longitude']

##Lat Lon para float
df1.Latitude = df1.Latitude.astype(float)
df1.Longitude = df1.Longitude.astype(float)


'''---------'''

##Criar dataframe de 00:00 até 23:59
lst_time_pattern = []
for i in range(24):
    for j in range(60):
        lst_time_pattern.append(dt.datetime(1900, 1, 1, i, j).strftime('%H:%M'))
df_time = pd.DataFrame(lst_time_pattern)
df_time.columns = ['Hora']
df_time = df_time.set_index('Hora')
del lst_time_pattern


'''---------'''

##Criar dataframe de 00:00 até 23:59 de 10 em 10min
m = 0
lst_time_pattern10 = []
for k in range(10):
    lst_time_pattern10.append(dt.datetime(1900, 1, 1, 0, 0).strftime('%H:%M'))
for i in range(24):
    for j in range(60):
        m += 1
        if m == 11:
            for k in range(10):
                lst_time_pattern10.append(dt.datetime(1900, 1, 1, i, j).strftime('%H:%M'))
            m=1


'''---------'''

## Função haversine
def haversine(lon1, lat1, lon2, lat2):        
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r


'''---------'''

##Filtros
line = '1364'


'''---------'''

##Filtrando por linha
df2 = df1[(df1.Linha == line)]
del df1


##Iterar todos os veículos de uma linha
for (n, df_filtrated) in df2.groupby("Veiculo"):
    
    ##Média do pto LatLon
    avg_lat_lon = df_filtrated.groupby('Hora')['Latitude','Longitude'].mean()
    df3 = df_time.join(avg_lat_lon)
    
    ##Criando Dataframe para calcular intervalo de 10 min
    df4 = df3.assign(Intervalo=lst_time_pattern10)
    df4.Latitude = df4.Latitude.astype(float)
    df4.Longitude = df4.Longitude.astype(float)
    df4 = df4.fillna(value = 0)
    
    ##Deletando dataframes obsoletos
    del avg_lat_lon

    '''---------'''
    
    ##Calcular a distancia e a velocidade
    lst_speed_temp=[]
    lst_speed_temp.append(0.0)
    for i in range(len(df4)-1):    
        lat1 = df4.get_value(i,0,takeable = True)
        lon1 = df4.get_value(i,1,takeable = True)
        lat2 = df4.get_value(i+1,0,takeable = True)
        lon2 = df4.get_value(i+1,1,takeable = True)
        speed_temp_x = ((haversine(lon1, lat1, lon2, lat2))*1000)/60
        if speed_temp_x < 22:     
            lst_speed_temp.append(speed_temp_x)
        else:
            lst_speed_temp.append(0.0)    
    ##Deletando dados obsoletos (DDO)
    del lat1, lat2, lon1, lon2, speed_temp_x
    df4 = df4.assign(Velocidade=lst_speed_temp)


    '''---------'''
    
    ##Gráfico de posição
    df_scatter = df4[(df4['Latitude'] != 0) | (df4['Longitude'] != 0)]
    df_scatter.plot(x="Latitude", y="Longitude", kind="scatter", title = u'Trajeto do veículo: ' + n)
    plt.show()


    '''---------'''

    ##Gráfico de velocidade
    df_line = df4.groupby('Intervalo')['Velocidade'].mean()
    df_line.plot(x='Intervalo',y='Velocidade', title = u'Velocidade média do veículo: ' + n)
    
    
    '''---------'''
    
    ##DDO
    del lst_speed_temp, df_filtrated, df_line, df_scatter

##DDO
del lst_time_pattern10, df_time, df2, df3





