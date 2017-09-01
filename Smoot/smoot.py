#!/usr/bin/env python3
# Ruslan Shakirov
# Problem 1: Smoots Problem

"""Smoot's Hieght = 5 feet and 7 inch
    Formula=(InputInteger*321.5)/1795
"""
def smootconverter():
    """This function takes input from smoot-test.in and converts 
         sample numbers in feet to smoot."""
    output=0
    feet=1795
    smoot=321.5
    file=open("smoot_test.in").readlines()
    numbers = [int(x) for x in file]
    for i in numbers:
        output=(i*smoot)/feet
        output=round(output,1)
        print("Input:",i, "feet")
        print("Output:", output, "smoot\n")
    return None
smootconverter()

