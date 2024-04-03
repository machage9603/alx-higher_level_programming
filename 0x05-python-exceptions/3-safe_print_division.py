#!/usr/bin/python3

def safe_print_division(a,b):
    try:
        div = a / b
    except ZeroDivisionError:
        return None
    finally:
        if 'div'not in locals():
            div = None
        print("Inside result: {}".format(div))
        return div
