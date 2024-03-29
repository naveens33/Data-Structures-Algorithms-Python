"""
Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given
array is 7.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(log(n))
"""

# Sort & Find
N = 6
arr = [7, 10, 4, 3, 20, 15]
K = 3

# Python's built-in sort() method, which typically implements an efficient sorting algorithm like
# Timsort (a hybrid of merge sort and insertion sort).
arr.sort()
print(arr[K - 1])

# Time complexity:  O(n log n)
# Space complexity:  O(1)