#!/usr/bin/env python
'''
EX02
• Create a program called downcase_it.py.
• Ensure this program is executable.
• The program takes a string as a parameter.
• It should display the string in lowercase, followed by a newline.
• If the number of parameters is different from 1, it should display "none" followed
by a newline.
'''

import sys

arguments_list = (sys.argv)

if len(sys.argv) !=2:
    print ("None")
    #Checks Length
    # print(f"First: {len(sys.argv)}")

else:
    print(f"{arguments_list[1].lower()}")
    #Checks Length
    #print(f"Second: {len(sys.argv)}")
    