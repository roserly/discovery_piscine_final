#!/usr/bin/env python
'''
◦ Take a string as a parameter.
◦ Prompt the user to enter a word that matches the parameter passed as an
argument, as shown in the example below.
◦ Display "Good job!" followed by a newline if the word entered by the user
matches the parameter passed.
◦ Display "Nope, sorry..." followed by a newline if the word entered by the user
does not match the parameter passed.
◦ Display "none" followed by a newline if the number of parameters passed is
different from 1.

Test:
?> ./parameter_matching.py
none
?> ./parameter_matching.py "Hello"
What was the parameter? Bonjour
Nope, sorry...
?> ./parameter_matching.py "Hello"
What was the parameter? Hello
Good 

'''

import sys

if len(sys.argv) !=2:
#if len(sys.argv) !=1:
    print ("None")

else:
    #print(type(sys.argv[1]))
    my_arguments = str(sys.argv[1])
    #print(type(my_arguments))
    user_input = str(input("What was the parameter?: "))

    if my_arguments == user_input:
        print("Good Job!")
    else:
        print("Nope Sorry.")