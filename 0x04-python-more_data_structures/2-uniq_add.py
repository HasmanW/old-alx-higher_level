#!/usr/bin/python3

def uniq_add(my_list):
    copy_list = []
    result = 0

    for i in my_list:
        if i not in copy_list:
            copy_list.append(i)
    for x in copy_list:
        result += x
    return result
