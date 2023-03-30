#!/usr/bin/python3

def safe_print_list_integers(my_list, x=0):
    """ print integers """
    count = 0
    for elements in my_list[:x]:
        try:
            print("{:d}".format(elements), end="")
            count += 1
        except Exception:
            pass
    print()
    return count
