def reverse_li(li, start, end):
    while start <= end:
        li[start], li[end] = li[end], li[start]
        start += 1
        end -= 1


li = [1, 2, 3, 4, 5, 6]
reverse_li(li, 0, len(li) - 1)
print(li)

'''
This code defines a function `reverse_li` that takes a list `li` and two indices `start` and `end` as parameters. 
The function reverses the elements in the list between the given start and end indices by swapping corresponding 
elements. Here's the analysis of the time and space complexity for this code:

Time Complexity:
The code iterates through the list from the `start` index to the `end` index using a while loop. 
The number of iterations is roughly equal to half the length of the sublist to be reversed. 
Therefore, the time complexity of this code is O(n/2), which simplifies to O(n), 
where n is the number of elements in the sublist.

Space Complexity:
The code uses a fixed amount of additional space to store the list `li`. 
The space complexity is O(1) because the amount of memory used does not depend on the size of the input.

In summary, the time complexity of the code is O(n), 
where n is the number of elements in the sublist to be reversed. 
The space complexity is O(1) as it doesn't use any extra space proportional to the input size.
'''
