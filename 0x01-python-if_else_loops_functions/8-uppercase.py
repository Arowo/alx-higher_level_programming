#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        convert_chr = str[i]
        if (ord(str[i]) >= 97) and (ord(str[i]) <= 122):
            convert_chr = chr(ord(str[i]) - 32)
        print("{}".format(convert_chr), end="")
    print()
