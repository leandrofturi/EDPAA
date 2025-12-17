from heap import Heap
from graph import Graph

INF = float("inf")


class Dijkstra:
    """Caminhos minimos via Dijkstra a partir de src."""

    def __init__(self, g: Graph, src: int):
        n = g.n
        self.src = src
        self.dist = [INF] * n
        self.parent = [-1] * n

        self.dist[src] = 0.0
        self.parent[src] = src

        heap = [(0.0, src)]  # (dist, vertex)

        while heap:
            d_u, u = heapq.heappop(heap)

            # Entrada desatualizada no heap: já encontramos uma dist melhor
            if d_u > self.dist[u]:
                continue

            for v, w in g.adj[u]:
                nd = d_u + w
                if nd < self.dist[v]:
                    self.dist[v] = nd
                    self.parent[v] = u
                    heapq.heappush(heap, (nd, v))

    def path_to(self, v: int):
        """Retorna lista de vértices do destino até a origem."""
        if self.dist[v] == INF:
            return [v]
        path = []
        cur = v
        while True:
            path.append(cur)
            if cur == self.src:
                break
            cur = self.parent[cur]
        return path  # v <- ... <- src
