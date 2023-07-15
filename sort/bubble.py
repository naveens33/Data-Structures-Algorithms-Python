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

"""
Important to note:
# Time complexity O(n) and O(n^2)

To demonstrate inputs where the time complexity of the Bubble Sort algorithm falls between O(n) and O(n^2), 
we can consider inputs that are partially sorted or have a specific pattern. Here are a few examples:

1. Partially Sorted List:
   Input: [1, 2, 3, 7, 5, 6]
   In this case, the first three elements are already sorted, but the remaining elements are not. 
   The time complexity would be closer to O(n) because fewer passes are required to sort the array.

2. Reversed List with a Few Elements Sorted:
   Input: [6, 5, 4, 1, 2, 3]
   In this case, the first three elements are in reverse order, 
   but the remaining elements are already sorted. 
   The time complexity would be closer to O(n) because after the initial passes, 
   the sorted elements will "bubble up" to their correct positions.

3. Alternating Sorted and Unsorted Blocks:
   Input: [1, 5, 2, 6, 3, 7, 4, 8]
   In this case, the array consists of alternating blocks of sorted and unsorted elements. 
   The time complexity would be closer to O(n^2), 
   but it may be slightly better than a completely reversed list because some elements are already sorted.

4. Few Elements Out of Order:
   Input: [1, 2, 4, 3, 5, 6]
   In this case, there are a few elements that are out of order within an otherwise sorted array. 
   The time complexity would be closer to O(n) because fewer passes are required to sort the array due to the small number of misplaced elements.

5. Randomly Shuffled List:
   Input: [5, 2, 1, 4, 3, 6]
   In this case, the array is randomly shuffled, 
   and the time complexity would be closer to O(n^2) as more passes are needed to sort the array completely.

"""