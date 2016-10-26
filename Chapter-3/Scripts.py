# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:37:19 2016

@author: Parvez
"""
#%% Stack Implementation
import linearDS
s=Stack()
s.isEmpty()
s.push(5)
s.push('nam')
s.items
s.pop()

#%% Parentheses Checker
import linearDS
def parCheck(expr):
    s=Stack()
    i=0
    balanced=True
    while i<len(expr) and balanced:
        symbol= expr[i]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            elif symbol==")":
                s.pop()
        i=i+1
    if balanced and s.isEmpty():
        return True
    else:
        return False
                
#%% General Parentheses Checker
import linearDS
def genParCheck(expr):
    s=Stack()
    i=0
    balanced=True
    while i<len(expr) and balanced:
        symbol=expr[i]
        if symbol in "[{(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top=s.pop()
                if not matches(top, symbol):
                    balanced=False
        i=i+1
    if balanced and s.isEmpty():
        return True
    else:
        return False
        
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(genParCheck('{{([][])}()}'))
print(genParCheck('[{()]'))

#%%Decimal to Binary
from pythonds.basic.stack import Stack
def decToBin(dec):
    binStack=Stack()
    while dec>0:
        rem=dec%2
        binStack.push(str(rem))
        dec=dec//2
    binstr=""
    while not binStack.isEmpty():
        binstr=binstr+binStack.pop()
    
    print(binstr)

decToBin(3)

#%% Decimal to octa
from pythonds.basic.stack import Stack
def decToBin(dec):
    binStack=Stack()
    while dec>0:
        rem=dec%8
        binStack.push(str(rem))
        dec=dec//8
    binstr=""
    while not binStack.isEmpty():
        binstr=binstr+binStack.pop()
    
    print(binstr)

decToBin(9)

#%% Base Converter
from pythonds.basic.stack import Stack
def baseConverter(dec,base):
    baseStack=Stack()
    while dec>0:
        rem=dec%base
        if rem>9:
            rem=chr(ord('A')+rem-10)
        baseStack.push(str(rem))
        dec=dec//base
    binstr=""
    while not baseStack.isEmpty():
        binstr=binstr+baseStack.pop()
    
    print(binstr)
    
baseConverter(12132435454656,26)