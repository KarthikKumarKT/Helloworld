# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:06:37 2020

@author: kt998
"""

largest = 0
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    try:
        num = int(inp)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num


print("Maximum is", largest)
print("Minimum is",smallest)