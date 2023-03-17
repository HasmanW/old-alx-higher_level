#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    if arguments == 0:
        print(f"{arguments} arguments.")
    elif arguments == 1:
        print(f"{arguments} argument:")
    else:
        print(f"{arguments} arguments:")

    arg_list = [f'{sys.argv[0]}']
    for arg in sys.argv[1:]:
        arg_list.append(arg)
    for i in range(1, len(arg_list)):
        print(f"{i}: {arg_list[i]}")
