import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataSet = pd.read_csv('assets/datosLaguna.csv',sep=',')
dataApril = dataSet[(dataSet.Fecha>= '2010-03-20')&(dataSet.Fecha <= '2010-04-30')]
dataBefore = dataSet[(dataSet.Fecha>= '2010-03-20')&(dataSet.Fecha < '2010-04-04')]
dataAfter = dataSet[(dataSet.Fecha> '2010-04-04')&(dataSet.Fecha <= '2010-04-30')]
#dataApril.plot(x='Fecha',y='Magnitud')
#dataBefore.plot(x='Fecha',y='Magnitud')
#dataAfter.plot(x='Fecha',y='Magnitud')
#plt.show()
res = 0
for i in range(len(dataBefore)):
    #print(dataBefore.iloc[i,1])
    res = res + dataBefore.iloc[i,1]
    if(i <= 0):
        auxMaxB = dataBefore.iloc[i,1]
        auxMinB = dataBefore.iloc[i,1]
    else:
        if dataBefore.iloc[i,1] > auxMaxB:
            auxMaxB = dataBefore.iloc[i,1]
        if dataBefore.iloc[i,1] < auxMaxB:
            auxMinB = dataApril.iloc[i,1]
promBefore = res/len(dataBefore)

res2 = 0
for i in range(len(dataAfter)):
    #print(dataApril.iloc[i,1])
    res2 = res2 + dataAfter.iloc[i,1]
    if(i <= 0):
        auxMaxA = dataAfter.iloc[i,1]
        auxMinA = dataAfter.iloc[i,1]
    else:
        if dataAfter.iloc[i,1] > auxMaxA:
            auxMaxA = dataAfter.iloc[i,1]
        if dataAfter.iloc[i,1] < auxMinA:
            auxMinA = dataAfter.iloc[i,1]
#print(res2)
promAfter = res2/len(dataAfter)
print(promBefore, promAfter)
print("Maximo y minimo para antes del temblor de 7.2 ", auxMaxB, auxMinB)
print("Maximo y minimo para despues del temblor de 7.2 ", auxMaxA, auxMinA)
