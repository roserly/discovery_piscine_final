#!/usr/bin/env python

import sys

'''
• Create a program called functions_everywhere.py that takes parameters.
• Ensure this program is executable.
• You need to create two different functions in this program:
◦ The shrink function: should take a string as a parameter and display the first
eight characters of that string.
◦ The enlarge function: should take a string as a parameter and append ’Z’
characters until the string has a total of eight characters. Then, it displays
the resulting string.
• If there are no parameters, display "none" followed by a line break.
• For each argument passed to the program:
◦ If the argument has more than eight characters, call the shrink function on
it.
◦ If the argument has fewer than eight characters, call the enlarge function on
it.
◦ If the argument has exactly eight characters, display it directly followed by a
new line.
?> ./functions_everywhere.py | cat -e
none$
?> ./functions_everywhere.py 'lol' 'physically' 'backpack' | cat -e
lolZZZZZ$
physical$
backpack$
?>
'''

def shrink(word):
    count=0
    count= 8 - len(word)
    print(word + count*"Z")
    # print (count)
    # print("shrink:" + word)
    # print(type(word))


# Assumption: When word characters = 8 will go to function enlarge
def enlarge(word):
    #print("enlarge:" + word)
    print(word[:8])

if len(sys.argv) < 2:
    print ("None")

else:
    for word in sys.argv[1:]:
        if(len(word)<8):
            shrink(word)
        else:
            enlarge(word)

#'lol' 'physically' 'backpack'