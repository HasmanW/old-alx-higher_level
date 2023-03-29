#!/usr/bin/python3
n = 8
for i in range(1, n):
    for j in range(n, 0, -1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print("")
