# Bubble Sort(Optimized) & Find
# the time complexity of the code is between O(n) and O(n^2),
# depending on the initial state of the array and whether the optimization is effective.
# The space complexity is O(1), indicating constant space usage.

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [7, 10, 4, 3, 20, 15]
K = 3
bubble_sort(arr)
print(arr[K - 1])

# Time complexity O(n) and O(n^2)
# Space complexity O(1)
# Refer sort/bubble.py file to understand bubble sort
