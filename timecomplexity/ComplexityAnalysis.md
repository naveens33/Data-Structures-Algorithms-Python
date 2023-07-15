# Time Complexity vs Space Complexity

Space complexity and time complexity are two important concepts in computer science and algorithm analysis. Here's a brief explanation of what they mean:

## Time complexity
Time complexity is the amount of time an algorithm takes to run as a function of the input size. It measures how much time an algorithm will take to execute on a given input, as the size of the input grows. Time complexity is typically measured in terms of the number of basic operations performed by the algorithm, such as comparisons, additions, or swaps.

## Space complexity: 
Space complexity is the amount of memory an algorithm requires as a function of the input size. It measures how much memory an algorithm will take to execute on a given input, as the size of the input grows. Space complexity is typically measured in terms of the number of bytes or bits required by the algorithm.

In general, algorithms with lower time complexity are more desirable than those with higher time complexity, because they are faster and more efficient. Similarly, algorithms with lower space complexity are more desirable than those with higher space complexity, because they use less memory and are more efficient in terms of storage.

However, it's important to note that time and space complexity are often inversely related. In other words, improving the time complexity of an algorithm may come at the cost of increasing its space complexity, and vice versa. It's also possible for an algorithm to have good time complexity but poor space complexity, or vice versa, so it's important to consider both when analyzing and optimizing algorithms.

## Time Complexity Analysis

1. Loop
```
for i in range(n+1):
    x= y + z
```
Time complexity => O(n)

2. Nested Loop
```
for i in range(n+1):
    for j in range(n+1):
        x = y + z
```
Time complexity => O(n^2)

3. Sequential Statement

   1. 
   ```a = a + b```
   2. 
   ```
   for i in range(n+1)
      x = x + z
   ```
   3.
   ```
      for j in range(n+1)
         c = d + e
   ```
Time Complexity => C + Cn + Cn => O(n)

4. If else statement
```
if(cond.):
    pass => O(n)
else:
   pass => O(n^2)
```
Time Complexity => O(n^2)

Order of time complexity,

O(1) < O(log n) < O(n) < O(n log n) < O(n^c) < O(n!)

O(n) => Linear time 

O(1) => Constant time

O(n^2) => Quadratic time 

How to find the time complexity.
1. Find the fastest growing term
2. Take out the coefficient 

When, T = an + b => O(n)

When, T = an^2 + dn + e => O(n^2)



