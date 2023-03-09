#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        if ord(str[i]) in range(65, 91):
            new_str += str[i]
        else:
            new_str += chr(ord(str[i]) - 32)
    print("{}".format(new_str))
