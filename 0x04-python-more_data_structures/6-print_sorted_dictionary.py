#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    convertToList = list(a_dictionary.keys())
    convertToList.sort()
    sorttedDict = {keys: a_dictionary[keys] for keys in convertToList}
    for key, value in sorttedDict.items():
        print("{}: {}".format(key, value))
