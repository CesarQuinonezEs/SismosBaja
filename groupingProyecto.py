import pandas as pd
import numpy as np

dataSet = pd.read_csv('assets/datosDistHeu.csv',sep=',')
asignados = []
fallas = [dataSet['Dist_vallecitos'],dataSet['Dist_AguaBlanca'],dataSet['Dist_LagunaSalada'],dataSet['Dist_SanMiguel'],dataSet['Dist_cerroPrieto']]


for i,dist in enumerate(fallas):
    mag = []
    lat = []
    lon = []
    date = []
    print(dist[0])
    for j in range(len(dist)):
        isInTarget = False
        isAsig = False
        for k in range(5):
            if(k == 0):
                aux = dist[j]
            else:
                if(aux < dataSet.iloc[j,k+4]):
                    #print(aux, " es menor que ", dataSet.iloc[j,k+4])
                    isInTarget = True
                else:
                    #print(aux, " es mayor que ", dataSet.iloc[j,k+4])
                    isInTarget = False
        if isInTarget:
            if  j not in asignados:
                #print(j)
                asignados.append(j)
                date.append(dataSet.iloc[j,0])
                mag.append(dataSet.iloc[j,1])
                lat.append(dataSet.iloc[j,2])
                lon.append(dataSet.iloc[j,3])
    if i == 0:
        print("Datos vallecitos")
        dataGroup = pd.DataFrame({'Fecha': date,
                          'Magnitud':mag,
                          'Latitud':lat,
                          'Longitud':lon
                          })
        print(dataGroup)
        dataGroup.to_csv('assets/datosValle.csv',index=False)
    elif(i == 1):
        print("Datos aguablanca")
        dataGroup = pd.DataFrame({'Fecha': date,
                          'Magnitud':mag,
                          'Latitud':lat,
                          'Longitud':lon
                          })
        print(dataGroup)
        dataGroup.to_csv('assets/datosAgua.csv',index=False)
    elif(i == 2):
        print("Datos laguna salada---------------")
        dataGroup = pd.DataFrame({'Fecha': date,
                          'Magnitud':mag,
                          'Latitud':lat,
                          'Longitud':lon
                          })
        print(dataGroup)
        dataGroup.to_csv('assets/datosLaguna.csv',index=False)
    elif(i == 3):
        print("Datos san miguel ----------")
        dataGroup = pd.DataFrame({'Fecha': date,
                          'Magnitud':mag,
                          'Latitud':lat,
                          'Longitud':lon
                          })
        print(dataGroup)
        dataGroup.to_csv('assets/datosMiguel.csv',index=False)
    elif(i == 4):
        print("Datos cerro prieto --------------------------------")
        dataGroup = pd.DataFrame({'Fecha': date,
                          'Magnitud':mag,
                          'Latitud':lat,
                          'Longitud':lon
                          })
        print(dataGroup)
        dataGroup.to_csv('assets/datosCerroPrieto.csv',index=False)