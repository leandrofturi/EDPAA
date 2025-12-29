import sys
import glob
import time
from pathlib import Path
from datetime import datetime
from Dijkstra import Dijkstra
from utils import read_input, write_output


def pprint_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def main():
    argc = len(sys.argv)

    if argc < 3:
        print("python analysis.py <pasta_entrada> <pasta_saida>")
        return

    in_files = glob.glob(f"{sys.argv[1]}/*.txt")
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    errors_file = None
    if argc > 3:
        errors_file = Path(sys.argv[3])

    results_file = out_dir / "resultados.txt"
    rf = open(results_file, "w", encoding="utf-8")

    if errors_file is not None:
        with open(errors_file, "w", encoding="utf-8") as ef:
            ef.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            ef.write("\n")

    rf.write("ARQUIVO\tVÉRTICES\tARESTAS\tTEMPO_LEITURA(s)\tTEMPO_DIJKSTRA(s)\tTEMPO_TOTAL(s)\n")

    for use_decrease_key in [True, False]:
        for ip in in_files:
            try:
                print(f"Processando {ip}, use_decrease_key={use_decrease_key}...")
    
                t0 = time.perf_counter()
                src, g = read_input(ip, errors_file=errors_file)
                t1 = time.perf_counter()
    
                sp = Dijkstra(g, src, use_decrease_key=use_decrease_key, errors_file=errors_file)
                t2 = time.perf_counter()
    
                edge_count = sum(len(lst) for lst in g.adj)
    
                output_graph_path = out_dir / f"{Path(ip).stem}_saida.txt"
                with open(output_graph_path, "w", encoding="utf-8") as f:
                    write_output(f, g, sp)
    
                t_read = t1 - t0
                t_dij = t2 - t1
                t_tot = t2 - t0
    
                rf.write(
                    f"{Path(ip).name}|use_decrease_key={use_decrease_key}\t{g.n}\t{edge_count}\t"
                    f"{t_read:.6f}\t{t_dij:.6f}\t{t_tot:.6f}\n"
                )
            except Exception as e:
                if errors_file is not None:
                    print(str(e))
                continue
    
    rf.close()
    print(f"\nResultados em: {results_file}")


if __name__ == "__main__":
    main()
