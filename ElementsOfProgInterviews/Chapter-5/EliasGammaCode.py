# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:07:08 2016

@author: Parvez
"""
def intTobin(n):
    b=''
    while n!=0:
        b=str((n&1))+b
        n>>=1
    return b

def encodeElis(num):
    b_num=intTobin(num)
    ZerostoAdd='0'*(len(b_num)-1)
    return ZerostoAdd + b_num
   
print(encodeElis(13))