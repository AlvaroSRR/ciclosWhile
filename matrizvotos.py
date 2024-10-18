votos =[]
for k in range(6):
    votos.append([""]*5)

votos[0][0]="Distrito"
votos[0][1]="Candidato A"
votos[0][2]="Candidato B"
votos[0][3]="Candidato C"
votos[0][4]="Candidato D"

for i in range(1,5):
    votos[i][0]= input("codigo distrito: ")
    for k in range(1,4):
        votos[i][k]= input(f"votos {votos[0][k]}: ")

for i in range(6):
    for k in range(5):
        print(f"{votos[i-1][k-1]}  ", end="")
    print("")