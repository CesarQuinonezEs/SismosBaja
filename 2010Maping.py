import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataSet = pd.read_csv('assets/datos.csv',usecols=['Fecha','Magnitud','Latitud','Longitud'],sep=',')
dataYear10 = dataSet[(dataSet.Fecha>= '2010-04-01')&(dataSet.Fecha <= '2010-04-04')]
dataYear10.plot.scatter(x='Fecha',y ='Magnitud')
plt.show()
dataYear10.to_latex('assets/datos2010.tex',index=False)