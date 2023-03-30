#!/usr/bin/python3

def safe_print_list(my_list, x=0):
    """ prints elements in a list """
    count = 0
    try:
        for element in my_list[:x]:
            print("{}".format(element), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
