from statistics import mean


a = []
print("enter the numbers")
for i in range(0,5):
    tot = int(input())
    a.append(tot)
    print(a)

print("average of numbers is:",mean(a))
    