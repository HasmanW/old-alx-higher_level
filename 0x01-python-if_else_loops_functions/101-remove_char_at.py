#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ""
    for val in str:
        if n > len(str) - 1:
            return str
        elif val != str[n]:
            new_str += val
    return new_str
