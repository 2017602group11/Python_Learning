# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:28:02 2016

@author: Parvez
"""
#%%
#time.time()
import time

def sumOfN(N):
    start=time.time()
    s=0
    for I in range(1,N+1):
        s=s+I
    end=time.time()
    return s, end-start
    

print("%d is the sum computed in %10.9f" %(sumOfN(999999)))
#%%

def sumofN(N):
    start=time.time()
    s=N*(N+1)
    end=time.time()
    return s,end-start
    
print("%d is sum computed in %10.12f" %(sumofN(999999999)))

#%%
"""Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list.
 O(n2). The second function should be linear O(n)."""

#Func1
def Max1(l):
    hghst=l[0]
    for i in l:
        if i>hghst:
            hghst=i
    return hghst
    
def Max2(l):
    for i in l:
        for j in l:
            if i<j:
                hghst=j
    return hghst
    
lst=[2,1,4,5,8,2]
print("Using O(n)=",Max1(lst))
print("Using O(n2)=",Max2(lst))
#%% Anagram Detection
"""
Method 1:
Our first solution to the anagram problem will check to see that each character
 in the first string actually occurs in the second. If it is possible to
 “checkoff” each character, then the two strings must be anagrams. 
"""
def anagramSolution1(s1,s2):
    if len(s1) != len(s2):
        return False
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd','dcbaa'))

#%%
"""
Anagram Detection Method 2:SORTING
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:07:33 2016

@author: Parvez
"""

def anagramSolution2(s1,s2):
    alist1=list(s1)
    alist2=list(s2)
    alist1.sort()
    alist2.sort()
    print(alist1)
    matches=True
    pos=0
    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos=pos+1
        else:
            matches=False
    return matches        
anagramSolution2('rafi','fira')

#%%
"""
Anagram Detection Method3: Count and Compare
"""
def anagramSolution3(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        c1[pos]=c1[pos]+1
    
    for j in range(len(s2)):
        pos=ord(s2[j])-ord('a')
        c2[pos]=c2[pos]+1

    k=0
    matches=True
    while k<26 and matches:
        if c1[k]==c2[k]:
            k=k+1
        else:
            matches=False
    return matches
    
anagramSolution3('zevrapp','parpvez')