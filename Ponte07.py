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
data = open('C:\\Users\\danielmota\\Documents\\KochTemp\\' +z+ '.txt','r')


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

vehicle = '33348'
line = '11091'
import datetime
lst_time_pattern = []
for ii in range(24):
    for j in range(60):
        lst_time_pattern.append(datetime.datetime(1900, 1, 1, ii, j).strftime('%H:%M'))
        
# DMota - Criação do padrão de horários - FIM        


h=1
dados_semitratados = []
dados_temp = []


dados2 = tuple()
position = dict()

#DMota - Inclusão de horários padrão - INICIO

for ltp in lst_time_pattern:
    position[ltp] = []
    
    


#DMota - Inclusão de horários padrão - FIM







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


for i in position.keys():
    if (len(position[i]) > 1):
        media_lat = 0
        count_lat = 0
        media_lon = 0
        count_lon = 0
        
        for j in position[i]:
            media_lat = media_lat + j[0]
            count_lat = count_lat + 1
            media_lon = media_lon + j[1]
            count_lon = count_lon + 1
        media_tuple = (media_lat/count_lat, media_lon/count_lon)
        
        position[i] = [media_tuple]
  
    else:
        media_tuple = (-23.5160725,-46.698696) # DMota - CORRIGIR!!!!!!
        position[i] = [media_tuple]
         
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
plt.title(u"Trajetória do veículo linha " + line)
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

from datetime import timedelta


dkm = []
Velm = []
it = 0

lst_time = position.keys()


tpl_vel = tuple()
lst_vel = []
lst_vel2 = []
lst_time2 = []

for i in range(len(position.keys())-1):
    lat1 = position[lst_time[i]][0][0]
    lon1 = position[lst_time[i]][0][1]
    lat2 = position[lst_time[i+1]][0][0]
    lon2 = position[lst_time[i+1]][0][1]
    vmtemp = (((haversine(lon1, lat1, lon2, lat2))*1000)/60)
#    Velm.append(vmtemp)
#    lst_time2.append(dt.strptime(lst_time[i+1],'%H:%M'))
#    lst_vel.append(vmtemp)
    tpl_vel = (dt.strptime(lst_time[i+1],'%H:%M'), vmtemp)
    lst_vel2.append(tpl_vel)



#lst_vel2.sort(key=lambda tup: tup[0])

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
        

plt.plot(lst_time2,lst_vel)



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




#