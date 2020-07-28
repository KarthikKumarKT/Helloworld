# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:04:34 2020

@author: kt998
"""
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = float(hrs)
rate = float(rate)
if hrs > 40 :
    reg = hrs*rate
    otp = (hrs - 40.0)*(rate*0.5)
    xp = reg + otp
else :
    xp = hrs *rate 
print ("Pay:",xp)