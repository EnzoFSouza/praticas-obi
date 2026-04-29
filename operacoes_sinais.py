import numpy as np
import matplotlib.pyplot as plt

class Sinal:

    def __init__(self, valores):
        self.valores = np.array(valores, dtype=complex)

    def __str__(self):
        return str(self.valores)

    #Soma
    def __add__(self, outro):
        tamanho = max(len(self.valores), len(outro.valores))

        x_pad = np.pad(self.valores, (0, tamanho - len(self.valores)), mode='constant')
        y_pad = np.pad(outro.valores, (0, tamanho - len(outro.valores)), mode='constant')

        return Sinal(x_pad + y_pad)

    #Multiplicação ponto a ponto
    def __mul__(self, outro):
        tamanho = max(len(self.valores), len(outro.valores))

        x_pad = np.pad(self.valores, (0, tamanho - len(self.valores)), mode='constant')
        y_pad = np.pad(outro.valores, (0, tamanho - len(outro.valores)), mode='constant')

        return Sinal(x_pad * y_pad)

    #Deslocamento
    def deslocamento(self, k):
        if k > 0:
            novo = np.pad(self.valores, (k, 0), mode='constant')
        else:
            novo = self.valores[abs(k):]

        return Sinal(novo)

    #Expansão
    def expansao(self, k):
        if k <= 0:
            raise ValueError("k deve ser positivo")

        novo = np.zeros(len(self.valores) * k, dtype=complex)
        novo[::k] = self.valores

        return Sinal(novo)

    #Contração
    def contracao(self, k):
        if k <= 0:
            raise ValueError("k deve ser positivo")

        novo = self.valores[::k]
        return Sinal(novo)
    
    #Plotar
    def plot(self, titulo="Sinal"):
        n = np.arange(len(self.valores))

        plt.figure()

        # Parte real
        plt.subplot(2, 1, 1)
        plt.stem(n, self.valores.real)
        plt.title(titulo + " - Parte Real")
        plt.grid()

        # Parte imaginária
        plt.subplot(2, 1, 2)
        plt.stem(n, self.valores.imag)
        plt.title(titulo + " - Parte Imaginária")
        plt.grid()

        plt.tight_layout()
        plt.show()
    
x = Sinal([1, 2, 3, 4])
y = Sinal([1+1j, 2, 1])

print("Sinal x:", x)
print("Sinal y:", y)

print("\nSoma:")
soma = x + y
print(soma)

print("\nMultiplicação:")
mult = x * y
print(mult)

print("\nDeslocamento (2):")
print(x.deslocamento(2))

print("\nExpansão (2):")
print(x.expansao(2))

print("\nContração (2):")
print(x.contracao(2))

x.plot("Sinal x")
y.plot("Sinal y")
soma.plot("Soma")
mult.plot("Multiplicação")