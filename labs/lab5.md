---
layout: page
title: COMP151 - Lab 5
permalink: /teaching/COMP152/labs/lab5
mathjax: true
---

This lab is a pen and paper lab. Turn in a copy of your group's work before
you leave lab.

## Part 1: Code Analysis - Single Loops

Your first set of problems involve the analysis of a function that utilizes a single loop. They're very similar
to what we've seen in class so far. Take some time to study them both for their
runtime but also to see what they do and how they do it.

1. Do **R-3.23**
2. Do **R-3.24**
3. Do **R-3.26**

## Part 2: Code Analysis - Nested Loops

We now turn our attention to *nested loops*. These are loops within loops. Our
main focus is a pair of book problems from the same set of problem we did above.
These problems involve the use of *dependent loops*. This is when the number of
repetitions of the inner loop is determined by the outer loop. You can see this
in *example3* from Code Fragment 3.10 in the text (page 143). Notice that the inner
loop (line 22) goes from 1 to $j$ and the value of $j$ is determined by the outer
loop.

Before we dive into that, let's try out an analysis technique with *independent loops*,
where the number of repetitions performed by the inner loop is independent of the
outer loop.

#### Nested Loop Warm-up

Look at the lab 5 replit assignment for this code. After you've pulled it up, read and follow along below.

The function `example2_2` is not designed to solve a problem, instead I've added print statements and other code that help illustrate the overall effect of these loops. Here we see the inner most loop:
```python
for k in range(n):
  print(S[k],end=' ')
  total += 1
```
The print statement is setup to print the item in sequence `S` at location `k` followed by a space. By ending with spaces rather than the default newline, we can see, on a single line, all the prints carried out by one complete execution of this loop. The next line of code  that increments total acts as a count for the number of times this point in the code has been reached. Thus, the final value of total is  equivalent to the number of times the print statement above it executes. As you'll see, it's really a reflection of total work done by the whole nested loop structure.

If we next "zoom out" to the outer loop we see something this:

```python
for j in range(n):
    #INNER LOOP
    print()
```

All that's happening here is a repetition of the inner loop followed by `print()`. The print will act to start a new line of output. When combined with the printing done by the inner loop you will get the desired effect of one line of output for each repetition of the inner loop.

To illustrate the overall effect we can feed this function small sequences. I've chosen to use ranges as they are easy to construct. The example I've given you is:
```python
t = example2_2(range(1,6))
print(t)
```
This will run the function then print the returned total. The range `range(1,6)` gives us the sequence of length 5 : 1, 2, 3, 4, then 5. So, $n=5$. When you hit run you should see that sequence printed 5 times: once for each repetition of the inner loop. We can think of each printed number as an $O(1)$ operation and the final value for total, which is printed after all the number rows, is the total count of these operations. The question we must now ask is, *what is the relationship between that number and the length of the sequence?* Here are some ways to approach this question:

* Re-run the program with sequences of different lengths. Some longer, some shorter, but none "too long". Look for a mathematical pattern. So far we see that a sequence of length 5 carries out 25 prints. This is not the best way to approach the problem but is worth your time because it makes everything very, very concrete. In theory, you could repeat this with a larger number of sizes, graph the results like we did with time, and see what kind of shape you're dealing with.
* A more analytical approach is to setup a table the lets you explore any potential relationship between the inner and outer loops. To do this we can create a row for each value that the outer loop variable $j$ takes on. Next to that value we put the range for the inner loop variable $k$ making note of it's overall size. The range for $j$ is `range(0,n)`, which in our example is the sequence 0 to 4. That means the table for my example would look like this:

| $j$ | $k$'s range | $k$'s range's size |
| :--: | :--: | :--: |
| 0 | range(0,5) |  5 |
| 1  | range(0,5) | 5 |
| 2  | range(0,5)  | 5 |
| 3  | range(0,5)  | 5 |
| 4  | range(0,5)  | 5 |

This table has 5 rows (one for each value in the outer loop range). The size of $k$'s range tells us the number of repetitions performed by each individual occurrence of the inner loop. For example, when $j$ is 3, the inner loop has the range `range(0,5)` and performs 5 repetitions.

If we add up every value in the last column, then we get our familiar total of 25. That's because 5 repetitions of the outer loop means 5 repetitions of the inner loop, each of which carries out 5 repetitions of our print statement. If you repeat the process of making this table for different sized sequences you should notice two things: the number of rows and the size of $k$'s range are both dependent on $n$, the size of the given sequence.

Now we get to the lab problems:

4. Give a big-Oh characterization, in terms of $n$, of the running time of the `example2_2` function.
5. Change `example2_2` so that the range for the inner loop is `range(j+1)` and, if necessary, set the example code back to where it started so that you execute `example2_2(range(1,6))`. This code now executes a *dependent* inner loop. Hit Run. See what happens. Feel free to try a few different ranges by replacing the 6 with another number.
6. Now, for the `range(1,6)` example, create a loop analysis table as described above. Pay extra attention to $k$'s range and it's size. Things will be very different with the dependent loop. Recall that the value of `total`, i.e. the number of times we print, is equal to the sum of the last column on the table. Go read through page 118 and the paragraph at the top of page 119. You should now be ready to *give a big-Oh characterization, in terms of $n$, of the running time of your modified `example2_2` function.*

#### Now that we're warmed up

Warm up done. Let's go back to the book problems. Take a crack the final two problems that stem from Code Fragment 3.10

7. Do **R-3.25**
8. Do **R-3.27**

## Runtime to Real Time

Your last task, time permitting, is to look at how our runtime analysis of operations performed might compare to real computation time.

Imagine you have a computer that can carry out 1 billion operations per second (known as 1 gigaflop). Below we have the analyzed runtime, for 5 imaginary code fragments. If $f(n)$ is the function $n$, then the code takes $n$ operations to complete for an input with size $n$. Our goal is to find the largest $n$ such that the code will complete in *1 hour* for all the running times listed below.

| $f(n)$ | $n$, where $f(n)$ = 1 hour |
| :---: | :--: |
| $\log n$ | |
|  $n$ | |
| $15n$ | |
| $n \log(n) | |
| $n^2$ | |
| $5n^2 | |
| $n^3 | |
| $2^n | |

Hints:
* Start by finding out how many operations can be done in one hour. If your computer does $T$ operations in one hour, then your task is to setup the equation $f(n) = T$ and solve for $n$.
* Remember the inverse of $\log$ is the exponential and the inverse of the exponential is $\log$. So, $10^{\log(n)} = n$ and $\log(10^n)=n$. You'll need this for the log and exponential rows.
* There is no inverse for $n\log(n)$, but we do have that handy solver function from last week. I've included an updated version of it in the lab repl. Use it for that row. 
