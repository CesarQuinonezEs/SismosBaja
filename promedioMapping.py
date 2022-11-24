import pandas as pd
import matplotlib.pyplot as plt
dataSetVll = pd.read_csv('assets/datosValle.csv',usecols=['Magnitud'],sep=',')
dataSetAg = pd.read_csv('assets/datosAgua.csv',usecols=['Magnitud'],sep=',')
dataSetLag = pd.read_csv('assets/datosLaguna.csv',usecols=['Magnitud'],sep=',')

print(dataSetVll)
print(dataSetLag)
print(dataSetLag)

proMag = []

fallas = [dataSetVll,dataSetAg,dataSetLag]
for j in fallas:
    res = 0
    for i in range(len(j)):
        res = res + j.iloc[i,0]
    prom = res/len(j)
    proMag.append(prom)

dataHeight = pd.DataFrame({'Falla': ['vallecitos','Agua blanca','Laguna salada'],
                            'Promedio': proMag
                          })
print(dataHeight)
dataHeight.to_csv('assets/promedios.csv',index=False)
dataHeight.to_latex('assets/promedios.tex',index=False)