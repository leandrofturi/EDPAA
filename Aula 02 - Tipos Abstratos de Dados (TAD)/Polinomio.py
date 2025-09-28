class Polinomio:
    # Define a classe Polinomio
    
    def __init__(s, coef):
        s.cfs = coef[:] # coeficientes    
    
    # Devolve o valor do polinômio no ponto x
    def valor(self, x):
        soma = 0
        for k in range(len(self.cfs)):
            soma += self.cfs[k] * pow(x, k)
        return soma

    def __get_sgn(self, x):
        if x >= 0:
            return "+"
        return "-"

    def __str__(self):
        s = ""
        for i in range(len(self.cfs)):
            x = self.cfs[i]
            signx = self.__get_sgn(x)
            if i == 0:
                s += f"{signx}{abs(x)}"
            elif i == 1:
                s += f" {signx} {abs(x)}x"
            else:
                s += f" {signx} {abs(x)}x^{i}"
        return s
        
    def __add__(self, p2):
        n1 = len(self.cfs)
        n2 = len(p2.cfs)
        n_max = max(n1, n2)
        cfs = [0] * n_max
        
        for i in range(n_max):
            a = self.cfs[i] if i < n1 else 0
            b = p2.cfs[i] if i < n2 else 0
            cfs[i] = a + b
        
        return Polinomio(cfs)

    def __sub__(self, p2):
        n2 = len(p2.cfs)
        p2_neg = [0] * n2
        for i in range(n2):
            p2_neg[i] = - p2.cfs[i]
        return self.__add__(Polinomio(p2_neg))

    def __mul__(self, p2):
        n1 = len(self.cfs)
        n2 = len(p2.cfs)
        n = n1 + n2 - 1
        cfs = [0] * n
        
        for i in range(n1):
            ai = self.cfs[i]
            if ai == 0:
                continue
            for j in range(n2):
                cfs[i + j] += ai * p2.cfs[j]
        
        return Polinomio(cfs)

    def __truediv__(self, p2):
        # https://stackoverflow.com/questions/26173058/division-of-polynomials-in-python
        if len(p2.cfs) == 0 or all(c == 0 for c in p2.cfs):
            raise ZeroDivisionError("Divisão por polinômio nulo.")

        def normalize(p):
            while p and p[-1] == 0:
                p.pop()
            if p == []:
                p.append(0)

        num = self.cfs[:]
        normalize(num)
        den = p2.cfs[:]
        normalize(den)

        if len(num) >= len(den):
            # Shift den towards right so it's the same degree as num
            shiftlen = len(num) - len(den)
            den = [0] * shiftlen + den
        else:
            return [0], num

        quot = []
        divisor = float(den[-1])
        for _ in range(shiftlen + 1):
            # Get the next coefficient of the quotient.
            mult = num[-1] / divisor
            quot = [mult] + quot

            # Subtract mult * den from num, but don't bother if mult == 0
            # Note that when i==0, mult!=0; so quot is automatically normalized.
            if mult != 0:
                d = [mult * u for u in den]
                num = [u - v for u, v in zip(num, d)]

            num.pop()
            den.pop(0)

        normalize(num)
        return Polinomio(quot), Polinomio(num)

    def derivate(self):
        n = len(self.cfs) - 1
        if n <= 0:
            return Polinomio([0])
        cfs = [0] * n
        
        for i in range(n):
            cfs[i] = (i + 1) * self.cfs[i + 1]
        
        return Polinomio(cfs)

    def integrate(self, C=0):
        n = len(self.cfs) + 1
        cfs = [0] * n
        
        cfs[0] = C
        for i in range(1, n):
            cfs[i] = self.cfs[i - 1] / (i)
        
        return Polinomio(cfs)
