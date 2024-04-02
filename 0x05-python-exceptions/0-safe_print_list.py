#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sum = 0
    try:
        for i in range(x):
            sum += 1
            print(my_list[i], end='')
        print()
    except IndexError:
        sum -= 1
        print()
        pass
    return sum
