#!/usr/bin/python3
'''Module for MyList class.'''


class MyList(list):
    '''Customized MyList class.'''
    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))
