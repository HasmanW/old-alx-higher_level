#!/usr/bin/python3
import hidden_4 as hidden

if __name__ == "__main__":
    for value in dir(hidden):
        if value[:2] != '__':
            print(value)
