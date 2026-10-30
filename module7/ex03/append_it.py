#!/usr/bin/env python

import sys
import re


if len(sys.argv) < 2:
    print("None")

else:
   
    count=0
    words = sys.argv[1:]
    for word in words:
        #print(word)
        if not word.endswith("ism"):
            word = word + "ism"
            print(word)


# "parallel" "egoism" "human"