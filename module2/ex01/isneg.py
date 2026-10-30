#!/usr/bin/env python

input_number = int(input("Please enter a number: "))
if input_number == 0:
    print("The number is both positive and negative.")   
elif input_number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")    