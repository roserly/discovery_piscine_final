#!/usr/bin/env python

import sys

'''
EX00
• Create a program called aff_first_param.py.
• Ensure this program is executable.
• The program should display the first string parameter passed, followed by a newline.
• If there are no parameters, display "none" followed by a newline
'''

if len(sys.argv) < 2:
    print ("None")
    #Checks Length
    #print(f"First: {len(sys.argv)}")
else:
    print(sys.argv[1])
    #Checks Length
    #print(f"Second: {len(sys.argv)}")