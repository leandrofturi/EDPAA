import os
import sys
from typing import List
from BTree import BTree
from diskManager import DiskManager


def run_case(input_path: str, output_path: str) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip() != ""]

    d = int(lines[0])
    n = int(lines[1])
    ops = lines[2: 2 + n]

    disk = DiskManager("btree_nodes.bin", d=d)
    bt = BTree(d=d, disk=disk)

    out_lines: List[str] = []
    dump_dir = os.path.join(os.getcwd(), "btree_dumps")
    os.makedirs(dump_dir, exist_ok=True)
    step = 0
    try:
        for op in ops:
            kind = op[0]
            rest = op[1:].strip()
            if kind == "I":
                k, v = rest.split(",", 1)
                k, v = int(k.strip()), int(v.strip())
                bt.insert(k, v)
            elif kind == "R":
                bt.remove(int(rest))
            elif kind == "B":
                k = int(rest)
                out_lines.append(
                    "O REGISTRO ESTA NA ARVORE!" if bt.search(k)
                    else "O REGISTRO NAO ESTA NA ARVORE!"
                )
            else:
                out_lines.append(f"OPERACAO INVALIDA: {op}")

            step += 1
            dump_path = os.path.join(dump_dir, f"passo_{step:03d}.txt")
            disk.dump_txt(dump_path)

        out_lines.append("-- ARVORE B")
        out_lines.extend(bt.to_level_order_lines())

        if output_path == "-":
            for ln in out_lines:
                sys.stdout.write(ln + "\n")
        else:
            with open(output_path, "w", encoding="utf-8") as out:
                for ln in out_lines:
                    out.write(ln + "\n")
    finally:
        disk.close_and_delete()


def main():
    if len(sys.argv) != 3:
        return 2
    run_case(sys.argv[1], sys.argv[2])
    return 0


if __name__ == "__main__":
    main()
