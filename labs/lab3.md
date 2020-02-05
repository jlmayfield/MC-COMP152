---
layout: page
title: COMP151 - Lab 3
permalink: /teaching/COMP152/labs/lab3
---

For this lab you'll begin to construct a python class to represent a runner's result for a half marathon race and then use Python's [unit tests](https://docs.python.org/3.7/library/unittest.html) to formally test the methods and functions you implement.

### A Runner

The class you'll define is called *Runner*. An instance of this class represents an individual's result's for a half marathon race (that's 13.1 miles or just a hair over 21km). Race results are often posted on websites and can be downloaded and analyzed by anyone. A class like *Runner* would be useful in this context.  If you want a real world example of this kind of data you can checkout sites like [itsracetime.com](itsracetime.com). I ran a half marathon last year and used that exact site to get data about my race and [do some analysis of my results and the race overall results](/blog/2019/04/LPHM).  

Individual racer's results include biographical data, time data, and rank data. Runners get grouped by their age and sex and ranks are recorded for their group as well as the overall field of runners. In additional to final time, races typically record and report splits, or times at specific points in the race.  Your class needs support fields for name, home town, age, sex, group place, overall place, final time, and split times. The table belows lists field names (minus the leading underscore), types, and an concrete examples of field data based off the race I did last year.  

| Field Name | | Type of Field | | Example |
| :--- | | :---- | |:---- |
| name | | string | |'Logan Mayfield' |
| home | |tuple | |('Monmouth','IL') |
| age  | | int | | 38 |
| sex  | |string | |'M' |
| place_group | |int | | 25 |
| place_overall | |int | | 183 |
| final_time | |tuple | |(1,50,59) |
| splits | |dictionary | | {'5k':(0,25,15),'10k':(0,51,22),'15k':(1,23,43)} |

#### And you're off!

You've been given a head start on this code. Go copy and take a look at [this repl](https://repl.it/@loganmayfield/lab-3-starter-code). In it you will see the beginnings of key definitions as well as some tests.  You'll notice that the method definitions are not complete but either use *pass* (a python command for "do nothing") or return a value that is at least the right type of result for the method. These are examples of **stubs**.  They let you setup definitions and tests before the coding begins.

0. Look [here](https://docs.python.org/3.7/library/unittest.html#unittest.main) and figure out how to run select tests rather than run them all as it does right now.
1. Invent another example of a racer and add another Runner object to the setUp method to represent that individual. This gives you two Runners to use in tests.
2. Complete the constructor (aka init) by replacing *pass* with the actual initialization code. Don't worry about type checking inputs and throwing exceptions. Assume the user is passing valid, well-structured initial values like you see in the tests.
3. In the string tests, add a test for your runner along side the existing test for jlm. Complete the str method and verify your code by seeing that the tests you have written now pass.
4. Write tests for == and !=, implement those methods, and verify your code by seeing that your tests pass.
5. Write a getGroup test for your racer alongside the existing test for jlm. Complete the getGroup method and verify your implementation by seeing that your tests pass.
6. Racers usually get grouped by age. My age group was 35-39. Add a method called *ageGroup* to the Runner class. It takes a range and returns a boolean that indicates if the runner's age is in that range. Start by writing a stub for the method. Next write tests, then finally complete the method and verify your work against your tests.
7. Write tests for the splitUnder method. Complete the splitUnder method and verify your implementation by seeing that your tests pass.
8. Write another set of tests for the average pace method that use your racer. You know the drill now: code and test.

#### Next Steps

This part is optional but if you have time you should work on it as it will really get you ready for things to come while testing your understanding of material from both chapter 1 and 2.

9. Write a function called *countAgeRange* that counts the number of Runners from a list of Runners that fall within a given age range. This function is not part of the Runner class. Definite it at the same indentation level as Runner. Approach it the same way as the class methods. First write a stub, then write tests, then tackle the code. 
