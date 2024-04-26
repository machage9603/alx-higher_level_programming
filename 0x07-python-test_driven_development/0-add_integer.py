#!/usr/bin/python3

"""
the module is add_integer
it adds two intergers together
"""


def add_integer(a, b=98):
    """
    returns addition of a and b
    Args:
        a(int, float) first integer
        b(int, float) second integer
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an interger")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
