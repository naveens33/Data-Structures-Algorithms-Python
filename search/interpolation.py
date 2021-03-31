
def search(arr,x,lo,hi):
    if(lo<=hi and x>=arr[lo] and x<=arr[hi]):
        pos = lo + int(((hi - lo) / (arr[hi] - arr[lo]) *
                    (x - arr[lo])))
        print(pos)
        if arr[pos]==x:
            return pos
        elif arr[pos]<x:
            return search(arr,x,pos+1,hi)
        else:
            return search(arr, x, lo, pos-1)

'''
arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]

print(search(arr,35,0,len(arr)-1))
'''
arr = [x*2 for x in range(1,10)]
print(arr,len(arr))
print(search(arr,12,0,len(arr)-1))