from random import random, randint

i=0
cont100 = 0
while i < 50:
#    num = int(input("ingrese nº: "))
    num = randint(0,9999) #genera numeros random
    if num >100:
        cont100 = cont100 +1
        print(num)
    i= i+1
print(f"nº mayores a 100: {cont100}")
