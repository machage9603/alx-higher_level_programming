#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    numargs = len(argv) -1
    if numargs == 0:
        print('{} arguments.'.format(numargs))
    elif numargs == 1:
        print('{} argument:'.format(numargs))
        print('1: {}'.format(argv[1]))
    else:
        print('{} arguments:'.format(numargs))
        i = 1
        for arg in argv[1:]:
            print('{}: {}'.format(i, arg))
            i += 1
