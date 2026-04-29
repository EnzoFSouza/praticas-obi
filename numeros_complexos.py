import math

# Classe Complexo
class Complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    #Definir como o numero será exibido ao utilizar print
    def __str__(self):
        return f"{self.real:.4f} + {self.imag:.4f}j"

    #Conversão de retangular para polar
    def para_polar(self):
        r = math.sqrt(self.real**2 + self.imag**2)
        theta = math.atan2(self.imag, self.real)
        return r, theta

    #Conversão de polar para retangular
    #@classmethod faz com que o método pertença a classe como um todo, e não somente a um objeto
    #método construtor alternativo, pois cria o objeto a partir de r e theta
    @classmethod 
    def de_polar(cls, r, theta):
        real = r * math.cos(theta)
        imag = r * math.sin(theta)
        return cls(real, imag)
        #cls --> referência a classe
        #Cria e retorna um objeto
        #Equivalente a return Complexo(real, imag)

    #Soma (retangular)
    def __add__(self, outro):
        return Complexo(
            self.real + outro.real,
            self.imag + outro.imag
        )

    # Subtração (retangular)
    def __sub__(self, outro):
        return Complexo(
            self.real - outro.real,
            self.imag - outro.imag
        )

    # Multiplicação (polar)
    def __mul__(self, outro):
        r1, t1 = self.para_polar()
        r2, t2 = outro.para_polar()

        r = r1 * r2
        theta = t1 + t2

        return Complexo.de_polar(r, theta)

    def __truediv__(self, outro):
        r1, t1 = self.para_polar()
        r2, t2 = outro.para_polar()

        if r2 == 0:
            raise ZeroDivisionError("Divisão por zero!")

        r = r1 / r2
        theta = t1 - t2

        return Complexo.de_polar(r, theta)



# Entrada de dados
def ler_numero_complexo():
    tipo = input("Digite o tipo (1 = Retangular, 2 = Polar): ")

    if tipo == "1":
        a = float(input("Parte real: "))
        b = float(input("Parte imaginária: "))
        z = Complexo(a, b)

    elif tipo == "2":
        r = float(input("Módulo (r): "))
        theta = float(input("Ângulo (em radianos): "))
        z = Complexo.de_polar(r, theta)

    else:
        print("Opção inválida.")
        return None

    return z


print("Número complexo 1:")
z1 = ler_numero_complexo()

print("\nNúmero complexo 2:")
z2 = ler_numero_complexo()

# Operações
soma = z1 + z2
sub = z1 - z2
mult = z1 * z2
div = z1 / z2

# Impressão
def imprimir_resultado(nome, z):
    r, theta = z.para_polar()
    print(f"\n{nome}:")
    print(f"Forma retangular: {z}")
    print(f"Forma polar: {r:.4f} ∠ {theta:.4f} rad")

imprimir_resultado("Soma", soma)
imprimir_resultado("Subtração", sub)
imprimir_resultado("Multiplicação", mult)
imprimir_resultado("Divisão", div)