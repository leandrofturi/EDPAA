import os
import sys
import time


from sorts import sortV1, sortV2, sortV3, sortV4, sortV5, sortV6, sortV7


def sortting(input_data, sort_func, CUTOFF=0):
    # start the timer 
    start = time.time()

    # sortting arrays
    sorted_data = sort_func(input_data, 0, len(input_data)-1, CUTOFF)

    # stop the timer
    end = time.time()

    name = sort_func.__name__
    print(f"sort '{name}'-CUTOFF={CUTOFF} in {end - start:.4f}s")

    # printing sorted arrays
    # with open(sys.argv[1] + f"_sorted_{name}", 'w') as file:
    #     for x in sorted_data:
    #         file.write(str(x) + " ")

    if len(input_data) < 10:
        for x in sorted_data:
            print(str(x) + " ")


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
    sortting(input_data, sortV1)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV2, CUTOFF)
    sortting(input_data, sortV3)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV4, CUTOFF)
    sortting(input_data, sortV5)
    for CUTOFF in CUTOFF_range:
        sortting(input_data, sortV6, CUTOFF)
    sortting(input_data, sortV7)


def main():
    paths = [os.path.join(dp, f) for dp, dn, filenames in
             os.walk(sys.argv[1]) for f in filenames
             if os.path.splitext(f)[1] == '.txt']
    for path in paths:
        print(path)
        run(path)


main()
