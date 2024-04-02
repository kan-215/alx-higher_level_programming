#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for item in range(x):
            print("{}".format(my_list[item]), end='')
            i += 1
    except IndexError:
        pass
    print()
    return i
