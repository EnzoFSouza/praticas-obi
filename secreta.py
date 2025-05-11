sequencia = list()
marcados = list()
N = int(input())
for i in range(N):
    sequencia.append(int(input()))

anterior = sequencia[0]
marcados.append(anterior)
for i in range(1, N):
    if sequencia[i] != anterior:
        marcados.append(sequencia[i])
        anterior = sequencia[i]

print(len(marcados))