#Time complexity

Example:

n is prime or not. 

Solution1:
```
for i in range(2, n):
    if i%n == 0:
        print("{} is not prime number".format(n))
```

Solution2:
```
for i in range(2, math.sqrt(n)+1):
    if i%n == 0:
        print("{} is not prime number".format(n))
```

|Solution1|Solution2|
|---------|---------|
|If 1ms for a division. (n-2) times the loop will run. so, for n=11 it will take 9ms for n=101 it will take 99ms|(sqrt(n)-1 time the lop will run. So, for n=11 it will take 2ms for n=101 it will take 9ms|
|O(n)|O(sqrt(n))|
