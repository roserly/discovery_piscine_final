#!/usr/bin/env python
# Assumption number 25 is accepted as a valid input.


input_number = int(input("Enter a number less than or equal to 25 : "))
if input_number > 25:
    print("Error!")

while input_number <= 25:
    print(f"Inside the loop, my variable is {input_number}")
    input_number += 1

