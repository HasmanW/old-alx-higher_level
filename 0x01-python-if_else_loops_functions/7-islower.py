#!/usr/bin/python3
def islower(c):
    lower_list = []
    for i in range(97, 123):
        lower_list.append(chr(i))
    if c not in lower_list:
        return False
    else:
        return True
