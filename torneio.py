partidas = list()
for i in range(6):
    partidas.append(input())

vitorias = partidas.count("V")
if vitorias == 0:
    print(-1)

elif vitorias <= 2:
    print(3)

elif vitorias <= 4:
    print(2)

else:
    print(1)