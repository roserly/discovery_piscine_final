#!/usr/bin/env python
''' 
EX01
• Create a program called upcase_it.py that takes a string as a parameter.
• Ensure this program is executable.
• The program should display the string in uppercase, followed by a newline.
• If the number of parameters is different from 1, display "none" followed by a newline.'''

import sys

arguments_list = (sys.argv)

if len(sys.argv) !=2:
    print ("None")
    #Checks Length
    # print(f"First: {len(sys.argv)}")
else:
    print(f"{arguments_list[1].upper()}")
    #Checks Length
    #print(f"Second: {len(sys.argv)}")
    
