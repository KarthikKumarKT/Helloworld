# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:35:45 2020

@author: kt998
"""
gd = input("Enter Score:")
gd = float(gd)
if gd >=0 and gd <=1:
    if gd >= 0.9:
        print("A")
    elif gd >= 0.8:
        print("B")
    elif gd >= 0.7:
        print("C")
    elif gd >= 0.6:
        print("D")
    else :
        print("F")
else :
    print("Not in Range")
    quit()
