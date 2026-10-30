#!/usr/bin/env python

import sys


if len(sys.argv) < 3 or len(sys.argv) > 3 :
    print("None")

elif int(sys.argv[1]) <= int(sys.argv[2]):
    num_list = []
    # Convert string arguments to integers for the range function
    for i in range(int(sys.argv[1]), int(sys.argv[2])):
        num_list.append(i)
    print(num_list)
else:

    print("None")

#10 14