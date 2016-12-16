# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:56:48 2016

@author: Parvez
"""
"""
Method1: Multiplication using bitwise operations:
    
Addition-Addition uses the principle that without
any carry sum=A xor B
If there's any carry (given by A&B) left shift it carry
and add again to sum above. There will again be carry. Keep repeating
it until carry =0
"""

def Add(a,b):
   carry=a&b
   s=a^b
   while(carry):
       shiftedCarry=carry<<1
       carry=s & shiftedCarry
       s=s^shiftedCarry
   return s

print(Add(5,7))

def Add2(x,y):
    if(y==0):
        return x
    else:
        return Add2(x^y,(x&y)<<1)
print(Add2(5,6))
       
def multiply(x,y):
    p=0
    if(y<0):
        return -multiply(x,-y)
    while(y):        
        if(y&1):
            p=(Add2(x,p))
        y>>=1
        x<<=1
    return p

print(multiply(2,-4))

#%%
"""
Method2: Multiplication using recursion:

Complexity : O(n)
"""

def multiply2(x,y):
    if y==0:
        return 0
    elif y>0:
        return(x+multiply2(x,y-1))
    else:
        return(-multiply2(x,-y))
    
print(multiply2(3,-4))


#%%
"""
Method3: Multiplication: 
Russian peasant method: Uses bitwise and + operators

Complexity : O(log(n))
"""

def multiply3(x,y):
    p=0
    if y<0:
        return -multiply3(x,-y)
    while(y):
        if(y&1):
            p=p+x
        y>>=1
        x<<=1
    return p
print(multiply3(3,100))