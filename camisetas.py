N = int(input())
dados = input()
dados = dados.split()
tamanho_pequeno = dados.count("1")
tamanho_medio = dados.count("2")
P = int(input())
M = int(input())

if tamanho_pequeno == P and tamanho_medio == M:
    print("S")

else:
    print("N")