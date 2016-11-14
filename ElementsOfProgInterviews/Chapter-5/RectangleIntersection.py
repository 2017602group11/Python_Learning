# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:31:19 2016

@author: Parvez
"""
class Rect:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.xcenter=(x+w/2) #x-coordinate of center
        self.ycenter=(y+w/2)  #y-ccordinate of center

    def __str__(self):
        return "x:"+ str(self.x)+"\ny:"+str(self.y)+ \
        "\nWidth:"+str(self.width)+ "\nHeight:"+ str(self.height)

def isIntersect(R1,R2):
    return ((abs(R1.xcenter-R2.xcenter)<=(R1.width+R2.width)/2)& \
            (abs(R1.ycenter-R2.ycenter)<=(R1.height+R2.height)/2))
    
def intersectRect(R1,R2):
    if(isIntersect(R1,R2)):
        x=max(R1.x,R2.x)
        y=max(R1.y,R2.y)
        w=min(R1.x+R1.width,R2.x+R2.width)-x
        h=min(R1.y+R1.height,R2.y+R2.height)-y
        return Rect(x,y,w,h)
    else:
        print("They are non-intersecting rectangles")
            
    
Ra=Rect(0,0,1,1)
Rb=Rect(1,1,1,1)

print(isIntersect(Ra,Rb))
print(intersectRect(Ra,Rb))