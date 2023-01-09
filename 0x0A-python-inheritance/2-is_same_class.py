#!/usr/bin/python3
"""object_is_same_class
"""


def is_same_class(obj, a_class):
    """Returns True if object is same as instance, else False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
