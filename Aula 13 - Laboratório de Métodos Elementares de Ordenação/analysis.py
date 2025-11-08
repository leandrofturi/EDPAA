import os
import sys
import time


from sorts import insertion_sort, selection_sort, bubble_sort, shaker_sort


def sortting(input_data, sort_func):
    # start the timer 
    start = time.time()

    # sortting arrays
    sorted_data = sort_func(input_data)

    # stop the timer
    end = time.time()

    name = sort_func.__name__
    print(f"sort '{name}' in {end - start:.4f}s")

    # printing sorted arrays
    with open(sys.argv[1] + f"_sorted_{name}", 'w') as file:
        for x in sorted_data:
            file.write(str(x) + " ")

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

    sortting(input_data, insertion_sort)
    sortting(input_data, selection_sort)
    sortting(input_data, bubble_sort)
    sortting(input_data, shaker_sort)


def main():
    paths = [os.path.join(dp, f) for dp, dn, filenames in
             os.walk(sys.argv[1]) for f in filenames
             if os.path.splitext(f)[1] == '.txt']
    for path in paths:
        print(path)
        run(path)


main()
