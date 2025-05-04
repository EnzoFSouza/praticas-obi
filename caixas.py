#caixa de tamanho X pode ser colocada dentro de Y se X < Y

#caixas de tamanho X e Y podem ser colocadas, lado a lado, dentro de uma caixa Z se
#(X + Y) < Z
num_viagens = 3
A = int(input())
B = int(input())
C = int(input())

if A < B: #pode colocar caixa A dentro de B, e nº de viagens diminui em 1
    num_viagens -= 1
    
    if B < C: #pode colocar caixa A dentro de B dentro de C, nº de viagens diminui em 1
        num_viagens -= 1
    
elif (A + B) < C: #pode colocar caixa A e B lado a lado dentro de C, nº de viagens diminui em 2
    num_viagens -= 2
    
elif A < C:
    num_viagens -= 1


print(num_viagens)