# Maximum and minimum of an array using minimum number of comparisons
# Linear Search
li = [34, 54, 12, 90, 5, 77]
min, max = 0, 0
if li[0] < li[1]:
    min = li[0]
    max = li[1]
else:
    min = li[1]
    max = li[0]
for i in li:
    if i < min:
        min = i
    elif i > max:
        max = i
print(min, max)

'''
Finds the minimum and maximum elements in a list (`li`). Here's the analysis of the time and space complexity for this code:

Time Complexity:
The code iterates through the list once, comparing each element to find the minimum and maximum values. Therefore, the time complexity of this code is O(n), where n is the number of elements in the list `li`. As the input size increases, the time taken by the algorithm grows linearly.
        
Space Complexity:
The code uses a fixed amount of additional space to store the minimum (`min`) and maximum (`max`) values. The space complexity is O(1) because the amount of memory used does not depend on the size of the input.

In summary, the time complexity of the code is O(n), where n is the number of elements in the list. The space complexity is O(1) as it doesn't use any extra space proportional to the input size. The code efficiently finds the minimum and maximum elements in a single pass through the list.
'''