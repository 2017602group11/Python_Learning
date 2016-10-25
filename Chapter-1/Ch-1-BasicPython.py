# -*- coding: utf-8 -*-
def hello():
    """Print "Hello World" and return None"""
    print("Hello World")

# main program starts here
hello()


print(2**10)
print(3/5)
print(3//5)

print(True or False)
print(True and False)
print(not(True))

#LISTS
myList=[1,3.4,True,'name']
rep_List=myList*2
rep_List2=[myList]*2
myList[0:3]
new_List=myList[0:2]+myList[2:4]
1 in myList

a=[1,2,3,4]
b=a
c=list(a)
d=a[:]
a.append(5)

(54).__add__(21)

a=range(4)
type(a)
_lst=list(a)
_lst2=list(range(0,4,1))
_lst3=list(range(0,4,-1))
# list(range(3,0,0.5)) Throws Error: 'float' object cannot be interpreted as an integer



#STRINGS
name='name'
name[2]
name.split('m')

#TUPLE
T=(1,2,3,4)
L=[1,2,3,4]
print(type(T))
print(type(L))

T*3
#T[1]='two' ERROR: 'tuple' object does not support item assignment

#Set
mySet={1,2,False,'a'}
mySet={1,1,2,False,'a'}
# mySet[2] : Error: 'set' object does not support indexing
# mySet*3 : Set cannot be repeated


myDict={'UP':'lko', 'JK':'srinagar'}
myDict['JK']

myDict.keys()

myDict.values()

myDict.items()

lst=list(myDict.items())

myDict.get('UP')

myDict.get('None',123)

for k in myDict:
    print("Capital of", k, "is",myDict[k])
    
# Adding new key-value
myDict['Delhi']='New Delhi'

#Input-Output

print('abc','pqr',sep='***', end='nnn')
_name=input('enter your name')
_age=input('enter age')
 print("%s is %d years old" %(_name,_age))


#Problem ActiveCode3: self-check2
##PRINT List
print([ch for ch in "".join(['cat','dog','rabbit'])])
print ([word[i] for word in ['cat','dog','rabbit'] for i in range(len(word))])
print ([ch for word in ['cat','dog','rabbit'] for ch in word])
##PRINT Set
print(list({ch for ch in "".join(['cat','dog','rabbit'])}))
print (list(set([ch for word in ['cat','dog','rabbit'] for ch in word])))


"""1.11. Exception Handling"""
import math
num=float(input('enter a number'))
try:
    print('sqrt of the num is', math.sqrt(num))
except:
    if (num<0):
        print('printing root of absolute value')
        print('sqrt of the num is', math.sqrt(abs(num)))


#raise an except
anumber=float(input('enter a number'))
if anumber < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(anumber))


"""1.12. Defining Functions """
def square(num):
    print(num**2)
num=4
square(num)

#SQUARE ROOT USING NEWTON'S METHOD
def squareroot(n):
    root=n/2 #Make initial guess
    for i in range(30):
        root=0.5*(root+(n/root))
    return root
        
squareroot(100)


"""1.13. Object-Oriented Programming in Python: Defining Classes"""
# 1.13.1. A Fraction Class

from Rationals import Fraction
        
myfraction=Fraction(3,5)
print(myfraction)
print("I ate", myfraction, "of the roti")
myfraction.__str__()
str(myfraction)

f1=Fraction(1,2)
f2=Fraction(2,3)
f3=f1+f2
f4=Fraction(0,3)
print(f3)
print(f1==f2)
print(f1>f2)
print(f1<f2)
print(f1*f2)
print(f2.reciprocal())
print(f1/f2)
print(-f1)
print(f1-f2)


# 1.13.2. Inheritance: Logic Gates and Circuits
from Logic import AndGate
    
g1 = AndGate("G1")
g1.getOutput()