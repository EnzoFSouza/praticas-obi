N = int(input())
soma = 0
termos = list()
for i in range(N):
    termos.append(input()) #Os valores serao salvos com string

for i in range(N):
    potencia = int(termos[i][len(termos[i]) - 1])
    num_original = int(termos[i][:len(termos[i]) - 1])
    soma += num_original ** potencia

print(soma)