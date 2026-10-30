#!/usr/bin/env python
'''
• Create a program called downcase_all.py.
• Ensure this program is executable.
• Define a function in this program called downcase_it.
• The downcase_it function should take a string as an argument and return the
string in lowercase.
• Apply this function to each program’s parameters and display the return value for
each.
• If there are no parameters, display "none" followed by a line break.
'''

import sys

# def downcase_it(x):
#     if len(sys.argv) < 2:
#         print("None")

#     for i in x:
#         print(i.lower())

# downcase_it(sys.argv[1:])


def downcase_it(argument):
    return argument.lower()

for argument in sys.argv[1:]:
    lowercase = downcase_it(argument)
    print(lowercase)