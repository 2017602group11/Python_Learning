# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:24:18 2016

@author: Parvez
"""
def GCD(A,B):
    rem=A%B
    if rem == 0:
        return B
    else:
        return GCD(B,rem)

print(GCD(16,12))