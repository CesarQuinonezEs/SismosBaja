for i in range(len(dataSet)):
    isInTarget = False
    for j in range(5):
            if(j == 0):
                #Para vallecitos
                #aux = dataSet.iloc[i,4]

                #Para agua blanca
                #aux = dataSet.iloc[i,5]

                #Laguna salda
                #aux = dataSet.iloc[i,6]

                #San miguel
                #aux = dataSet.iloc[i,7]

                #Cerro prieto
                aux = dataSet.iloc[i,8]
            else:
                if(aux < dataSet.iloc[i,j+4]):
                    isInTarget = True
                else:
                    isInTarget = False
    if isInTarget:
        date.append(dataSet.iloc[i,0])
        mag.append(dataSet.iloc[i,1])
        lat.append(dataSet.iloc[i,2])
        lon.append(dataSet.iloc[i,3])
dataGroup = pd.DataFrame({'Fecha': date,
                          'Magnitud':mag,
                          'Latitud':lat,
                          'Longitud':lon
                          })
print(dataGroup)
dataGroup.to_csv('assets/datosCerroPrieto.csv',index=False)