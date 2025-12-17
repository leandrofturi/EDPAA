import sys
from graph import Graph
from Dijkstra import Dijkstra


def read_input(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]

    src_name = lines[0]

    matrix_lines = lines[1:]
    n = len(matrix_lines)

    names = []
    rows = []

    for ln in matrix_lines:
        parts = [p.strip() for p in ln.split(",")]
        names.append(parts[0])
        rows.append(parts[1:])  # tem n-1 pesos

    name_to_idx = {name: i for i, name in enumerate(names)}
    src = name_to_idx[src_name]

    g = Graph(names)

    for u in range(n):
        k = 0  # índice em rows[u]
        for v in range(n):
            if v == u:
                continue  # diagonal não existe no arquivo
            w = float(rows[u][k])
            k += 1
            if w > 0.0:
                g.add_edge(u, v, w)

    return src, g


def write_output(stream, g: Graph, sp: Dijkstra):
    n = g.n
    order = sorted(range(n), key=lambda v: sp.dist[v])
    for v in order:
        path_vertices = sp.path_to(v)  # [v, ..., src]
        chain = " <- ".join(g.names[x] for x in path_vertices)
        stream.write(
            f"SHORTEST PATH TO {g.names[v]}: "
            f"{chain} (Distance: {sp.dist[v]:.2f})\n"
        )
    stream.flush()


def main():
    argc = len(sys.argv)

    if argc < 2:
        print("python trab1.py <nome_arquivo_entrada> <nome_arquivo_saida>")
        return

    in_path = sys.argv[1]
    out_path = sys.argv[2] if argc >= 3 else None

    src, g = read_input(in_path)
    if out_path is None:
        print("\n=== GRAPH ===")
        g.print_graph()
        print("=============\n")
    sp = Dijkstra(g, src)

    if out_path is not None:
        with open(out_path, "w", encoding="utf-8") as f:
            write_output(f, g, sp)
    else:
        write_output(sys.stdout, g, sp)


if __name__ == "__main__":
    main()
