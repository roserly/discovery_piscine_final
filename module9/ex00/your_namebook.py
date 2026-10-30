#!/usr/bin/env python

def array_of_names(persons):
    full_names = []
    for k_first, v_last in persons.items():   
        formatted_name = f"{k_first.capitalize()} {v_last.capitalize()}"
        full_names.append(formatted_name)
    
    return full_names


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

namebook=(array_of_names(persons))
print(namebook)