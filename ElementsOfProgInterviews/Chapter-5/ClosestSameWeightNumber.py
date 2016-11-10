# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:33:26 2016

@author: Parvez
"""

def SameWeightNum(x):
    c=3 # 3=0b11
    for i in range(64):
        if((x>>i&1)!=(x>>i+1&1)):
            return x^c
        else:
            c<<=1
    return x
 
N=55
print(bin((N)))
print(bin(SameWeightNum(N)))