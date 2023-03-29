#!/usr/bin/python3
number = int(input())
factorial = 1
for i in range(1, number+1):
    factorial *= i

print("Factorial of {} is {}".format(number, factorial))
