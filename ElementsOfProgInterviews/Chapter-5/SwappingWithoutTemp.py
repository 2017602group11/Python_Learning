def Swap1(a,b):
    a=a^b
    b=b^a
    a=a^b
    return a,b

print(Swap1(3,5))

#%%
def Swap2(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
    
print(Swap2(3,5))
