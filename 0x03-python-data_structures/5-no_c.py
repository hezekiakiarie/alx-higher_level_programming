#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)
    indexCount = 0
    for i in my_string_list:
        if i == 'c' or i == 'C':
            my_string_list[indexCount] = ""
        indexCount += 1
    return "".join(my_string_list)
