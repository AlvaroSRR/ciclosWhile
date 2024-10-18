n=int(input("cantidad de numeros: "))
num = [0] * n
promedio = 0
for i in range(0,n,1):
    num[i]=int(input("numero: "))
    promedio += num[i]
numMax=num[0]
numMin=num[0]
for i in range(1,n,1):
    if numMax < num[i]:
        numMax =num[i]
    if numMin> num[i]:
        numMin = num[i]
promedio = promedio/n
"""
nunMin = min(num)
numMax = max(num)
"""
print(f"minimo: {numMin}, maximo:{numMax}, promedio: {promedio}")