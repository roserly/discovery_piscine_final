#!/usr/bin/env python

input_first_number = int(input("Please enter first number: "))
input_second_number = int(input("Please enter second number: "))

result = input_first_number * input_second_number

print(f"{input_first_number} x {input_second_number} = {result}")
if result == 0:
    print("The number is both positive and negative.") 
elif result > 0:
    print("The number is positive.")
else:
    print("The number is negative.")  