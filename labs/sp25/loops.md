
# Loop Conversion 
For each loop shown below:
1.  Determine *exactly* (either a literal value or a function of *n*) how many times the loop will repeat. Then determine the Big-0 characterization of the loop. 
2.  Translate to the equivalent while/for loop. This means a loop with a counter (i,j,k, etc.) that takes on the exact same sequence of values, repeats the same number of times, and has the same Big-O characterization.
 

```python
j = 2
while j < n:
    ...
    j += 3
```

```python
for i in range(0,n-1,n//3):
    ...
```

```python
k = n+5
while k >= 4:
    ...
    k -= 2
```

```python
for i in range(n):
    for j in range(n-1,i-1,-1):
        ...
```

