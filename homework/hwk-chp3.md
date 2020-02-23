---
layout: page
title: COMP151 - Homework 3
permalink: /teaching/COMP151/homework/homework3
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<h3 align="center">
 Due in-class on 2/28
</h3>

1. Do problems R-3.2, R-3.3, R-3.8, and R-3.29 through R-3.33 from the text. Be sure to justify your answer.
2. Answer the following:
  1. How many times do you need to divide 482 by 2 to get a value less than 1?
  2. How many times do you need to divide 379 by 2 to get a value less than 1?
  3. If starting at 1, how many times would you need to double up to get to a value that is bigger than 1011?
  4. If starting at 1, how many times would you need to double up to get to a value that is bigger than 92?
  5. Fill in the following table (don't use a calculator):
  | $n$ | $\lfloor \log_2{n} \rfloor$ | $\lceil \log_2{n} \rceil$ |
  | :--- | :---- | :--- |
  | 25 | | |
  | 195 | | |
  | 15300 | | |
  | 95127 | | |
3. What is the time complex of the following code fragments? For each fragment the variable *alist* is list data.  
  1.
  ```python
  for el in alist:
     ...
  ```
  2.
  ```python
  for i in range(len(alist)):
     el = alist[i]
     ...
  ```
  3.
  ```python
  for i in range(0,len(alist)):
     for j in range(i,len(alist)):
       ...
  ```
