A = int(input()) #nº de moedas
N = int(input()) #não contando o capitão

#cada marinheiro recebe x --> N marinheiros recebem N*x
#capitao recebe 2x

#A = N*x + 2x
#A = x(N + 2)
#x = A / (N + 2)
#capitao recebe 2x

qtd_marinheiro = A / (N + 2)
qtd_capitao = int(2 * qtd_marinheiro)
print(qtd_capitao)