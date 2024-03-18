#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        return my_list.pop(idx)
        my_list.insert(idx, new_element)
        return my_list
