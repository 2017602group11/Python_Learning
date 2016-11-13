# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 20:43:25 2016

@author: Parvez
"""


def ClmnEncodr(s):
    res=0
    for c in s:
        v=ord(c) - ord('A')+1
        res=res*26+v
    return res
        
print(ClmnEncodr('AD'))