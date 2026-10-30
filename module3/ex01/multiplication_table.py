#!/usr/bin/env python

input_num = int(input("Enter a number: "))
print(f"Multiplication table for {input_num}:")
table_num = 0    
while table_num < 10:
    result = input_num * table_num
    print(f"{table_num} x {input_num} = {result}")
    table_num    += 1