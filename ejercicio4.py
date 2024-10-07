from random import randint
"""
Se dispone de diez pares ordenados (X,y) de números. a los cuales se debe calcular la suma
de todas las X y la suma de todas las Y, imprimir los resultados.
"""
suma1=0
suma2=0
i=0
while i <10:
    valor1=int(randint(0,1000))
    valor2=int(randint(0,1000))
    suma1 += valor1
    suma2 += valor2
    i += 1
print(f"Suma X: {suma1}, Suma Y: {suma2}")