from Fila import Fila

# testes da classe Fila
f = Fila()
# enfila 1, 3 e 5 nesta ordem
f.enqueue(1)
f.enqueue(3)
f.enqueue(5)
# mostra início e fim da fila
print("inicio:", f.first(), "fim:", f.last())
# remove e mostra os dois primeiros 1 e 3
print("desenfila:", f.dequeue())
print("desenfila:", f.dequeue())
# mostra início e fim da fila
print("inicio:", f.first(), "fim:", f.last())



from FilaLista import FilaLista

# teste das funções - fila de 3 elementos
F = FilaLista()
# adicionar 4 elementos
for k in [32, 45, 12, 27]:
   if F.enqueue(k): print(k, " adicionado com sucesso")
   else: print(k, "não foi adicionado - fila cheia")
   F.print()
# retirar 2 elementos
print()
print(F.dequeue(), "foi removido")
F.print()
print(F.dequeue(), "foi removido")
F.print()
# primeiro elemento e tamanho
print()
print(F.first(), "é o primeiro elemento da fila")
print(len(F), "é o tamanho atual da fila")
# adicionar 1 elemento
print()
if F.enqueue(-1): print(-1, " adicionado com sucesso")
else: print(-1, "não foi adicionado - fila cheia")
F.print()

# retirar 3 elementos
print()
k = F.dequeue()
if k is not None: print(k, "foi removido")
else: print("fila vazia - nada foi removido")
F.print()

k = F.dequeue()
if k is not None: print(k, "foi removido")
else: print("fila vazia - nada foi removido")
F.print()

k = F.dequeue()
if k is not None: print(k, "foi removido")
else: print("fila vazia - nada foi removido")
F.print()


from random import randrange
MAXF = 5 # teste com fila de 5 elementos
# cria uma fila
NF = FilaLista(MAXF)
# operações sobre a fila
while True:
   k = randrange(2)
   if k == 0:
       # adiciona elemento
       x = randrange(100000)
       if NF.enqueue(x):
           print(x, "adicionado a fila")
       else:
           print(x, "não foi adicionado - fila cheia")
   else:
       # remove elemento
       x = NF.dequeue()
       if x is not None:
           print(x, "- removido com sucesso")
       else:
           print("nada foi removido - fila vazia")
   # mostra a fila
   NF.print()
   # espera um tempo
   entrada = input("")
