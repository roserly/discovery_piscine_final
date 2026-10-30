#!/usr/bin/env python

user_input = int(input("Please tell me your age: "))
print(f"You are currently {user_input} years old.")
for age in (10,20,30):
    print(f"In {age} years, you will be {int(user_input) + age} years old.")