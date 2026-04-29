import numpy as np

class Sinal:
    def __init__(self, valores, n0=0):
        self.valores = np.array(valores, dtype=complex)
        self.n0 = n0  # índice inicial

    def indices(self):
        return np.arange(self.n0, self.n0 + len(self.valores))

    def __str__(self):
        return f"valores={self.valores}, n0={self.n0}"
    
def convolucao_exponencial_teorica(h: Sinal, a, k_min, k_max):
    a = complex(a)

    n = h.indices()

    #Calcula R = soma h(n) * a^{-n}
    R = np.sum(h.valores * (a ** (-n)))

    #Agora gera saída y[k] = R * a^k
    k = np.arange(k_min, k_max + 1)
    y = R * (a ** k)

    return Sinal(y, n0=k_min)
    
#h(n) definido de n = -2 até 2
h = Sinal([1, 2, 3, 2, 1], n0=-2)

a = 0.8 + 0.2j

y = convolucao_exponencial_teorica(h, a, k_min=-5, k_max=10)

print("h:", h)
print("Saída y:", y)