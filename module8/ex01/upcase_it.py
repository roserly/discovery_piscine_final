#!/usr/bin/env python
'''
• Create a program called upcase_it.py (again!)
• Ensure this program is executable.
• Define a function in the program named upcase_it.
• The upcase_it function should take a string as an argument and return the string
in uppercase.
• Test the function by calling it in your program. In the example below, we test it
with "hello":
Test:    
?> cat upcase_it.py
# Your function definition
print(upcase_it("hello"))
?> ./upcase_it.py
HELLO
?>'''

def hello(x):
    return x.upper()

print(hello("hello"))
