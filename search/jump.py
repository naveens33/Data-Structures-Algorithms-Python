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