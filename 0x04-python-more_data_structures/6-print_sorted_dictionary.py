#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for l in sorted(my_dict.keys()):
        print("{}: {}".format(l, my_dict[l]))
