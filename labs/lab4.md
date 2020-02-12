---
layout: page
title: COMP151 - Lab 4
permalink: /teaching/COMP152/labs/lab4
---

We'll begin our foray into algorithm analysis by doing some analysis of the concrete instantiation of algorithms: code.

### The Code

On page 143 of the text is code fragment 3.10. It contains five python function definitions. These are our objects of study.

1. Work with your partner to copy this code into a repl. You can absolutely work with your partner(s) to get this done quickly; don't worry about the driver/navigator paradigm. Get it copied over, run it, test it, get familiar with what each function accomplish. Towards this end *write several concrete tests for each function using the unittest library*. Be certain you can trace the execution of the code for small inputs.

### The analysis

Record your answers to the following with good old fashioned paper and pencil. For each function listed in fragment 3.10:
2. Choose a small (size 3-5 probably) input and count how many basic python operations are needed to complete the function for that input. Be sure to indicate the exact input used to generate your count.  Briefly indicate which parts of the code you did not count, what is *not* an operation and what things we get for free (the goal is to make clear what is and is not counted).
3. Characterize the worst-case and best-cast input. Offer concrete examples of these case for an input of size 10.
4. Write a *work* function, in mathematical notation not code, for each python function. This function takes as its input the size of the input (*n*) and computes the total number of operations for the *worst case* input of that size. Which of the seven functions listed in chapter three best classifies each of your functions? 
