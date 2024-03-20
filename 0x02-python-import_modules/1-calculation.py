#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    a = 10
    b = 5
    add_num, sub_num = add(a, b), sub(a, b)
    div_num, mul_num = div(a, b), mul(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add_num))
    print("{:d} - {:d} = {:d}".format(a, b, sub_num))
    print("{:d} * {:d} = {:d}".format(a, b, mul_num))
    print("{:d} / {:d} = {:d}".format(a, b, div_num))
