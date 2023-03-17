#!/usr/bin/python3
import hidden_4.pyc as hidden

if __name__ == "__main__":
    for value in dir(hidden):
        if value[0] == '_':
            print(value)
