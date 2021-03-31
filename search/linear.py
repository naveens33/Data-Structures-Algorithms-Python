def search(seq, target):
    for index, ele in enumerate(seq):
        if ele == target:
            return index
    else:
        return None


li = [23, 54, 12, 77, 39, 15, 1]
target = 39
ans = search(li, target)
if ans is not None:
    print(target, "found in index", ans)
else:
    print(target, "not found")
