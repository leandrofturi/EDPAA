from pathlib import Path
from heap import PriorityHeap
from graph import Graph

INF = float("inf")


def log_error(errors_file, msg: str):
    if errors_file is not None:
        with open(errors_file, "a", encoding="utf-8") as ef:
            ef.write(msg + "\n")


class Dijkstra:
    """Caminhos mínimos via Dijkstra a partir de src."""

    def __init__(self, g: Graph, src: int, use_decrease_key=True, errors_file=None):
        if g is None:
            log_error(errors_file, "Grafo inválido: objeto Graph é None.")
            raise ValueError("Grafo inválido (None).")

        n = g.n
        if n <= 0:
            log_error(errors_file, "Grafo inválido: número de vértices <= 0.")
            self.src = src
            self.dist = []
            self.parent = []
            self.use_decrease_key = use_decrease_key
            return

        if not (0 <= src < n):
            log_error(errors_file, f"Origem inválida: src={src}, n={n}.")
            raise IndexError(f"Origem fora do intervalo: src={src}, n={n}.")

        self.src = src
        self.dist = [INF] * n
        self.parent = [-1] * n
        self.use_decrease_key = use_decrease_key

        self.dist[src] = 0.0
        self.parent[src] = src

        for u, adj_list in enumerate(g.adj):
            if adj_list is None:
                log_error(errors_file, f"Lista de adjacência None no vértice {u}.")
                raise ValueError(f"Lista de adjacência inválida no vértice {u}.")
            for v, w in adj_list:
                if not (0 <= v < n):
                    log_error(errors_file, f"Vértice destino inválido na aresta ({u} -> {v}).")
                    raise IndexError(f"Vértice destino inválido: {v} em ({u}->{v}).")
                if w < 0:
                    log_error(errors_file, f"Peso negativo detectado em ({u}->{v}) = {w}.")
                    raise ValueError("Grafo possui peso negativo; Dijkstra não é aplicável.")

        heap = PriorityHeap()

        for v in range(n):
            key = self.dist[v]
            heap.push(key, v)

        while not heap.is_empty():
            d_u, u = heap.pop_min()

            # se u for inalcançável, d_u = INF
            if d_u == INF:
                break

            if d_u != self.dist[u]:
                continue

            for v, w in g.adj[u]:
                nd = d_u + w
                if nd < self.dist[v]:
                    self.dist[v] = nd
                    self.parent[v] = u

                    if self.use_decrease_key:
                        try:
                            heap.decrease_key(v, nd)
                        except KeyError as e:
                            log_error(
                                errors_file,
                                f"decrease_key falhou para v={v} (dist={nd}): {e}"
                            )
                            heap.push(nd, v)
                    else:
                        heap.push(nd, v)

    def path_to(self, v: int, errors_file=None):
        """Retorna lista de vértices do destino até a origem."""
        if v < 0 or v >= len(self.dist):
            log_error(errors_file, f"path_to chamado com vértice inválido v={v}.")
            return []

        if self.dist[v] == INF:
            return [v]

        path = []
        cur = v
        while True:
            path.append(cur)
            if cur == self.src:
                break
            cur = self.parent[cur]
            if cur == -1:
                log_error(
                    f"parent inconsistente ao reconstruir caminho até {v} "
                    f"(chegou em -1). Caminho parcial: {path}"
                )
                break

        return path  # v <- ... <- src
