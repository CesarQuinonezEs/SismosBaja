import matplotlib.pyplot as plt
import pandas as pd

dataSetVll = pd.read_csv('assets/datosValle.csv',usecols=['Latitud','Longitud'],sep=',')
dataSetAg = pd.read_csv('assets/datosAgua.csv',usecols=['Latitud','Longitud'],sep=',')
dataSetLag = pd.read_csv('assets/datosLaguna.csv',usecols=['Latitud','Longitud'],sep=',')
coorVallecitos = [32.22,-116.54]
coorAguaBlanca = [31.6, -116.53]
coorLagunaSa = [32.360320206798384, -115.65058167215838]
index = [coorVallecitos,coorAguaBlanca,coorLagunaSa]
colors = ["#4EACC5", "#FF9C34", "#4E9A06",]
plt.figure(1)
fallas = [dataSetVll,dataSetAg,dataSetLag]
for i,j in enumerate(fallas):
    for k in j:
        plt.scatter(j['Latitud'],j['Longitud'],c=colors[i], marker=".", s=10)

for i in index:
   plt.scatter(i[0],i[1],c="b", marker=".", s=10)
plt.title("Agrupamiento de cada sismo")
plt.xticks([])
plt.yticks([])
plt.show()