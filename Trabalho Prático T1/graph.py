class Graph:
    """TAD opaco: grafo direcionado com lista de adjacências."""

    def __init__(self, names):
        self.n = len(names)
        self.names = names[:]  # index -> "node_i"
        self.adj = [[] for _ in range(self.n)]  # adj[u] = [(v, w), ...]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

    def print_graph(self):
        """
        Imprime o grafo como lista de adjacência.
        """
        for u in range(self.n):
            edges = []
            for v, w in self.adj[u]:
                edges.append(f"{self.names[v]}({w})")

            if edges:
                line = ", ".join(edges)
            else:
                line = "[empty]"

            print(f"{self.names[u]} -> {line}")
