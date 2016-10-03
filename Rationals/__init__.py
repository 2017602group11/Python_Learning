#Contains implementation of Rational Numbers in Python
def GCD(m,n):
    r= m % n
    while r != 0:
        m=n
        n=r
        r= m % n
    return n
    
class Fraction:
    def reciprocal(self):
        if self.num !=0:
            return Fraction(self.deno,self.num)
        else:
            raise ZeroDivisionError
    def __init__(self,top,bottom):
        self.num=top
        self.deno=bottom
    def show(self):
        print(self.num,"/",self.deno)
    def __str__(self):
        return str(self.num)+"/"+str(self.deno)
    def __add__(self,f):
        new_num=self.num*f.deno + self.deno*f.num
        new_deno=self.deno*f.deno
        g=GCD(new_num,new_deno)
        return Fraction(int(new_num/g), int(new_deno/g))
    def __mul__(self,f):
        new_num=self.num*f.num
        new_deno=self.deno*f.deno
        g=GCD(new_num,new_deno)
        return Fraction(int(new_num/g), int(new_deno/g))
    def __truediv__(self,f):
        return self*f.reciprocal()
    def __sub__(self,f):
        return self.__add__(-f)
    def __eq__(self,f):
        return (self.num*f.deno) == (self.deno*f.num)
    def __gt__(self,f):
        return (self.num*f.deno) > (self.deno*f.num)
    def __lt__(self,f):
        return (self.num*f.deno) < (self.deno*f.num)
    def __neg__(self):
        return Fraction(-self.num, self.deno)
