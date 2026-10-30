#!/usr/bin/env python
'''
Create a program called greetings_for_all.py that does not take any parameters.
• Ensure this program is executable.
• Create a function called greetings which takes a name as a parameter and displays
a welcome message with that name.
• If the function is called without an argument, its default parameter should be "noble
stranger".
• If the function is called with an argument that is not a string, an error message
should be displayed instead of the welcome message.
~~~~~
test
~~~~~
?> cat greetings_for_all.py | cat -e
# your function definition here
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)

?> ./greetings_for_all.py | cat -e
Hello, Alexandra.$
Hello, Wil.$
Hello, noble stranger.$
Error! It was not a name.$
?>

'''

import sys
import re

def greetings(name):
   
    if isinstance(name, (int,float)):
        print("Error! It was not a name.!")
    elif not name: 
        print(f"Hello noble stranger!")
    else:
        print(f"Hello, {name}" )

# greetings("Alexandra")
# greetings("Wil")
# greetings("")
# greetings(42)

for name in ["Alexandra","Wil","",42]:
    greetings(name)

