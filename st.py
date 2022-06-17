a = int(input("enter the no.")) 
n = int(input("enter start no:"))
m = int(input("enter end no:"))
if n==0 or m ==0:
    print("not able")
else:
  for i in range(n,m+1):
     if i%a == 0:
       print(i)
     else:
        pass
