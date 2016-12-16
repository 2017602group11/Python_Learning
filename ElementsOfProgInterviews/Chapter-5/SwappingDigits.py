# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 01:16:58 2016

@author: Parvez
"""

""" 5.2: A 64-bit integer can be viewed as an array of 64 bits, with the bit at
index 0 corresponding to the least significant bi.t,and the bit at index 63corresponding to the
most significant bit. Implement code that tnJces as input a 64-bit integer x and swaps the bits
at indices i and j."""

def swap(num,i,j):
    num=int(num,2)
    if (num>>i)&1 != (num>>j)&1: #check if ith and jth digits differ
        num^=(1<<i)|(1<<j)
    return bin(num)
    
print(swap('110100',2,0))