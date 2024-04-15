#!/usr/bin/python3
'''Module for python lookup method.'''


def lookup(obj):
    '''Looks up object attributes and methods.
    Args:
        obj: the object to list.

    Returns:
        list: the list of attributes.
    '''
    return dir(obj)
