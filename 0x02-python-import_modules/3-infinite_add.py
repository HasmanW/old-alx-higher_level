#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arg_list = []
    total = 0
    for arg in sys.argv[1:]:
        arg_list.append(int(arg))
    for val in arg_list:
        total += val
    print(total)
