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



#%%
"""
Method 2:
"""

def GCD(x,y):
    if (x==0) & (y!=0):
        return y
    elif (y==0) & (x!=0):
        return x
    elif x>y:
        return GCD(y,x-y)
    else:
        return GCD(x,y-x)
        
          
print(GCD(8,12))