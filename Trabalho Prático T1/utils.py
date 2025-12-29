from pathlib import Path
from graph import Graph
from Dijkstra import Dijkstra


def log_error(errors_file, msg: str):
    if errors_file is not None:
        with open(errors_file, "a", encoding="utf-8") as ef:
            ef.write(msg + "\n")


def read_input(path, errors_file=None):
    def name_to_idx(name: str) -> int:
        return int(name.split("_")[-1])

    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]

    src_name = lines[0]

    raw_rows = []
    for ln in lines[1:]:
        parts = [p.strip() for p in ln.split(",")]
        name = parts[0]
        weights = parts[1:]
        raw_rows.append((name, weights))

    n = len(raw_rows)

    names = [None] * n
    rows = [None] * n

    for name, weights in raw_rows:
        i = name_to_idx(name)
        names[i] = name
        rows[i] = weights

    src = name_to_idx(src_name)

    g = Graph(names)
    for u in range(n):
        k = 0
        for v in range(n):
            if v == u:
                continue

            try:
                w = float(rows[u][k])
            except ValueError:
                log_error(errors_file, f"[ValueError] ({u},{v}){rows[u][k]}")
                w = -1.0
            except Exception as e:
                log_error(errors_file, f"[Exception] ({u},{k}){rows[u][k]} {str(e)}")
                w = -1.0

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
