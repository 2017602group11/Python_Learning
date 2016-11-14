# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:18:05 2016

@author: Parvez
"""
"""
Method 1: Complexity log(y)
"""
def divide(x,y):
    if(y<0):
        return -divide(x,-y)
    if(x<0):
        return -divide(-x,y)
    if(x<y):
        return 0
    else:
        return(1+divide((x-y),y))

print(divide(-4,3))

#%%

"""
Method 2: Complexity(log(y))
"""
def divide2(x,y):
    power=0
    if(x<y):
        return 0
    while((1<<power)*y<=x):
        power+=1
    part=1<<(power-1)
    print(power)
    return part+divide2(x-part*y,y)
    
print(divide2(115,5))
            
    
    
    