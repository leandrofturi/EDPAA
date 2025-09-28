from Fracao import Fracao, mdc

x = Fracao(3, 4)
y = Fracao(5, 12)
z = Fracao()

print(x + y)  # 7/6

z = x + y
print(z)  # 7/6

print(mdc(6, -9))  # 3
print(mdc(-6, 9))  # 3
print(mdc(-6, -9))  # 3
print(mdc(6, 9))  # 3

a = Fracao(2, 4)
b = Fracao(1, 2)
print(a == b)  # True
print(a + b)  # 1/1
print(a * b)  # 1/4
print(a / b)  # 1/1


################################################################################


from Conjunto import Conjunto
from Conjunto import (
    Elimina_Repetidos, 
    Elimina_Repetidos_set, 
    Elimina_Repetidos_dict, 
    Elimina_Repetidos_list_set
)

x = Conjunto([1, 2, 25, 5, 72, 5, 1])
print(len(x))  # 5
print(x)  # *[1, 2, 5, 25, 72]

y = Conjunto([])
print(len(y))  # 0
print(y)  # *[]

z = Conjunto([1, 9, 113, 5, 9, 2, 22, 12, 2, 11])
print(len(z))  # 8
print(z)  # *[1, 2, 5, 9, 11, 12, 22, 113]

t = x + z
print(t)      # *[1, 2, 5, 9, 11, 12, 22, 25, 72, 113]
print(x + z)  # *[1, 2, 5, 9, 11, 12, 22, 25, 72, 113]

x = [1, 2, 25, 5, 72, 5, 1]
print(Elimina_Repetidos(x))           # [2, 25, 72, 5, 1]
print(Elimina_Repetidos_set(x))       # [1, 2, 5, 72, 25]
print(Elimina_Repetidos_dict(x))      # [1, 2, 25, 5, 72]
print(Elimina_Repetidos_list_set(x))  # [1, 2, 25, 5, 72]

a = Conjunto([1, 2, 3, 2])
b = Conjunto([3, 2, 1])
c = Conjunto([1, 4])
vazio = Conjunto()

a == b  # True
not (a == c)  # True

(a + c) == Conjunto([1, 2, 3, 4])  # True

(a * c) == Conjunto([1])  # True
(a * vazio) == Conjunto([])  # True

(a - c) == Conjunto([2, 3])  # True
(c - a) == Conjunto([4])  # True

len(a)  # 3
len(Conjunto([1, 1, 1]))  # 1

2 in a  # True
99 not in a  # True

Conjunto([1]) < a  # True
a > Conjunto([1])  # True

d = Conjunto([1, 2])
d += 3
d == Conjunto([1, 2, 3])  # True
d -= 2
d == Conjunto([1, 3])  # True

str(a)  # *[1, 2, 3]


################################################################################


from Polinomio import Polinomio

p1 = Polinomio([1.0, -2.2, 3.5])
v = p1.valor(1.0)
print(v)  # 2.3

p = Polinomio([2, 3, 4])  # 2 + 3x + 4x^2
q = Polinomio([1, 0, -1, 1])  # 1 - x^2 + x^3

print((p + q))  # 3 + 3x + 3x^2 + x^3
print((p - q))  # 1 + 3x + 5x^2 - x^3
print((p * q))  # 2 + 3x + 2x^2 - x^3 + x^5 + 4x^6

print((p + Polinomio([0])))  # 2 + 3x + 4x^2
print((p - Polinomio([0])))  # 2 + 3x + 4x^2
print((p * Polinomio([0])))  # +0 + 0x + 0x^2

Q, R = p / q
print(Q)  # 0
print(R)  # +2 + 3x + 4x^2
Q, R = p / Polinomio([0]) # error
Q, R = q / p
print(Q)  # -0.4375 + 0.25x
print(R)  # +1.875 + 0.8125x

print(p.derivate())  # 3 + 8x
print(p.integrate(C=5))  # 5 + 2x + 1.5x^2 + (4/3)x^3


################################################################################


from Matriz import Matriz

ma = Matriz(2, 3)
mb = Matriz(2, 3)
print(ma)

ma[0] = [1, 2, 3]
print(ma)

ma[1] = [4, 5, 6]
mb[0] = [5, 5, 5]
mb[1] = [9, 9, 9]

print(ma)
print(mb)

mc = ma + mb
print(mc)

A = Matriz(2, 3, [[1, 2, 3],
                  [4, 5, 6]])

B = Matriz(2, 3, [[7,  8,  9],
                  [10, 11, 12]])

print(A + B)
# Matriz 2x3
# [8, 10, 12]
# [14, 16, 18]

print(A - B)
# Matriz 2x3
# [-6, -6, -6]
# [-6, -6, -6]

C = Matriz(3, 2, [[1, 4],
                  [2, 5],
                  [3, 6]])

print(A * C)
# Matriz 2x2
# [14, 32]
# [32, 77]

_ = A * B
# mensagem de incompatibilidade de dimensões

print(A[0])  # [1, 2, 3]
A[0] = [100, 200, 300]
print(A[0])  # [100, 200, 300]