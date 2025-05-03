def checarEscher(lista):
    soma = lista[0] + lista[N - 1]
    for i in range(N):
        if lista[i] + lista[N - 1 - i] != soma:
            print("N")
            return
        
    print("S")

N = int(input())
dados = input()
dados = dados.split(" ")
sequencia = list()
for i in range(N):
    sequencia.append(int(dados[i]))

checarEscher(sequencia)