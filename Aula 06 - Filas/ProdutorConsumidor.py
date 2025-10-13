"""
Implementar o problema do produtor e consumidor utilizando conceitos de sincronização do Python.
Roteiro:
Uma Thread em Python é um processo em execução ou uma linha de execução de um programa. A classe que contém um programa concorrente é uma classe “filha” da classe Thread e precisa de uma função de nome run.
A classe Condition especifica os elementos de sincronização entre os processos concorrentes. O sincronismo é implementado através dos métodos:
    - acquire() e release(): Bloqueia e desbloqueia um trecho de programa ou uma região crítica onde apenas um dos processos pode entrar por vez.
    - wait(): Coloca o processo em espera de uma notificação. Só pode ser emitida se o processo está bloqueado. Libera o bloqueio e coloca o processo em espera da notificação. Quando recebe a notificação o bloqueio é retomado.
    - notify(): Envia uma notificação a qualquer processo que esteja esperando esta notificação. Não libera o bloqueio imediatamente. O bloqueio só é liberado quando esse processo emitir um release().
    - <classe>().start(): Lança a Thread para execução (método run da Thread) e continua a execução normal do programa.
"""

import time
from random import randrange
import threading
from FilaLista import FilaLista


class Produtor(threading.Thread):
    contador = 0
    
    def __init__(self, queue, qtd_itens, identificador=0):
        Produtor.contador += 1
        identificador = Produtor.contador
        super().__init__(name=f"Prod-{identificador}")
        self.queue = queue
        self.qtd_itens = qtd_itens
    
    def run(self):
        for i in range(self.qtd_itens):
            item = randrange(100000)
            self.queue.enqueue(item)
            time.sleep(random.uniform(0.1, 0.6))
        print(f"[{self.name}] finalizou producao de {self.qtd_itens} itens")


class Consumidor(threading.Thread):
    contador = 0
    
    def __init__(self, queue, qtd_itens):
        Consumidor.contador += 1
        identificador = Consumidor.contador
        super().__init__(name=f"Cons-{identificador}")
        self.queue = queue
        self.qtd_itens = qtd_itens
        self.processados = 0
    
    def run(self):
        for _ in range(self.qtd_itens):
            _ = self.queue.dequeue()
            self.processados += 1
            time.sleep(random.uniform(0.2, 0.7))
        print(f"[{self.name}] finalizou consumo de {self.qtd_itens} itens")


class Sincronizador:
    def __init__(self, capacidade=3):
        self.fila = FilaLista(capacidade)
        self.cond = threading.Condition()
    
    def enqueue(self, item):
        self.cond.acquire()
        try:
            while self.fila.is_full():
                print(f"fila cheia, esperando...")
                self.cond.wait()
            
            self.fila.enqueue(item)
            print(f"produziu: {item}")
            time.sleep(random.uniform(0.1, 0.4))
            
            self.cond.notify() # Avisa que há um novo item
        finally:
            self.cond.release()
    
    def dequeue(self):
        self.cond.acquire()
        try:
            while self.fila.is_empty():
                print(f"fila vazia, esperando...")
                self.cond.wait()
            
            item = self.fila.dequeue()
            print(f"[consumiu: {item}")
            time.sleep(random.uniform(0.2, 0.5))
            
            self.cond.notify() # Avisa que há espaço disponível
            return item
        finally:
            self.cond.release()
