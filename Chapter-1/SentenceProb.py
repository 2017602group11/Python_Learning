# -*- coding: utf-8 -*-
from random import choice
from string import ascii_lowercase

def random(n):
    chars=' ' +ascii_lowercase
    L="".join(choice(chars) for i in range(n))
    return L


def score(goal, teststr):
    c=0
    for i in range(len(goal)):
        if goal[i]==teststr[i]:
            c+=1
    scr=c*100/len(goal)
    return (scr)


goal='parvez rafi'
best_scr=0;
best_match='';
m=0
#for j in range(100000):
while best_scr<=90:
    m+=1
    test_wrd=random(len(goal))
    scr=score(goal,test_wrd)
    if(best_scr<scr):
        best_scr=scr
        best_match=test_wrd

print(best_scr)
print(best_match)
print('iteractions it took=',m)
    
