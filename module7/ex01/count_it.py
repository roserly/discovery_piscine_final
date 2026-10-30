#!/usr/bin/env python

'''
• Create a program called count_it.py.
• Ensure this program is executable.
• The program should:
◦ Display "parameters:" followed by the total number of parameters passed as
arguments.
◦ For each parameter, display the parameter itself and its length, ending with a
newline.
◦ If no parameters are provided, display "none" followed by a newline.

Test commands:
?> ./count_it.py | cat -e
none$
?> 
parameters: 3$
Game: 4$
of: 2$
Throne 7$

'''

import sys

if len(sys.argv) < 2:
    print ("None\n")  

else:
    print(f"Parameters: {len(sys.argv[1:])}")
    for word in sys.argv[1:]:
        print(word + ":" + " " + str(len(word)))
