#!/usr/bin/env python

import sys
import re
'''
• Create a program called string_are_arrays.py that takes a string as a parameter.
• This program should be executable.
• When executed, the program should display "z" for each occurrence of the character
"z" in the string passed as a parameter, followed by a newline.
• If the number of parameters is different from 1, or if there are no "z" characters in
the string, it should display "none" followed by a newline.

Test
?> ./string_are_arrays.py | cat -e
none$
?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
none$
?> ./string_are_arrays.py "The character z is found in this string" | cat -e
z$
?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
zzz$

'''


if len(sys.argv) < 2:
    print("None")

else:
    count = 0
    #print(len(sys.argv[1:]))
    words = sys.argv[1:]
    for word in words:
        if "z" in word:
            count += len(word)
        else:
            print("None")

    print(count * "z")


# ?> ./string_are_arrays.py | cat -e
# none$
# ?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
# none$
# ?> ./string_are_arrays.py "The character z is found in this string" | cat -e
# z$
# ?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
# zzz$

