#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_list = []
    for i, j in a_dictionary.items():
        if j == value:
            delete_list.append(i)
    for i in delete_list:
        del a_dictionary[i]
    return a_dictionary
