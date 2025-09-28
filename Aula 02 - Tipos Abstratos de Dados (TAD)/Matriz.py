class Matriz:
    def __init__(self, m, n, dados=None):
        self.m = m
        self.n = n
        self.dados = [0] * m
        for i in range(m):
            if dados:
                self.dados[i] = dados[i][:]
            else:
                self.dados[i] = [0] * n
    
    def __add__(s1, s2):
        if s1.m != s2.m or s1.n != s2.n:
            raise RuntimeError(f"Dimensão {s1.m}x{s1.n} não compativel com {s2.m}x{s2.n}.")

        d = [0] * s1.m
        for i in range(s1.m):
            d[i] = [0] * s1.n
            for j in range(s1.n):
                d[i][j] = s1.dados[i][j] + s2.dados[i][j]
        return Matriz(s1.m, s1.n, d)
           
    def __sub__(s1, s2):
        if s1.m != s2.m or s1.n != s2.n:
            raise RuntimeError(f"Dimensão {s1.m}x{s1.n} não compativel com {s2.m}x{s2.n}.")

        d = [0] * s1.m
        for i in range(s1.m):
            d[i] = [0] * s1.n
            for j in range(s1.n):
                d[i][j] = s1.dados[i][j] - s2.dados[i][j]
        return Matriz(s1.m, s1.n, d)

    def __mul__(s1, s2):
        if s1.n != s2.m:
            raise RuntimeError(f"Dimensão {s1.m}x{s1.n} não compativel com {s2.m}x{s2.n}.")

        d = [0] * s1.m
        for i in range(s1.m):
            d[i] = [0] * s2.n
            for k in range(s1.n):
                aik = s1.dados[i][k]
                for j in range(s1.n):
                    d[i][j] += aik * s2.dados[k][j]
        return Matriz(s1.m, s2.n, d)

    def __str__(self):
        s = f"Matriz {self.m}x{self.n}"
        for i in range(self.m):
            s += "\n[" + str(self.dados[i]) + "]"
        return s
    
    # leitura com []
    def __getitem__(self, idx):
        return self.dados[idx]

    # atribuição com []
    def __setitem__(self, idx, valor):
        self.dados[idx] = valor
    