#!/usr/bin/python3

def safe_print_list_integers(my_list, x=0):
    """ print integers """
    count = 0
    try:
        for element in my_list[:x]:
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                count += 1
        print()
    except IndexError:
        raise 'IndexError: list index out of range'
    return count
