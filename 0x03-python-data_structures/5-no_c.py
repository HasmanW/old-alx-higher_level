#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i == ord('C') or i == ord('c'):
            pass
        else:
            new_string += i
    return new_string
