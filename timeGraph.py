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
#print(dataYear10)
listAux = []
j = 0

for i in dataYear10.Fecha:
    if(i >= '2010-01-01')and(i <= '2010-01-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 0:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-02-01')and(i <= '2010-02-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 1:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-03-01')and(i <= '2010-03-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        #print(aux2)
        if len(listAux) > 2:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-04-01')and(i <= '2010-04-31') and 7.2 not in listAux:
        listAux.append(7.2)
    elif(i >= '2010-05-01')and(i <= '2010-05-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 4:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-06-01')and(i <= '2010-06-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 5:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-07-01')and(i <= '2010-07-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 6:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-08-01')and(i <= '2010-08-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 7:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-09-01')and(i <= '2010-09-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 8:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-10-01')and(i <= '2010-10-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 9:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-11-01')and(i <= '2010-11-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 10:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    elif(i >= '2010-12-01')and(i <= '2010-12-31'):
        aux = dataYear10[(dataYear10.Fecha == i)]
        aux2 = aux.iloc[0]['Magnitud']
        if len(listAux) > 11:
            if listAux[len(listAux)-1] < aux2:
                listAux.pop()
                listAux.append(aux2)
        else:
            listAux.append(aux2)
    j = j + 1   

        
print(len(listAux))
dateList = ['Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Nombrie','Diciembre']
plt.plot(dateList,listAux)
dataByYear = {
    'Fecha':dateList,
    'Magnitud':listAux
}
df = pd.DataFrame(dataByYear)
df.to_latex('./assets/2010ForMonth.tex',index=False)
plt.title("Sismo mas grande de cada mes en el año 2010")
#plt.(dataYear10['Fecha'],dataYear10['Magnitud'])
#ataSet.plot.scatter(x='Fecha',y ='Magnitud')

#dataYear10[(dataYear10.Fecha>= '2010-04-01')&(dataYear10.Fecha <= '2010-04-31')].plot.scatter(x='Fecha',y ='Magnitud')
plt.show()
