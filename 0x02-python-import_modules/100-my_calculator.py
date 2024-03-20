#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    ar = sys.argv
    if len(ar) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(True)
    elif ar[2] != "+" and ar[2] != "-" and ar[2] != "*" and ar[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(True)
    else:
        a = int(ar[1])
        b = int(ar[3])
        if ar[2] == "+":
            add_num = add(a, b)
            print("{} + {} = {}".format(a, b, add_num))
        elif ar[2] == "-":
            sub_num = sub(a, b)
            print("{} - {} = {}".format(a, b, sub_num))
        elif ar[2] == "*":
            mul_num = mul(a, b)
            print("{} * {} = {}".format(a, b, mul_num))
        elif ar[2] == "/":
            div_num = div(a, b)
            print("{} / {} = {}".format(a, b, div_num))
        sys.exit(False)
