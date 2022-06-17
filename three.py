a = int(input("enter the number:"))
b = int(input("enter the number:"))
c = int(input("enter the number:"))
if a>b and a>c:
    print("a is greatest among three")
elif b>c and b>a:
    print("b is greatest among three")
else:
    print("c is greatest among three")