#!/usr/bin/env python

def find_the_redheads(dupont_family):

    def is_redhead(name):
        return dupont_family[name] == "red" 
    
    redheads_filter = filter(is_redhead, dupont_family)

    return list(redheads_filter)

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))