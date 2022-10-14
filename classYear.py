import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
yearsData = []
dataSet = pd.read_csv('datos.csv',usecols=['Fecha','Magnitud','Latitud','Longitud'],sep=',',index_col='Fecha')
#print(dataSet.loc['2009-09-19':'2009-12-30'])
yearsData.append(dataSet.loc['2000-01-01':'2000-12-31'])
yearsData.append(dataSet.loc['2001-01-01':'2001-12-31'])
yearsData.append(dataSet.loc['2002-01-01':'2002-12-31'])
yearsData.append(dataSet.loc['2003-01-01':'2003-12-31'])
yearsData.append(dataSet.loc['2004-01-01':'2004-12-31'])
yearsData.append(dataSet.loc['2005-01-01':'2005-12-31'])
yearsData.append(dataSet.loc['2008-01-01':'2008-12-31'])
yearsData.append(dataSet.loc['2009-09-19':'2009-12-30'])
yearsData.append(dataSet.loc['2010-01-01':'2010-12-31'])
yearsData.append(dataSet.loc['2011-01-01':'2011-12-31'])
yearsData.append(dataSet.loc['2012-01-01':'2012-12-31'])
yearsData.append(dataSet.loc['2013-01-01':'2013-12-31'])
yearsData.append(dataSet.loc['2014-01-01':'2014-12-31'])
yearsData.append(dataSet.loc['2015-01-01':'2015-12-31'])
yearsData.append(dataSet.loc['2016-01-01':'2016-12-31'])
yearsData.append(dataSet.loc['2017-01-01':'2017-12-31'])
yearsData.append(dataSet.loc['2018-01-01':'2018-12-31'])
yearsData.append(dataSet.loc['2019-01-01':'2019-12-31'])
yearsData.append(dataSet.loc['2020-01-01':'2020-12-31'])
yearsData.append(dataSet.loc['2021-01-01':'2021-12-31'])
yearsData.append(dataSet.loc['2022-01-01':'2022-09-30'])

for i in yearsData:
    print("------------------------------------------------")
    print(i)
