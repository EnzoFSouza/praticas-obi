a = int(input())
b = int(input())
c = int(input())
d = int(input())

lista_niveis = [a, b, c, d]

maior = max(lista_niveis)
lista_niveis.remove(maior)

menor = min(lista_niveis)
lista_niveis.remove(menor)

soma1 = maior + menor
soma2 = sum(lista_niveis)

print(abs(soma1 - soma2))