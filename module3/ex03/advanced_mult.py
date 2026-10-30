#!/usr/bin/env python

table_count = 0
while table_count <= 10:
    print(f"Table of {table_count}: ", end="")
    multiplier = 0
    while multiplier <= 10:
        result = table_count * multiplier
        print(f"{result} ",end="")
        multiplier += 1
    table_count += 1   
    print() 