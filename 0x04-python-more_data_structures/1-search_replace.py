#!/usr/bin/python3

def search_replace(my_list, search, replace):
    r_list = my_list.copy()
    for i in range(len(r_list)):
        if r_list[i] == search:
            r_list[i] = replace
    return r_list
