#!/usr/bin/env python

user_input_number = input("Give me a number: ").strip()
#print(type(user_input_number))
num = float(user_input_number)
#print(type(num))
if num.is_integer() and user_input_number.endswith('.0'):
    print(f"{num} is an integer")
    #print(type(num))
elif num.is_integer():
    print(f"{num:g} is an integer")
    #print(type(num))
else:
    print(f"{num} is a decimal")
    #print(type(num))
