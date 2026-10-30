#!/usr/bin/env python

password = "Python is awesome"

input_password = str(input("Please enter the password: "))
if input_password == password:
    print("Access granted") 
else:
    print("Access denied")