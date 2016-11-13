# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 18:31:08 2016

@author: Parvez
"""

def baseConverter(ip_s,b1,b2):
    decNum=0;
    op_s=''
    while(ip_s):
        dig=ord(ip_s[-1])-ord('0')
        if not (0<=dig<=9):
            dig= ord(ip_s[-1])-ord('A')+10
        decNum=decNum*b1+int(dig)
            
        ip_s=ip_s[0:-1]
    while(decNum):
        rem=decNum%b2
        if rem>9:
            rem=chr(ord('A')+rem-10)
        op_s=op_s+str(rem)
        decNum//=b2
    op_s=op_s[::-1]
    return op_s
    
print(baseConverter('FFFF',16,10))