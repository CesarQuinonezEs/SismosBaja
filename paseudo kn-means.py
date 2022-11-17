from dis import dis
import pandas as pd
import numpy as np

#Abrimos el csv
dataSet = pd.read_csv('./assets/datos.csv',usecols=['Fecha','Magnitud','Latitud','Longitud'],sep=',')

#Distancia de cada falla
coorVallecitos = [32.22,-116.54]
coorAguaBlanca = [31.6, -116.53]
coorLagunaSa = [32.360320206798384, -115.65058167215838]
coorSanMiguel=[32.0290495918323, -116.35614222296115]
coorPrieto=[32.33181037749735, -115.25019460694705]
disHeu = []
#Distancia heuclidiana longitud para la falla de vallecitos
#dataLatLon = dataSet.iloc[:,[2,3]]
disVal =[]
dataLatLon = dataSet[['Latitud','Longitud']]
print(dataLatLon['Latitud'])
print(len(dataLatLon))
for i in range(len(dataSet)):
    res = 0
    #print(dataLatLon.iloc[i,1])
    res = res + (coorVallecitos[0] - dataLatLon.iloc[i,0])**2
    res = res + (coorVallecitos[1] - dataLatLon.iloc[i,1])**2
    disVal.append(np.sqrt(res))
disHeu.append(disVal)

#distancia para agua blanca
disAgu = []
for i in range(len(dataSet)):
    res = 0
    #print(dataLatLon.iloc[i,1])
    res = res + (coorAguaBlanca[0] - dataLatLon.iloc[i,0])**2
    res = res + (coorAguaBlanca[1] - dataLatLon.iloc[i,1])**2
    disAgu.append(np.sqrt(res))
disHeu.append(disAgu)

#Distancia para la laguna salda

disLaguna = []
for i in range(len(dataSet)):
    res = 0
    #print(dataLatLon.iloc[i,1])
    res = res + (coorLagunaSa[0] - dataLatLon.iloc[i,0])**2
    res = res + (coorLagunaSa[1] - dataLatLon.iloc[i,1])**2
    disLaguna.append(np.sqrt(res))
disHeu.append(disLaguna)

#Distancia de la falla de san miguel 
disSanMiguel = []
for i in range(len(dataSet)):
    res = 0
    #print(dataLatLon.iloc[i,1])
    res = res + (coorSanMiguel[0] - dataLatLon.iloc[i,0])**2
    res = res + (coorSanMiguel[1] - dataLatLon.iloc[i,1])**2
    disSanMiguel.append(np.sqrt(res))
disHeu.append(disSanMiguel)
#Distancia de cerro prieto
disPrieto = []
for i in range(len(dataSet)):
    res = 0
    #print(dataLatLon.iloc[i,1])
    res = res + (coorPrieto[0] - dataLatLon.iloc[i,0])**2
    res = res + (coorPrieto[1] - dataLatLon.iloc[i,1])**2
    disPrieto.append(np.sqrt(res))
disHeu.append(disSanMiguel)

dataFDist = pd.DataFrame({'Fecha': dataSet['Fecha'],
                          'Magnitud':dataSet['Magnitud'],
                          'Latitud':dataSet['Latitud'],
                          'Longitud':dataSet['Longitud'],
                          'Dist_vallecitos':disHeu[0],
                          'Dist_AguaBlanca':disHeu[1],
                          'Dist_LagunaSalada':disHeu[2],
                          'Dist_SanMiguel':disHeu[3],
                          'Dist_cerroPrieto':disHeu[4]})
                        
print(dataFDist)
dataFDist.to_csv('assets/datosDistHeu.csv',index=False)
dataFDist.to_latex('assets/datosDistHeu.tex',index=False)