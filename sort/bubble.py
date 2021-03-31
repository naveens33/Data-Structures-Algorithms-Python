"""
Improved Bubble sort -> During any iteration, if there are no swaps then we can
claim that our array is already sorted.
"""
li = [5, 1, 9, 3]
for i in range(len(li)):
    isSwap = False
    for j in range(len(li) - i - 1):
        if li[j] > li[j + 1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp
            isSwap = True
    print(isSwap)
    if isSwap == False:
        break
    print(li)
