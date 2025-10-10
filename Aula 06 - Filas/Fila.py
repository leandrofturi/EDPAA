class Fila:
    # inicia a fila - lista vazia
    def __init__(self):
        self.items = []
    # devolve True se fila está vazia e False senão
    def is_empty(self):
        return self.items == []
    # enfila novo elemento no final da fila
    def enqueue(self,item):
        self.items.append(item)
    # retira da fila o primeiro elemento
    def dequeue(self):
        if self.is_empty(): return None
        return self.items.pop(0)
    # devolve o valor do elemento do primeiro mas não remove 
    def first(self):
        if self.is_empty(): return None
        return self.items[0]
    # devolve o valor do elemento do último mas não remove 
    def last(self):
        if self.is_empty(): return None
        return self.items[-1]
    def size(self):
        return len(self.items)
