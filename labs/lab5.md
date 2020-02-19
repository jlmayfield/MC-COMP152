---
layout: page
title: COMP151 - Lab 5
permalink: /teaching/COMP152/labs/lab5
---

0. Do the following problems: R-3.28, C-3.36, and C-3.44. Write your answers on a sheet of paper. For 3.36, provide a sketch of the algorithm, not full on python, and be sure to justify your running time.    

1. Write a function called *prefix_sum* which takes a single list of integers and computes the exclusive prefix sum that list. In an exclusive prefix sum, the ith element of the result is the sum of
the first i elements of the input. For example, the element at index 5 of the result
is the sum of the elements at indexes 0 to 4 in the input. This means if the given list were [3,4,5,6], then the returned list would be [0,3,7,12]. This function is very, very similar to what we saw last week in examples 3 and 4 and the prefix average seen in code fragments 3.2 through 3.4. *Your function should run in O(n) time*. Do not use append or + for lists in your code. (Hint: check out code fragment 3.4 again). Write the given example as a unit test and add unit tests for an empty list, a list of length 1, and a list of length 5.

2. Write a function called *multiple_map*. This function takes two inputs: a list of integers and a single integer. It returns a list of 0 or 1 values that is the same length as the given list. A value of 1 occurs at index i of the result if the value at same location in the given list is a multiple of the given value. For example, if the given list is [3,4,5,6,7,8,9] and the given number is 3, then the returned list is [1,0,0,1,0,0,1] because 3,6, and 9 are multiples of 3 but the remaining numbers are not. Again, your function must *not* use list append nor the + operator for lists and it should run in O(n) time.   Write the given example as a unit test and add unit tests for an empty list, a list of length 1, and a list of length 5.

3. Write a function called *multiple_filter*. This function takes two inputs: a list of integers and a single integer. It returns a list containing all the multiples of the single integer input found in the list input. For example, if the given list is [3,4,5,6,7,8,9] and the given number is 3, then the returned list is [3,6,9]. Here's the catch: you cannot use append or + for lists. Instead you'll implement an algorithm that uses multiple_map and prefix_sum in very particular ways:
   * the value at index i of the original list is in the result if and only if the result of a multiple_map of the original list has a 1 at index i.  
   * if the value at index i of the original list is in the result, then it's location in the result is the value found at location i in the prefix_sum of the multiple_map of the original list
   * the size of the result is one more than maximum value in the  prefix_sum of the multiple_map of the original list
Why and how this works is not at all obvious. Before you try to write this algorithm in python you should take our running example and convince yourself this works by tracing out the above logic. Figure out the result of *multiple_map([3,4,5,6,7,8,9],3)*. Then take that result and figure out it's prefix_sum. Now, take those two lists and figure out how the points above are applied to them in order to get you [3,6,9], the desired outcome of *multiple_filter([3,4,5,6,7,8,9],3)*. Do a similar trace of the program logic using other lists of similar or even smaller size is recommended by not required. Mix of the number and locations of multiples in your list. Write the given example as a unit test and add unit tests for an empty list, a list of length 1, and a list of length 5.

4. Determine the Big-O running time of *multiple_filter* as implemented above. Justify your answer.  Is this better or worse than what you'd see using list appends (or + for lists) and an iterate-and-accumulate strategy?

5. (Optional) Take a crack at C-3.53

6. (Optional) The function prefix_sum, multiple_map, and multiple_filter can all be done using comprehensions along with the occasional list slice and conditional expression (see 1.9.1). While they're clearly shorter in terms of lines of code, it's not clear that they are more efficient in terms of computation time. See if you can work out the comprehension and decide what must be true for the comprehension to be more efficient in terms of their Big-O running time.  
