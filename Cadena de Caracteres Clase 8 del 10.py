"""
se debe calcular e imprimir el producto de todas las X Y de todas las y de cincuenta pares
ordenados de números enteros.
"""
#muerta cual es el mas largo
#nombre1 = input("nombre: ").upper()
#nombre2 = input("nombre: ").upper()
#if len(nombre1.replace(" ","")) > len(nombre2.replace(" ", "")):
#    print("el primer nombre es elmas largo")
#else:
#    print("el segundo nombre es mas largo")

#cuenta los caracteres de la variable y borra los espacios
#nombre = input("nombre: ").upper()
#print(f"{nombre} tiene {len(nombre.replace(" ",""))}")

#muestra primera y ultima letra
#nombre=input("nombre: ")
#print(nombre[0])
#print(nombre[(len(nombre))-1])


num=input("numero: ")
    num.replace(6,"")

print(num)
cont =len(num)
for i in range(0,cont-1):
    if num[i]>"5":
        letra=num[i]
        num = num.replace(letra.__str__(),"")
print(num)
"""
print(nombre.upper())
print(nombre.lower())
print(nombre.swapcase())
print(nombre.title())
print(nombre.capitalize())
"""