def criarEstado():
    dados = input() #str
    dados = dados.split(" ") #lista
    nome = dados[0]
    alcool = float(dados[1])
    gasolina = float(dados[2])
    estado_dict = {
        "nome": nome,
        "alcool": alcool,
        "gasolina": gasolina,
    }

    return estado_dict

def checkVantagem(estado):
    preco_max = 0.7 * estado["gasolina"]
    if estado["alcool"] <= preco_max:
        lista_vantagem.append(estado["nome"])

lista_dicts = list()
lista_vantagem = list()

N = int(input())

for i in range(N):
    lista_dicts.append(criarEstado())

for i in range(N):
    checkVantagem(lista_dicts[i])

if len(lista_vantagem) == 0:
    print("*")

else:
    for i in range(len(lista_vantagem)):
        print(lista_vantagem[i])