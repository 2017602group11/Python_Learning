# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:12:33 2016

@author: Parvez

* Implement the simple methods getNum and getDen that will return 
the numerator and denominator of a fraction.

* In many ways it would be better if all fractions were maintained in lowest
 terms right from the start. Modify the constructor for the Fraction class so 
 that GCD is used to reduce fractions immediately. Notice that this means the 
 __add__ function no longer needs to reduce. Make the necessary modifications.
 
 Research the __radd__ method. How does it differ from __add__? When is it used? Implement __radd__.
"""
def GCD(m,n):
    r= m % n
    while r != 0:
        m=n
        n=r
        r= m % n
    return n
    
class Fraction:
    def __init__(self,top,bottom):
        hcf=GCD(top,bottom)
        self.num=int(top/hcf)
        self.deno=int(bottom/hcf)
    def __str__(self):
        return str(self.num)+"/"+str(self.deno)
        
def getNum(f):
    return(f.num)
    
def getDen(f):
    return(f.deno)
    
    
f1=Fraction(3,4)
print(getNum(f1))
print(getDen(f1))

f2=Fraction(7,21)
print(f2)