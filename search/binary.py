'''
def search(seq, target, left, right):

    while left <= right:
        print(left,right)
        mid = left + ((right - left) // 2)
        print("calc",left + (right - left))
        print(mid)
        if seq[mid] == target:
            return mid
        elif seq[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


def is_sorted(seq):
    if seq == sorted(seq):
        return True
    else:
        return False


#li = [32, 54, 22, 11, 67]
#li = ['Mason','Nalty','Ochoa','Patel','Quinn','Reily','Smith']
li=[1,3,5,7,9,11,13,15]
li if is_sorted(li) else li.sort()
print(li)
#target = 32
#target = 'Reily'
target = 9
left = 0
right = len(li) - 1
ans = search(li, target,left,right)
if ans is not None:
    print(target, "found in index", ans)
else:
    print(target, "not found")
'''


def search_(li, target,l ,r):
    middle  = l + (r-l)//2
    if(l>r):
        return None
    else:
        if li[middle]==target:
            print(middle)
        elif target < li[middle]:
            search_(li, target, l, middle-1)
        else:
            search_(li, target, middle+1,r)

li = [1, 3, 5, 7, 9, 11, 13, 15]
search_(li, 11, 0, len(li))
