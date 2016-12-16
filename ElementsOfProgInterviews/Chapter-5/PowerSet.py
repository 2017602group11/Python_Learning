# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:16:50 2016

@author: Parvez
"""
""""""
i={4,5,1,3,6,7,4}
from itertools import chain, combinations
for z in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
    print(z)
    
#%%
"""
Method 2:
"""
s={4,5,1}
pow_set=set()
lst=list(s)
len_s=len(lst)
for i in range(0,2**len_s):
    sub_s=set()
    print(i," ",bin(i))
    c=0
    while(i):
        if(i&1):
            print(c)
            sub_s.add(lst[c])
        i>>=1
        c+=1
    print(sub_s)
    pow_set.add(frozenset(sub_s))
print('powerset is:',pow_set)

#%%

"""
Method 3

"""

def PowerSet(S):
    subS=[[]]
    for elt in S:
        for j in range(len(subS)):
            subS.append(subS[j]+[elt])
            print(subS)  

PowerSet({2,3,5})
    
    
#%%
"""
Method4: Using Recursion
"""

def power_set_r(set_):
    def k_subsets(k, start_ind):
        if k == 0:
            return [[]]
        else:
            subsets = []
            for ind in range(start_ind, len(set_) - k + 1):
                for subset in k_subsets(k - 1, ind + 1):
                    subsets.append(subset + [set_[ind]])
            return subsets

    subsets = []
    for k in range(len(set_) + 1):
        for subset in k_subsets(k, 0):
            subsets.append(subset)
    return subsets

power_set_r([12,4,5])
