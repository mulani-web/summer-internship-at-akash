from re import I


n = int(input("enter the number:"))
fac = 1
if n == 0:
    print("invalid input")
else:
    for i in range(1,n+1):
        fac = fac * i 
    print(fac)