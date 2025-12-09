import os
import sys
import time
import signal

from sorts import sortV1, sortV2, sortV3, sortV4, sortV5, sortV6, sortV8
from sorts_aula17 import sortV1 as sortV1_aula17, sortV2 as sortV2_aula17, sortV3 as sortV3_aula17, sortV4 as sortV4_aula17, sortV5 as sortV5_aula17, sortV6 as sortV6_aula17, sortV7 as sortV7_aula17

timeout = 180


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException()



def sortting(input_data, sort_func, CUTOFF=0, shuffle=False, method="quick-sort"):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        # start the timer
        start = time.time()

        # sortting arrays
        sorted_data = sort_func(input_data, 0, len(input_data)-1, CUTOFF, shuffle)

        # stop the timer
        end = time.time()

        name = sort_func.__name__
        print(f"{method} '{name}'-CUTOFF={CUTOFF}-shuffle={shuffle} in {end - start:.4f}s")

        # printing sorted arrays
        # with open(sys.argv[1] + f"_sorted_{name}", 'w') as file:
        #     for x in sorted_data:
        #         file.write(str(x) + " ")

        if len(input_data) < 10:
            for x in sorted_data:
                print(str(x) + " ")
    except TimeoutException:
        signal.alarm(0)  # cancelar timeout depois do erro
        print(f"{method} '{sort_func.__name__}'-CUTOFF={CUTOFF}-shuffle={shuffle} TIMEOUT ({timeout}s)")
    except RecursionError:
        print(f"{method} '{sort_func.__name__}'-CUTOFF={CUTOFF}-shuffle={shuffle} RecursionError")


def run(path):
    # reading the input data

    # example of time counting for reading the input data

    # start the timer
    start = time.time()
    input_data = []
    with open(path, 'r') as file:
        # Read each line in the file
        for line in file:
            x = int(line)
            input_data.append(x)

    print(f"size={len(input_data)}")

    # stop the timer
    end = time.time()
    # calculate elapsed time
    print(f"read in {end - start:.4f}s")

    CUTOFF_range = range(10, 40, 5)

    sortting(input_data, sortV1, shuffle=True)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV2, CUTOFF, shuffle=True)
    sortting(input_data, sortV3, shuffle=True)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV4, CUTOFF, shuffle=True)
    sortting(input_data, sortV5, shuffle=True)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV6, CUTOFF, shuffle=True)
    sortting(input_data, sortV8, shuffle=True)

    sortting(input_data, sortV1)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV2, CUTOFF)
    sortting(input_data, sortV3)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV4, CUTOFF)
    sortting(input_data, sortV5)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV6, CUTOFF)
    sortting(input_data, sortV8)

    CUTOFF_range = range(10, 40, 5)
    sortting(input_data, sortV1_aula17, method="merge-sort")
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV2_aula17, CUTOFF, method="merge-sort")
    sortting(input_data, sortV3_aula17, method="merge-sort")
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV4_aula17, CUTOFF, method="merge-sort")
    sortting(input_data, sortV5_aula17, method="merge-sort")
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV6_aula17, CUTOFF, method="merge-sort")
    sortting(input_data, sortV7_aula17, CUTOFF, method="merge-sort")


def main():
    paths = [os.path.join(dp, f) for dp, dn, filenames in
             os.walk(sys.argv[1]) for f in filenames
             if os.path.splitext(f)[1] == '.txt']
    for path in paths:
        if '10M' in path:
            print(path)
            run(path)

    for path in paths:
        if 'few_uniq/10M_const_keys_unif_rand' in path:
            print(path)
            run(path)


main()
