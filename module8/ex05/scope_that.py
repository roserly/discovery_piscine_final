#!/usr/bin/env python
'''
• Create a program called scope_that.py that does not take any parameters.
• Ensure this program is executable.
• Inside the program, create a function called add_one that takes a parameter and
adds 1 to the parameter.
• Initialize a variable in the body of the program, display it, and then call the function
that adds 1.
• Display your variable again in the body of the program.
• What do you observe?
'''


def add_one(num):
    num+=1
    print(f"Print Number within function: {num}")
    return num    

number = 42
print(f"Initial Global variable: {number}")
add_one(number)
print(f"Print Number in the Global without return: {number}")
num =add_one(number)
print(f"Print Number in the Global with return statment: {num}")

"""
Variable update in the function will not be pass to the Global. Need the return command
"""
