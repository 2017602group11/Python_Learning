# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:44:56 2016

@author: Parvez
"""
def strToInt(s):
    if s=='':
        return 0
        
    num=0
    isNeg = False
    if (s[0]=='-'):
        isNeg=True
        s=s[1:]
    
    for i in s:
        j=ord(i)-ord('0')
        if 0<=j<10:
            num=num*10+j
        else:
            raise 'Error: Given String cannot be converted to Int'
           
    if isNeg:
        num=-num
        
    return num

print(strToInt(''))