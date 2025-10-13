class Empty(Exception):
   # Nova excessão - sub classe de Exception
   pass

class Full(Exception):
   # Nova excessão - sub classe de Exception
   pass


class FilaDupla:
    # MAXF define o tamanho máximo da fila.
    def __init__(self, MAXF=3):
        self._fila = [None] * MAXF
        self._size = 0
        self._front = -1
        self._end = -1
        self.MAXF = MAXF
        self._MAXF = MAXF
    
    # Adiciona um elemento no final da fila
    def enqueue_end(self, x):
        # verifica se a fila está cheia
        if self._size == self.MAXF: return False
        self._end = (self._end + 1) % self.MAXF
        self._fila[self._end] = x
        # se é o primeiro elemento altera também o inicio
        if self.is_empty(): self._front = 0
        self._size = self._size + 1
    
        if self._size == self.MAXF:
            self._resize(2*len(self._fila))
        
        return True
    
    def enqueue_front(self, x):
        # verifica se a fila está cheia
        if self._size == self.MAXF: return False
        self._front = (self._front - 1)
        if self._front < 0:
            self._front = self.MAXF - 1
        self._fila[self._front] = x
        # se é o primeiro elemento altera também o inicio
        if self.is_empty(): self._end = self.MAXF - 1
        self._size = self._size + 1
        
        if self._size == self.MAXF:
            self._resize(2*len(self._fila))
        
        return True
    
    # Remove um elemento do fim da fila
    def dequeue_front(self):
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
        
        if 0 < self._size < len(self._fila) // 4:
            self._resize(len(self._fila) // 2)
        
        return x
    
    def dequeue_end(self):
        if self.is_empty(): return None
        x = self._fila[self._end]
        self._fila[self._end] = None
        self._size = self._size - 1
        # verifica se a fila vai ficar vazia
        # neste caso, ambos os ponteiros ficam -1
        if self._front == self._end:
            self._front = self._end = -1
        else:
            self._end = (self._end - 1)
            if self._end < 0:
                self._end = self.MAXF - 1
        
        if 0 < self._size < len(self._fila) // 4:
            self._resize(len(self._fila) // 2)
        
        return x
    
    # Retorna True se a fila está vazia
    def is_empty(self):
        return self._size == 0
    
    # Devolve o primeiro elemento da fila sem removê-lo
    def first(self):
        if self.is_empty(): return None
        return self._fila[self._front]
    
    def last(self):
        if self.is_empty(): return None
        return self._fila[self._end]
    
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
    
    def _resize(self, newsize):
        print("resize")
        fila_antiga = self._fila # guarda a fila antiga
        front_antigo = self._front
        size_antigo = self._size
        MAXF_antigo = self.MAXF
        
        self._fila = [None] * newsize
        self._front, self._end = -1, -1
        self.MAXF = newsize
        self._size = 0
        
        # reinsere os elementos na fila_antiga para self_fila
        for i in range(size_antigo):
            self.enqueue_end(fila_antiga[(i + front_antigo) % MAXF_antigo])
