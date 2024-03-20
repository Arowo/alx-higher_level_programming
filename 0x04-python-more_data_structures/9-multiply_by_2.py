#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    value_list = list(map(lambda x: x * 2, a_dictionary.values()))
    key_list = a_dictionary.keys()
    return dict(zip(key_list, value_list))
