import sys
from Dijkstra import Dijkstra
from utils import read_input,  write_output


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
    sp = Dijkstra(g, src, use_decrease_key=True)

    if out_path is not None:
        with open(out_path, "w", encoding="utf-8") as f:
            write_output(f, g, sp)
    else:
        write_output(sys.stdout, g, sp)
        print()


if __name__ == "__main__":
    main()
