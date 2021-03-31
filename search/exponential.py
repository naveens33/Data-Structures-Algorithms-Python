def search(seq, target, left, right):

    while left <= right:
        mid = left + (right - left) // 2
        if seq[mid] == target:
            return mid
        elif seq[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

li = [1, 3, 5, 8, 9, 11, 13, 15, 23, 38, 44]
target = 38
if li[0] == target:
    print(target, "found in index 0")
else:
    i = 1
    n = len(li)
    while i < n and li[i] <= target:
        i *= 2
    left = i//2
    right = min(i,n-1)
    print("len: {}".format(n),"\nexponential: {}".format(i),"\nleft: {}".format(left),"\nright: {}".format(right))
    ans = search(li, target, left, right)
    if ans is not None:
        print(target, "found in index", ans)
    else:
        print(target, "not found")
