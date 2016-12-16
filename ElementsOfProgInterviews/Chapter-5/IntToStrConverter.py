# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:14:32 2016

@author: Parvez
"""
def intToStr(i):
    s=''
    isNeg=False
    if i<0:
        i=-i
        isNeg=True
    while(i):
        s=s+chr(i%10+ord('0'))
        i//=10
    if(isNeg):
        s=s+'-'
    #s=s[::-1]
    s=''.join(reversed(s))
    return s
    
print(intToStr(-123))