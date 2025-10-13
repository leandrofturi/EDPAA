class Empty(Exception):
   # Nova excessão - sub classe de Exception
   pass

class Full(Exception):
   # Nova excessão - sub classe de Exception
   pass


class FilaLista:
    # MAXF define o tamanho máximo da fila.
    def __init__(self, MAXF=3):
        self._fila = [None] * MAXF
        self._size = 0
        self._front = -1
        self._end = -1
        self.MAXF = MAXF
    
    # Adiciona um elemento no final da fila
    def enqueue(self, x):
        # verifica se a fila está cheia
        if self._size == self.MAXF: return False
        self._end = (self._end + 1) % self.MAXF
        self._fila[self._end] = x
        # se é o primeiro elemento altera também o inicio
        if self.is_empty(): self._front = 0
        self._size = self._size + 1
        
        return True
    
    # Remove um elemento do fim da fila
    def dequeue(self):
        if self.is_empty(): return None
        x = self._fila[self._front]
        self._fila[self._front] = None
        self._size = self._size - 1
        # verifica se a fila vai ficar vazia
        # neste caso, ambos os ponteiros ficam -1
        if self._front == self._end:
            self._front = self._end = -1
        else:
            self._front = (self._front + 1) % self.MAXF
        
        return x
    
    # Retorna True se a fila está vazia
    def is_empty(self):
        return self._size == 0
    
    # Retorna True se a fila está vazia
    def is_full(self):
        return self._size == self.MAXF
    
    # Devolve o primeiro elemento da fila sem removê-lo
    def first(self):
        if self.is_empty(): return None
        return self._fila[self._front]
    
    # Retorna o tamanho atual da fila
    def __len__(self):
        return self._size
    
    # Mostra o conteúdo da fila - apenas para teste
    #def print(self):
    #     print(self._fila)
    
    def print(self):
        # mostra a fila
        print("* * * status da fila * * *")
        for k in range(self.MAXF):
            if self._fila[k] is None: print('Vazio', end = ' | ')
            else: print("%05d" %self._fila[k], end = ' | ')
        print()
        # mostra os índices
        for k in range(self.MAXF): print('%-8d' %k, end = '')
        print()
        # mostra o início e o fim
        print("i =", self._front, " f =", self._end)
        print()
