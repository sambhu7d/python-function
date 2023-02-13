# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:25:25 2023

"""

def area(l,b):
    a=l*b
    return a

def area(s):
    a=s**2
    return a

def area(r):
    a=pi*(r**2)
    return a

c=int(input("Input a number to find area of circle"))


print("area of circle:",area(c))
print("area of square:",area(7))
print("area of rectangle:",area(2, 3))
