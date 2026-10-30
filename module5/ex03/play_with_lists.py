#!/usr/bin/env python

#EX00 - Create List, original list
original_list= [2,8,9,48,8,22,-12,2]
print(f"Original List: {original_list}")

#EX01 - Adding + 2 to original list
modified_list = [number + 2 for number in original_list]
#print(f"Original list: {original_list}")
print(f"Modified list add 2: {modified_list}")

#EX02 - Process value greater than 5
modified_list_more_than_5 = [num +2 for num in original_list if num > 5]
# print(f"Modified list add two: {modified_list}")
print(f"Modified_list_more_than_5 : {modified_list_more_than_5}")

''' MAIN FOCUS '''

#EX03 - Remove duplicates
#print(list({num for num in modified_list_more_than_5 if num > 5}))
print({num +2 for num in original_list if num > 5})
print(set(modified_list_more_than_5))

# if want to evaluate after adding 2 to the list
# print({num +2 for num in original_list if (num +2) > 10})
# print(list({num +2 for num in original_list if (num +2) >10 }))

# filtered_set = set()
# for num in modified_list_more_than_5:
#     if num > 5:
#         filtered_set.add(num)

# final_list = list(filtered_set)
# print(final_list)

#print(type(list({num for num in num_list if num > 5}))) 