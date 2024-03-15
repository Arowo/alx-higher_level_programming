#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i, 10):
        if i == j:
            continue
        print("{}".format(i), end="")
        print("{}".format(j), end=", ")
print("{}{}".format(8, 9))
