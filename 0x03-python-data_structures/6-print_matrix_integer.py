#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # we get the number of rows
    for i in range(len(matrix)):
        # we get the number of columns
        for x in range(len(matrix[i])):
            # prints the values in the row in straight line
            print("{:d}".format(matrix[i][x]), end="")
            # prints the space after the value in row is printed
            if x != len(matrix[i]) - 1:
                print(" ", end="")
        # separates the rows by ending in a new line
        print("")
