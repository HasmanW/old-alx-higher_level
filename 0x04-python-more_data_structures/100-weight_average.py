#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        weight_list = []
        val_list = []
        for i in range(len(my_list)):
            weight = my_list[i][0] * my_list[i][1]
            val_list.append(my_list[i][1])
            weight_list.append(weight)
    average_weight = sum(weight_list) / sum(val_list)
    return average_weight
