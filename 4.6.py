# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:18:20 2020

@author: kt998
"""
def computepay(hrs,rate):
    hrs = float(hrs)
    rate = float(rate)
    if hrs > 40 :
        reg = hrs*rate
        otp = (hrs - 40.0)*(rate*0.5)
        xp = reg + otp
    else :
        xp = hrs *rate 
    return(xp)
hrs = input("Enter Hours")    
rate = input("Enter rate:")
p = computepay(hrs,rate)
print("Pay",p) 