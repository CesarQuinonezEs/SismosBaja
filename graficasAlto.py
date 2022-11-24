import pandas as pd
import matplotlib.pyplot as plt

dataSet = pd.read_csv('assets/highestData.csv',usecols=['Fecha','Magnitud'],sep=',')
print(dataSet)
dataSet.plot.scatter(x='Fecha',y ='Magnitud')
plt.show()