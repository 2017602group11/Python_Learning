# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:15:50 2016

@author: Parvez
"""

"""Method 1: perform XOR in between every digit"""
def parity1(x):
    r=0
    while x:
        # & gives rightmost digit
        r=r^(x&1)
        
        #>> means right shift by 1
        x=x>>1
    return r    
    
print(parity1(4))

#%%
"""Method 2: Calculate parity based only on 1s present in the number"""
def parity2(x):
    r=0
    while x:
        r^=1 #Alternates previous r on removal of every 1
        x&=(x-1) #removes LSB
    return r    
    
print(parity2(7))
   
#%% 
"""Method 3: for very large numbers precompute and 
create a lookup for parities of every 16 digit. Divide
Large number into batch of 16 digit and look up parity of 
each batch and futher calculate parities of these numbers"""


parity_lookup=[]
for i in range(2**16):
    parity_lookup.append(int(parity2(i)))
    

def parity3(num):
    res=parity_lookup[num>>48]^ \
        parity_lookup[(num>>32)&(16**4-1)]^ \
        parity_lookup[(num>>16)&(16**4-1)]^ \
        parity_lookup[(num)&(16**4-1)]  #16**4-1 is 0xFFFF for masking
    return res
                      
parity3(65535)