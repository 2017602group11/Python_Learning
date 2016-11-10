# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:12:45 2016

@author: Parvez
"""
"""
Method 1:
"""

def bitRev(N,l):
    #l=len(bin(N))-2  #to cut down additional 2 digits 0b
    Nrev=N
    for i in range(1,l):
        Nrev<<=1
        N>>=1
        Nrev|=(N&1) # AND with LSB on N
    return (Nrev&(2**l -1)) #To slice last l LSBs of Nrev
N=1
print(bin(N))
print(bin(bitRev(N,4)))

#%%

"""
Method 2:FOR LARGE NUMBERS
    a. Create lookup table of all reversed 16-bit integers
    b. Divide large numbers

"""
precomp_bitRev=[]
for i in range(2**16):
    precomp_bitRev.append(bitRev(i,16))
    
def largeBitRev(N):
    Nrev=precomp_bitRev[(N>>48)&65535]| \
         precomp_bitRev[(N>>32)&65535]<<16| \
         precomp_bitRev[(N>>16)&65535]<<32| \
         precomp_bitRev[N&65535]<<48 #65535 = 0xFFFF
    return(Nrev)

print(largeBitRev(18446744073709551615))