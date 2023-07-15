li = [0, 1, 1, 1, 0, 1, 1]
left = 0
right = len(li) - 1

while left < right:
    print(left, right)
    while li[left] == 0 and left < right:
        left += 1

    while li[right] == 1 and left < right:
        right -= 1

    if li[left] > li[right]:
        li[left] = 0
        li[right] = 1
        left += 1
        right -= 1

print(li)
