import math


def search(arr, x, n):
    step = math.sqrt(n)
    print(step)
    prev=0
    while arr[int(min(step,n))]<x:
        prev = step
        step +=math.sqrt(n)
        if prev>=n:
            return -1
    print(prev)
    while arr[int(prev)]<x:
        prev+=1
        if arr[int(prev)]==x:
            return prev


arr = [x*10 for x in range(1,10) ]
x = 70
n = len(arr)

index = search(arr, x, n)
print(index)


import math

li = [24, 56, 69, 70, 83, 99, 109, 145, 154, 167]

l = 0
r = len(li)
s = math.ceil(math.sqrt(r))
t = 69
while s <= len(li):
    if t > li[s]:
        l = s
        s += s
    elif t <= li[s]:
        r = s
        break

for i in range(l, r + 1):
    if (li[i] == t):
        print(i)
        break
else:
    print("-1")
