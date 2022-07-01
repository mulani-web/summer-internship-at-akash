def removeDuplicates(arr, n):
	temp = list(range(n))
	j = 0;
	for i in range(0, n-1):
		if arr[i] != arr[i+1]:
			temp[j] = arr[i]
			j += 1
	temp[j] = arr[n-1]
	j += 1
	for i in range(0, j):
		arr[i] = temp[i]
	return j
def ar(name):
    a = []
    for i in range(len(name)):
      a += name[i]
    return(a)
name = input("enter the string:\n")
print(name)
arr = ar(name)
n = len(arr)
n = removeDuplicates(arr, n)
for i in range(n):
	print ((arr[i]), end = " ")