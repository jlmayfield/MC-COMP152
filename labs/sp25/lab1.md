---
layout: page
title: COMP151 - Lab 1 & Homework 1
permalink: /teaching/COMP152/sp25/labs/lab1
---

[Github Classroom Assignment](https://classroom.github.com/a/corI2gbO)

The goal today is to get back into programming with python and to get some code that can be used as objects of study.  Don't worry about being rusty. Just take stock of where you're at, ask questions, ask for help, and take note of any gaps in you skill set that might need attention. We'll get this started in lab, continue a bit in class, and then you'll wrap it up as homework. 

# Setup 

For this lab (and all future labs and projects) you need:
* a python development environment ([python](https://www.python.org/downloads/) + [vs-code](https://code.visualstudio.com/))
* the [pytest module](https://docs.pytest.org/en/stable/getting-started.html)
* [git](https://git-scm.com/downloads) version control 
* a [github](https://github.com/) account

It is assumed that you have all of this from COMP151 and prior COMP courses. If you don't, or if you need help getting things setup, then please ask for help. You'll know you're ready to go if you got this lab from github classroom and can run `lab1.py`.


# The Problems 

Below are two sets of problems. The first are straight forward. The second are a bit more interesting and will prove to be more interesting objects of study.  You need to write functions and pytest unit tests for all of them. *Use basic python.* Stay away from modules other than `typing` and `pytest`.  When in doubt, ask if you can use something. We'll play with python's toys eventually, but we also want to be able to code from *first principles*. 

## Tier 1

Solutions to these problems follow from iterate and accumulate. 
1. Compute the product of all the numbers in a list.
2. Compute the product of all the numbers in a list that are not multiples of 3. 
3. Transform (in-place) a list of strings to a list of *first-letter...last-letter* or *only-letter*.  For example, *apple* becomes *a...e* and *a* becomes *a*. 
4. Like above but produce a new list, don't modify the given list.  
5. Given a list of strings, compute a new list containing all the odd length strings from that list. 
6. Compute a function that returns true or false if a list of strings contains a string that begins and ends with the same letter/symbol.

## Tier 2

These problems can be solved with the iterate and accumulate strategy, but they are not as formulaic and the resultant solution is not necessarily "the best".  
1. *Prefix sum*: Given a list of numbers, compute a new list where location *i* in the computed list is the sum of everything from 0 to *i* in the given list. 
2. Compute true or false if a given list of numbers contains any duplicates. 
3. Compute true or false if a string is a palindrome. 
4. Compute a list of numbers that is the reverse of a given list of numbers. 
5. Repeat the above reverse problem but do it in-place. 

