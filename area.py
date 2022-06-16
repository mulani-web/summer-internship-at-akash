def rec(l,w):
    print("area of rectangle is :",l*w)
def squ(a):
    print("area of square is :",a*a)
def cir(r):
    a = 3.14
    print("area of circle is:",a*r*r)
a=int(input("enter the length and breadth:"))
b=int(input("enter the breadth:"))
rec(a,b)
a=int(input("enter the side:"))
squ(a)
a=int(input("enter the radius:"))
cir(a)
