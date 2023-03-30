#!/usr/bin/python3

def safe_print_list_integers(my_list, x=0):
    """ print integers """
    count = 0
    for element in my_list[:x]:
        if isinstance(element, int):
            try:
                print("{:d}".format(element), end="")
                count += 1
            except IndexError:
                raise
        else:
            pass
    print()
    return count
