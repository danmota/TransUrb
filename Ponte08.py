# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:23:59 2018

@author: DMota e Koch
"""
    
#from Tkinter import *
#
#class Application(Frame):
#    def __init__(self, master=None):
#        Frame.__init__(self,master)
#        self.grid()
#        self.initialize()        
#    
#    def initialize(self):
#        
#        self.btn1 = Button(self, text = 'Aplicar', command=retrieve_input)
#        self.btn1.grid()
#
#def retrieve_input():
#    global z
#    z = entry.get()
#        
#root = Tk()
#root.title('Arquivo')
#root.geometry('200x100')
#entry = Entry(root)
#entry.grid(column=0,row=0)
#entry.focus()                                    
#entry.bind('<Return>', (lambda event: retrieve_input()))  
#app = Application(root)
#root.mainloop()
#  

'''----------------------------'''

z = '000'
data = open('C:\\Users\\danielmota\\Documents\\GitHub\\TransUrb\\' +z+ '.txt','r')


line = data.readlines()
count =  len(line)


alist = []
i=0
while i<=count-1:
    alist.append(line[i])
    i=i+1   


t = list(set(alist))
count2 = len(t)

#DMota Comentado  - Inicio
#'''----------Filtros-----------'''
#
#class Application2(Frame):
#    def __init__(self, master=None):
#        Frame.__init__(self,master)
#        self.grid()
#        self.initialize()     
#    
#    def initialize(self):
#        
#        self.btn1 = Button(self, text = 'Veiculo Ap', command=retrieve_input)
#        self.btn1.grid()
#        
#        self.label = Label(self,)
#
#def retrieve_input():
#    global vehicle, line
#    vehicle = entry.get()
#    line = entry1.get()
#        
#root = Tk()
#root.title('Teste')
#root.geometry('200x100')
#entry1 = Entry(root)
#entry = Entry(root)
#entry.grid(column=0,row=0)
#entry1.grid(column=0,row=1)
#entry.focus()
#entry1.focus()
#entry.bind('<Return>', (lambda event: retrieve_input()))
#entry1.bind('<Return>', (lambda event: retrieve_input()))
#app = Application(root)
#root.mainloop()
#
##Filtros
##vehicle = '11864'
##line = '33200'
#
#
#'''----------------------------'''
#DMota Comentado  - Fim


# DMota - Criação do padrão de horários - INICIO


import datetime
lst_time_pattern = []
for ii in range(24):
    for j in range(60):
        lst_time_pattern.append(datetime.datetime(1900, 1, 1, ii, j).strftime('%H:%M'))
        
# DMota - Criação do padrão de horários - FIM        



dados_semitratados = []
dados_temp = []


dados2 = tuple()
position = dict()

#DMota - Inclusão de horários padrão - INICIO

for ltp in lst_time_pattern:
    position[ltp] = []




#DMota - Inclusão de horários padrão - FIM





h=1
dct_line = dict()


##### Gera dicionário com onibus e linhas
k = 'k' #Solucao para o ) que vinha depois de y no segundo while
while h<=count2-1:
    tex = t.__getitem__(h)
    c1,c2,c3,c4,c5,c6 = tex.split(',')
    
    if c3 in dct_line:
        if c4 in dct_line[c3]:
            pass
        else:
            dct_line[c3].append(c4)
    else:
        dct_line[c3] = [c4]
    
    h += 1


vehicle = '12163'
line = '1364'

#for vehicle in dct_line['33348']:
h=1
k = 'k' #Solucao para o ) que vinha depois de y no segundo while
while h<=count2-1:
    tex = t.__getitem__(h)
    c1,c2,c3,c4,c5,c6 = tex.split(',')
    
    if (c4 == vehicle) and (c3 == line):
        dados2 = (float(c5),float(c6))
  
        try:
            if c2 in position:
                position[c2].append(dados2)

            else:
                position[c2] = [dados2]
        except:
            pass
    h=h+1 


for pos in position.keys():
    
    if (len(position[pos]) > 1):
        media_lat = 0
        count_lat = 0
        media_lon = 0
        count_lon = 0
        
        for j in position[pos]:
            media_lat = media_lat + j[0]
            count_lat = count_lat + 1
            media_lon = media_lon + j[1]
            count_lon = count_lon + 1
        media_tuple = (media_lat/count_lat, media_lon/count_lon)
        
        position[pos] = [media_tuple]
        
 
    elif (len(position[pos]) == 1):
        
        for jayjayojatinho in position[pos]:
            media_tuple = (jayjayojatinho[0], jayjayojatinho[1])
            position[pos] = [media_tuple]
      
     

          
#         
#    if (c4 == vehicle) and (c3 == line):  
#        dados_temp = c1,c2,float(c5),float(c6), k
#        dados_semitratados.append(dados_temp)
     
    
#dados_semitratados.sort(key=lambda tup: tup[1])
#
#
#'''---------------------------'''
#
#dados_tratados = []
#dados_tratados = dados_semitratados
#
#
#for ipx in range(len(dados_semitratados)):
#    tex = dados_semitratados.__getitem__(h)
#
#
#ipx = 0
#
#'''---------------------------'''

from datetime import datetime as dt


X = []
Y = []
table_time = []
for i in position.keys():
#    trashdate,time,x,y,k = str(dados_tratados.__getitem__(hh)).split(',')
    if len(position[i])>0:
        X.append(position[i][0][0])
        Y.append(position[i][0][1])
    #    time = time.replace("'","")
    time = dt.strptime(i,'%H:%M')     
    table_time.append(time)
    
    
'''---Graph-Trajeto-----------'''

from matplotlib import pyplot as plt


labels = []
plt.scatter(X,Y)


for label,X_count,Y_count in zip(labels,X,Y):
    plt.annotate(label,
                 xy=(X_count,Y_count),
                 xytext=(5,-5),
                 textcoords='offset points')    
plt.title(u"Trajetoria da linha " + str(line) + " veiculo:" + str(vehicle))
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



'''---------------------------'''



dkm = []
Velm = []
it = 0

lst_time = position.keys()


tpl_vel = tuple()

lst_vel2 = []

lst_time.sort()


for ci in range(len(position.keys())-1):
    try:
        lat1 = position[lst_time[ci]][0][0]
        lon1 = position[lst_time[ci]][0][1]
        lat2 = position[lst_time[ci+1]][0][0]
        lon2 = position[lst_time[ci+1]][0][1]
        vmtemp = (((haversine(lon1, lat1, lon2, lat2))*1000)/60)
    #    Velm.append(vmtemp)
    #    lst_time2.append(dt.strptime(lst_time[i+1],'%H:%M'))
    #    lst_vel.append(vmtemp)
        tpl_vel = (dt.strptime(lst_time[ci+1],'%H:%M'), vmtemp)
        lst_vel2.append(tpl_vel)
    except IndexError:
        tpl_vel = (dt.strptime(lst_time[ci+1],'%H:%M'), 0)
        lst_vel2.append(tpl_vel)
        #z_temp = 'error'
        #z_temp = ("-I- Time",lst_time[ci],"or",lst_time[ci+1],"does not exist")
        #z.append(z_temp)

#lst_vel2.sort(key=lambda tup: tup[0])
    
lst_time2 = []
lst_vel = []
for ii in range(24):
    for j in range(60):
        current_date = datetime.datetime(1900, 1, 1, ii, j)
        bool_test = False
       
        for i in lst_vel2:
            if (current_date == i[0]):
                bool_test = True
                break
            
        if (bool_test == True):
                lst_vel.append(i[1])
                lst_time2.append(i[0])
        else:
                lst_vel.append(0)
                lst_time2.append(current_date)                
        

#Agregar Velocidades
 


lst_test = []                   
time_window = 59
lst_timewdw = []
lst_velwdw = []
dict_window = dict()
current_date =(datetime.datetime(1900, 1, 1, 0, 0)) #testei como str tambem sem sucesso
last_date = (datetime.datetime(1900, 1, 1, 0, 0))

for ii in range(24):
    k=0
    for j in range(60):
        if (k < 60):        
            try:
#                print "Quer criar em -> " + str(last_date)  + "Tempo atual é -> " + str(lst_time2[0])
                if lst_time2[0] == last_date:
#                    print "Criou em -> " + str(last_date) 
                    dict_window[last_date] = [lst_vel[0]]
                    del lst_time2[0]
                    del lst_vel[0]
                else:
                    while (lst_time2[0] < current_date):
#                        print "Acumulada-> "+str(lst_time2[0]) + " Entra em -> " + str(last_date)
                        dict_window[last_date].append(lst_vel[0])
                        
                        lst_test = lst_time2
                        del lst_time2[0]
                        del lst_vel[0]
                    last_date = current_date
                    k = k + time_window
                    current_date=(datetime.datetime(1900, 1, 1, ii, k))
            except:
#                print "Falhou"
                pass


for l in dict_window.keys():
    if (dict_window[l]>0):
        dict_window[l] = sum(dict_window[l])/len(dict_window[l])
    else:
        dict_window[l] = 0

    



#    break
#
#countm = 0
#sumi = 0
#
#for dic in range(len(dict_window.keys())): 
#    countm += 1
#    counti = 0
#    while counti < 10:
#        sumi += dict_window[lst_test[dic]][counti]
#        counti += 1
#    meani = sumi/countm    



#dict_test = {'00:00':[2,3,4,5,2,3,4,5,2,3],'00:10':[5,1,5,1,5,1,5,1,5,1],'00:20':[4,1,2,8,5,1,2,8,2,1],'00:30':[3,1,2,5,3,1,2,5,4,1]}
#lst_dict_test = ['00:00','00:10','00:20','00:30']
#
#countm = 0
#sumi=0
#for dicktest in range(len(dict_test.keys())):
#    countm += 1
#    counti = 0
#    print 'fock' 
#    while counti < 10:
#        sumi += dict_test[lst_dict_test[dicktest]][counti]
#        counti += 1
#    meani = sumi/countm












import matplotlib.dates as mdates
import numpy as np
from matplotlib import pyplot as plt2

lst_time2 = dict_window.keys()
lst_time2.sort()

lst_time3 = []

for l in lst_time2:
    #lst_time3.append(str(l.time())[0:5])
    lst_time3.append(l.time())

lst_vel = []

for i in lst_time2:
    lst_vel.append(dict_window[i])

fig = plt2.figure(num=None, figsize=(10, 5), dpi=100, facecolor='w', edgecolor='k')
ax  = fig.add_subplot(111)
plt2.plot(lst_time3,lst_vel,c='b', label='Velocidade Media')


#ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=20))   #to get a tick every 15 minutes
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))     #optional formatting 
#plt.show()

# Comentado DMota - Inicio 

#for ipx in range(len(dados_tratados)-1):
#    lat1 = (dados_tratados [ipx][2])
#    lon1 = (dados_tratados [ipx][3])
#    lat2 = (dados_tratados [ipx + 1][2])
#    lon2 = (dados_tratados [ipx + 1][3])
#    time = table_time.__getitem__(it)
#    time2 = table_time.__getitem__(it+1)
#    
#    if (time2 - time) <= timedelta(minutes=1):    
#        dkmtemp = haversine(lon1, lat1, lon2, lat2)
#        vmtemp = (((haversine(lon1, lat1, lon2, lat2))*1000)/60)
#        dkm.append(dkmtemp)
#        Velm.append(vmtemp)
#    else:
#        dkm.append('Null')
#        Velm.append('Null')
#    
#    it = it + 1
#ipx = 0
#
#'''----Tabelando--------------'''
#
#import pandas as pd
#
#
#Tabela = pd.DataFrame(dados_tratados)
#dkm = pd.DataFrame(dkm)
#Velm = pd.DataFrame(Velm)
#dfx_temp = pd.DataFrame(['-'])
#Distancia = dfx_temp.append(dkm)
#Velocidade = dfx_temp.append(Velm)
#Tabela = Tabela.assign(Distancia=Distancia.values)
#Tabela = Tabela.assign(Velocidade=Velocidade.values)
#Tabela = Tabela.drop([4], axis=1)


# Comentado DMota - Fim




'''----Médias-----------------'''
#
#
#smx = []
#smx_temp = []
#speed_mean_temp = []
#speed_mean = []
#table_time_temp = []
#table_time = []
#
#
#for ippx in range(len(Tabela)-1):
#    if (Tabela.get_value(ippx,1,takeable=True) == 
#        Tabela.get_value(ippx+1,1,takeable=True)): 
#        
#        smx_temp = Tabela.get_value(ippx,5,takeable=True)
#        smx.append(smx_temp)
#      
#    else:
#        smx_temp = Tabela.get_value(ippx,5,takeable=True)
#        smx.append(smx_temp) 
#



#
#speed_mean_temp = []
#spedd_mean = []
#for ippx in range(len(Tabela)-1):
#    if (Velocidade.get_value(ippx,1,takeable=True) <> 
#        Velocidade.get_value(ippx+1,1,takeable=True)):
#        
#        table_time_temp = Tabela.get_value(ippx,1,takeable=True)
#        table_time.append(table_time_temp)   
#        Hora = pd.DataFrame(table_time)
#    else:
#
#'''----Graph-Veloc------------'''
#fazer média intervalo de 15 min

#
#
#mean = pd.DataFrame()
#mean_temp = pd.DataFrame()
#
#
#
#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.axis([0, 6, 0, 20])
#plt.show()




