from dis import dis
import pandas as pd
import numpy as np

#Abrimos el csv
dataSet = pd.read_csv('./assets/datos.csv',usecols=['Fecha','Magnitud','Latitud','Longitud'],sep=',')

#Distancia de cada falla
coorVallecitos = [32.22,-116.54]
coorAguaBlanca = [31.6, -116.53]
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

dataFDist = pd.DataFrame({'Fecha': dataSet['Fecha'],
                          'Magnitud':dataSet['Magnitud'],
                          'Latitud':dataSet['Latitud'],
                          'Longitud':dataSet['Longitud'],
                          'Dist_vallecitos':disHeu[0],
                          'Dist_AguaBlanca':disHeu[1]})
print(dataFDist)
dataFDist.to_csv('assets/datosDistHeu.csv',index=False)
dataFDist.to_latex('assets/datosDistHeu.tex',index=False)