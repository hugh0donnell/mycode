#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for farm in farms:
    print("\nOld MacDonald had a farm: " + farm.get("name"), end="")   # newline, print current vendor, and end without newline
    print("\nAnd on that farm he had a:")
    
    for animal in farm.get("agriculture"):   # if x does not appear within the list approved_vendors
        print(animal)
    
    print("\nE-I-E-I-O") # print when loop has finished

