#!/usr/bin/env python

'''
EX03
• Create a program called aff_rev_params.py.
• Ensure this program is executable.
• When executed, the program should display all the strings passed as parameters,
followed by a newline, in reverse order.
• If there are fewer than two parameters, it should display "none" followed by a
newline
'''

import sys

arguments_list = (sys.argv)


if len(sys.argv) < 3:
    print ("None")
else:
    #Method 1
    # comments sequence[start:stop:step]
    arguments_orig = (arguments_list[1:])
    arguments_reverse = (arguments_list[-1:0:-1])

    #Method 1
    print("Original: ")
    for i in (arguments_list[1:]):
        print(f"{i} ")
    print()

    print("Reverse: ")
    for i in (arguments_list[-1:0:-1]):
        print(f"{i} ")
    print()
        

    # Method 2
    '''This takes all the remaining items from that sliced list and glues them together into one long string. 
    The " " specifies that a single space should be placed between each item. This is to display single lines'''
    # arguments_orig = " ".join(arguments_list[1:])
    # arguments_reverse = " ".join(arguments_list[-1:0:-1])
    # print(f"Orignal: {arguments_orig}")
    # print(f"Reverse: {arguments_reverse}")