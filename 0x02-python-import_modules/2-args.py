#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_item = sys.argv
    length = len(args_item) - 1
    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, args_item[1]))
    else:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, args_item[i]))
