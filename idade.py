lista_idades = list()    
for i in range(3):
    lista_idades.append(int(input()))

maior_idade = max(lista_idades)
menor_idade = min(lista_idades)

#.remove() removes first occurrence of value
lista_idades.remove(maior_idade)
lista_idades.remove(menor_idade)

print(lista_idades[0])