#crear matriz n°1
matrizNombre = []
for k in range(10):
    matrizNombre.append([0]*10)
for k in range(10):
    for i in range(10):
        print(" ",matrizNombre[k][i],end="")
    print(" ")

#crear matriz n°2
matriz =[[str() for ind0 in range(4)]for ind1 in range(4)]
for i in range(4):
    for j in range(4):
        matriz[i][j]= "x"
for i in range(4):
    for j in range(4):
        print(f'  {matriz[i][j]}',end="")
    print("")