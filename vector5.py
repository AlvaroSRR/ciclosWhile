n=int(input("cantidad de nuneros: "))
num=[0]*n
par=[" "]*n
for i in range(n):
    num[i]=int(input("numeros: "))
    if num[i]%2 ==0:
        par[i]= "par"
    else:
        par[i]= "impar"

print(num)
print(par)