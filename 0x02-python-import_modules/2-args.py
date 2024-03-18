#!/usr/bin/python3

import sys
def arguments_out(argv):
    n = len(argv) -1
    if n == 0:
        print('{} arguments.'.format(n))
    elif n == 1:
        print(' arguments:'.format(n))
        print('1: {}'.format(arg[1]))
    else:
        print('{} arguments:'.format(n))
        i = 1
        for arg in argv[1:]:
            print('{}: {}'.format(i, arg))
            i += 1

if __name__ == '__main__':
    arguments_out(sys.argv)
