n = int(input("cantidad alumnos:"))
nombre=[" "]*n #defino el array, el tamaño y el contenido
nota=[0]*n
print(nombre)
for i in range(0,n,1):
    nombre[i]= input("nombre: ")
    nota[i]= int(input("nota: "))

for i in range(0,n,1):
    print(f"nombre: {nombre[i]}")
    print(f"nota: {nota[i]}")