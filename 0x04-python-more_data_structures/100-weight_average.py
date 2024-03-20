#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return 0
    sum_tuple = 0
    mult = 0
    for tup in my_list:
        mult += tup[0] * tup[1]
        sum_tuple += tup[1]
    return mult / sum_tuple
