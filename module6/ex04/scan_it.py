#!/usr/bin/env python
''' 
ex04
• Create a program called scan_it.py.
• Ensure this program is executable.
• This program should take two parameters.
• The first parameter is a keyword to search for in a string.
• The second parameter is the string to be searched.
• When executed, the program should display the number of times the keyword appears in the string.
• If the number of parameters is different from 2 or if the first strin'''
import sys
import re   

if len(sys.argv) < 3:
    print ("None")
    #print(f"First: {len(sys.argv)}")
else:
    #count = 0
    count=(len(re.findall(sys.argv[1], sys.argv[2])))
    if count == 0:
        print("None")

    else:
        print(count)
        #print(f"Second: {len(sys.argv)}")


''' Test
?> ./scan_it.py | cat -e
none$
?> ./scan_it.py "the" | cat -e
none$
?> ./scan_it.py "the" "hello world" | cat -e
none$
?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
2$
?>'''