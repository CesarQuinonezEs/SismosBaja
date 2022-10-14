import pandas as pd
import matplotlib.pyplot as plt

dataSet = pd.read_csv('./assets/datos.csv',usecols=['Fecha','Magnitud'],sep=',')
dataYear10 = dataSet[(dataSet.Fecha>= '2010-01-01')&(dataSet.Fecha <= '2010-12-31')]
#dataYear10=dataSet.loc['2010-01-01':'2010-12-31']
#dataYear11=dataSet.loc['2011-01-01':'2011-12-31']
#dataYear12=dataSet.loc['2012-01-01':'2012-12-31']
#dataYear13=dataSet.loc['2013-01-01':'2013-12-31']
#dataYear14=dataSet.loc['2014-01-01':'2014-12-31']
#dataYear15=dataSet.loc['2015-01-01':'2015-12-31']
#dataYear16=dataSet.loc['2016-01-01':'2016-12-31']
#dataYear17=dataSet.loc['2017-01-01':'2017-12-31']
#dataYear18=dataSet.loc['2018-01-01':'2018-12-31']
#dataYear19=dataSet.loc['2019-01-01':'2019-12-31']
#dataYear20=dataSet.loc['2020-01-01':'2020-12-31']
#dataYear21=dataSet.loc['2021-01-01':'2021-12-31']
#dataYear22=dataSet.loc['2022-01-01':'2022-12-31']
#dataYear10.set_index()
print(dataYear10)
#dataYear08['Magnitud'].plot()
#dataSet.plot.scatter(x='Fecha',y ='Magnitud')
dataYear10.plot.scatter(x='Fecha',y ='Magnitud')
plt.show()
