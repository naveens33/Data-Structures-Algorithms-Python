# two-pointer approach
li = [1, 2, 3, 5, 6]

for i in range(len(li)//2):
    li[i], li[len(li)-i-1] = li[len(li)-i-1], li[i]

print(li)

'''
This code using a two-pointer approach. 
Here's the analysis of the time and space complexity for this code:

Time Complexity:
The code iterates over the first half of the list, performing a swap operation for each element. 
Therefore, the time complexity of this code is O(n/2), which simplifies to O(n), 
where n is the length of the list `li`.

Space Complexity:
The code uses a fixed amount of additional space to store the list `li`. 
The space complexity is O(1) because the amount of memory used does not depend on the size of the input.

In summary, the time complexity of the code is O(n),
and the space complexity is O(1), where n is the length of the list `li`.
'''