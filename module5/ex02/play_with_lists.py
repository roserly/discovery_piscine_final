#!/usr/bin/env python
original_list= [2,8,9,48,22,-12,2]
modified_list = [number + 2 for number in original_list]   
# print(f"Original list: {original_list}")
# print(f"Modified list: {modified_list}")
modified_list_more_than_5 = [num +2 for num in original_list if num > 5]   
print(f"Modified_list: {modified_list}")
print(f"modified_list_more_than_5 : {modified_list_more_than_5}")

'''
# numbers = [2, 8, 9, 48, 22, -12, 2]
# modified_numbers = []

# for num in numbers:
#     if num > 5:
#         # process
#         modified_numbers_v2.append(num+2)
#     else:
#         # don't process
# for number in numbers:  

#     if number > 5:
        
#         # 4. If true, append (add) the number to our new list
#         modified_numbers.append(number)

# print(modified_numbers)
'''