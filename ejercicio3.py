
"""
Leer una serie de números enteros. que contenga como máximo veinte elementos, en caso de
ingresar un valor negativo o la cantidad de números ingresados supere los veinte, detener
el proceso e informar mediante un mensaje cuántos son mayores que 100.
"""
from random import randint

estado = True
cantidadNumeros = 0
contadorMayor100 = 0
while estado:
    valor = int(randint(-50,500))
    cantidadNumeros += 1
    if cantidadNumeros <20:
        if valor >=0 :
            if valor> 100:
                contadorMayor100 += 1
        else:
            estado = False
    else:
        estado = False
print(f"Nº Mayores de 100: {contadorMayor100}, Numero Igresados {cantidadNumeros}")
