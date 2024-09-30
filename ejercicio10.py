# carga de cantidad de dias
periodo= int(input("ingrese cantidad de dias: "))
#creo la variable auxiliar "i" y la seteo en 0
i=0
#ciclo while para cargar las temperaturas
while i < periodo:
    tempMin = float(input("temperatura minima: "))
    tempMax = float(input("temperatura maxima: "))
    if i == 0:
        minima = tempMin
        maxMin = tempMin
        minMax = tempMax
        maxima = tempMax
    #controlo que el valor de las temperaturas sea 99, asi finaliza el ciclo while
    if tempMin == 99 and tempMax == 99:
        # le doy un valor para que no se cumpla la condicion del ciclo while
        i = periodo + 1
    #controlo las temperaturas con las variables, para actualizar valores
    else:
        if minima > tempMin:
            minima= tempMin
        if maxMin < tempMin:
            maxMin = tempMin
        if maxima < tempMax:
            maxima = tempMax
        if minMax > tempMax:
            minMax = tempMax
        #incremento la variable en uno cada vez que repite el ciclo
        i = i + 1
#imprimo los resultados
print(f"temperatura minima :{minima}º")
print(f"temperatura minima mas alta :{maxMin}º")
print(f"temperatura maxima :{maxima}º")
print(f"temperatura Maxima mas baja:{minMax}º")