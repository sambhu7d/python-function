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

c=float(input("Input a number to find area of circle"))
s=int(input("Input a number to find area of square"))
l,b=float(input("Input length"))
,float(input("Input a breath"))
print("area of circle:",area(c))
print("area of square:",area(s))
print("area of rectangle:",area(l,b))
