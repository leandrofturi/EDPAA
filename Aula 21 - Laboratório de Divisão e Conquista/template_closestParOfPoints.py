import math
import sys

def dist(p1, p2):
    pass

def closest_pair_rec(px, py):
   pass


def closest_pair(points):
    pass


'''
--------------------------
    LEITURA DA ENTRADA
--------------------------
'''
def main():
    for linha in sys.stdin:
        N = int(linha.strip())
        if N == 0:
            break

        pontos = []
        for _ in range(N):
            x, y = map(int, sys.stdin.readline().split())
            pontos.append((x, y))

        resposta = closest_pair(pontos)

        if resposta >= 10000:
            print("INFINITY")
        else:
            print(f"{resposta:.4f}")


if __name__ == "__main__":
    main()


'''
Análise do comportamento pela relação de recorrência:
'''