import pandas as pd
import matplotlib.pyplot as plt
dataSetVll = pd.read_csv('assets/datosValle.csv',sep=',')
dataSetAg = pd.read_csv('assets/datosAgua.csv',sep=',')
dataSetLag = pd.read_csv('assets/datosLaguna.csv',sep=',')

print(dataSetVll)
print(dataSetLag)
print(dataSetLag)
date = []
mag = []
lat = []
lon = []
fallas = [dataSetVll,dataSetAg,dataSetLag]
for j in fallas:
    for i in range(len(j)):

        if(i <= 0):
            aux = j.iloc[i,1]
            dateAux = j.iloc[i,0]
            magAux = aux
            latAux = j.iloc[i,2]
            lonAux = j.iloc[i,3]
        else:
            if(aux < j.iloc[i,1]):
                aux = j.iloc[i,1]
                dateAux = j.iloc[i,0]
                magAux = aux
                latAux = j.iloc[i,2]
                lonAux = j.iloc[i,3]
    date.append(dateAux)
    mag.append(magAux)
    lat.append(latAux)
    lon.append(lonAux)
dataHeight = pd.DataFrame({'Falla': ['vallecitos','Agua blanca','Laguna salada'],
                           'Fecha': date,
                           'Magnitud': mag,
                           'latitud':lat,
                           'longitud':lon
                          })
print(dataHeight)
dataHeight.to_csv('assets/highestData.csv',index=False)
