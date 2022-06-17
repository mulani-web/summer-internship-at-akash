def ty(a):
    if a<0:
        print("number is negative")
    elif a>0:
        print("number is positive")
    else:
        print("number is zero")

def nu(a,b):
    if a>b:
        print(a)
    elif a<b: 
        print(b)
    else:
        print("both are equal")
   
n = int(input("enter the number:"))
m = int(input("enter the comparison numer:"))
ty(n)
nu(n,m)

    
 