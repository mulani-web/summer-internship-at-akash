from tkinter import N


n = 10
m = 15
print("before swapping")
print("n:",n)
print("m:",m)
n,m = m,n
print("after swapping")
print("n:",n)
print("m:",m)
n ^=m
m ^=n 
n ^=m
print("again after swapping")
print(n)
print(m)