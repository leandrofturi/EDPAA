# Função mdc
def mdc(n, m):
    resto = n % m
    while resto != 0:
        n = m
        m = resto
        resto = n % m
    return abs(m)


class Fracao:
    # Define o TAD Fracao

    # Construtor da classe
    def __init__(self, topo = 0, base = 1):
        # Cria uma instância de Fracao
        if base == 0:
            raise ValueError("Denominador igual a zero!\n")
        self.num = topo
        self.den = base

        if self.den < 0:  # denominador sempre positivo
            self.num *= -1
            self.den *= -1

    # Retorna a soma de dois elementos do TAD
    def __add__(self, f2):
        xnum = self.num * f2.den + self.den * f2.num
        xden = self.den * f2.den
        xmdc = mdc(xnum, xden)
        return Fracao(xnum // xmdc, xden // xmdc)

    # Retorna a diferença de dois elementos do TAD
    def __sub__(self, f2):
        f2_neg = Fracao(-f2.num, f2.den)
        return self.__add__(f2_neg)

    # Retorna o produto de dois elementos do TAD
    def __mul__(self, f2):
        xnum = self.num * f2.num
        xden = self.den * f2.den
        xmdc = mdc(xnum, xden)
        return Fracao(xnum // xmdc, xden // xmdc)

    # Retorna a razão de dois elementos do TAD
    def __truediv__(self, f2):
        f2_inv = Fracao(f2.den, f2.num)
        return self.__mul__(f2_inv)
    
    # Transforma em string para o print
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    # Compara dois elementos do TAD
    def __eq__(self, f2):
        pri_fator = self.num * f2.den
        seg_fator = self.den * f2.num
        return pri_fator == seg_fator

    # Compara dois elementos do TAD
    def __gt__(self, f2):
        pri_fator = self.num * f2.den
        seg_fator = self.den * f2.num
        return pri_fator > seg_fator

    # Compara dois elementos do TAD
    def __lt__(self, f2):
        pri_fator = self.num * f2.den
        seg_fator = self.den * f2.num
        return pri_fator < seg_fator

    # Compara dois elementos do TAD
    def __ge__(self, f2):
        return self.__gt__(f2) or self.__eq__(f2)

    # Compara dois elementos do TAD
    def __le__(self, f2):
        return self.__lt__(f2) or self.__eq__(f2)
    
    # Compara dois elementos do TAD
    def __ne__(self, f2):
        return not self.__eq__(f2)
