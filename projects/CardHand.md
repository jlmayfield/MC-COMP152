---
layout: page
title: COMP151 - Project 1 - Card Hand ADT
permalink: /teaching/COMP152/projects/cardhand
mathjax: true
---

For your first project you'll be implementing project P-7.47 from the text.  This project asks you to implement an abstract data type called a *CardHand*.  Such an ADT could be used as the basis for a number of classic card games. 

# The Problem 

Let's begin with a modification of the project description as seen in the book:
> Implement at *CardHand* class and a *Card* that supports a person arranging a group of cards in his or her hand. The *Card* class represents a single card by it's' *rank* (2-10,K,Q,J,A) and *suit* (Hearts, Diamonds, Clubs, Spades). The *CardHand* class should represent the sequence of cards using a single positional list ADT so that cards of the same suit are kept together. Implement this by means of four "fingers" into the hand, one for each of the suits so that adding a new card to the person's hand or playing a correct card from the hand can be done in constant time. 
> The *Card* class should support the following methods: 
> * `__eq__` and `__ne__` for card comparison   
> * `__str__` and `__repr__` for human readable printing
> The *CardHand* class should support the following methods:
> * `add_card(c)` - Add a new card `c` to the hand
> * `play(s)` - Remove and return a card of suit *s* from the player's hand 
> * `__iter__()` - Iterate through all cards currently in the hand
> * `all_of_suit(s)` - Iterate through all cards of suit *s* that are currently in the hand 

For the most part, all we've added is the *Card* class. This adds a layer for abstraction and gives you practice building and working with simple classes and object. 

# The Project 

You'll work on this project during the next couple of lab periods as well as outside of class. *Proceed through the work in the following order*.

1. (**Lab 1**) `tests.py` Finish *Card* unit tests and write unit tests for *CardHand*. 
2. (**Lab 1**) `usercode.py` Code up the use-case given below, come up with another use-case or two for *CardHand*, and write user-side code for *Card* and *CardHand* class that capture your use-cases.  
3. (**Lab 1 and Homework**) `CardHand.py` Implement and test *Card* class. 
4. (**Lab 2 and Homework**) `CardHand.py` Implement and test *CardHand* class
    a. Implement and test *add_card* and **__iter__**. 
    b. Implement and test *play*
    c. Implement and test *all_of_suit*

## Unit Testing and `unittest` 

Thus far we've been taking a DIY approach to testing. For this project we'll explore a standard development practice for testing code called *Unit Testing* and we'll use a python module called [unittest](https://docs.python.org/3/library/unittest.html) that supports this kind of testing. 

Unit testing works more or less in the same fashion as the tests you've already been writing. You write small tests for each little piece of your code, i.e. for each unit of code. These tests should achieve full **coverage** of your code, meaning the sum total of your tests should run every line of code you've written. Tests typically come in the form of equality assertions: *"I expect this expression to produce this value"* or *"I expect this variable to have this value"*. Unit testing modules like `unittest` let you focus on developing and writing the tests and provide you with detailed reports while managing some of the tedious bits associated with good tests.  The hard work should be coming up with good, meaningful tests, not reading and sorting through output to determine which tests pass and which failed. A good unit testing module makes this possible.  


## Use-Cases and and User-Level Testing

One problem with unit testing is that it takes a more bottom-up approach and you risk losing site of the forest for the trees. That is to say, your focus on the small units that make up program doesn't necessarily test how things will come together in a larger system. To remedy this we can write can develop code to follow what we expect to be real-world **use-cases**.  

A use-case is a short narrative story that describes a situation where your code will be used.  In the case of *Card* and *CardHand* we're talking about a series of actions typical of card game. We'll focus on short stories (i.e. dealing out a hand, playing a few cards, etc.) rather than full-length stories (like the back and forth of a full hand or game of poker).  Here's an example:

> Bob is dealt 5 cards: the Ace of Hearts, the Jack of Clubs, the 3 of Diamonds, the 2 of Hearts, and the 5 of Clubs.  Scanning his hearts, he sees two cards, the Ace and 2.  He decides to play one heart (doesn't really matter which), and that leaves him with a single heart. His full hand now contains one heart (whichever is left), the Jack and 5 of clubs, and the 3 of Diamonds. 

I can now write code the corresponds to Bob's experience:
1. Build Bob's hand as described.
2. Iterate through the hand to see/print all the cards. 
3. Use `all_of_suit` iterate through and see the hearts.
4. Play a heart.
5. Use `all_of_suit` to see the hearts and notice there's one fewer.
6. Iterate through the hand to see/print the remaining four cards. 

Notice this story uses all of the *CardHand* methods. It doesn't cover all the different logical cases (actions with suits other than hearts, handling situation with not cards of a desired suit, etc.) but it's concrete, comes from an expected use case, and it lets us see how the different *Card* and *CardHand* methods will work together. Where unit tests let us know that the individual pieces work, a good use-case test lets us see that those pieces are usable in practice. Doing both forms of testing before fulling implementing complex ADTs or functions can save time on building code pieces (classes, methods, functions, etc.) that are difficult to use or that cannot even be used in the way we need them. 


## Iterators, Generators, and `__iter__` 

The text covers this topic in **Chapter 1, Section 8**. Be sure to read it as well as the description below. 

The `__iter__` and `all_of_suit` methods are meant to enable you to loop through a hand of cards or a suit within a hand using the python `for` loop.  For example, you'll quickly want to print out the cards in a hand and prior experience in Python says code to do that should look like this: 
```python
import CardHand as ch

myhand = ch.CardHand()
# code to add/remove cards from myhand
for c in myhand:
    print(c)
```

Or maybe you want to look at all the hearts in a hand. Assuming the string `"H"` is used to represent the heart suit, we could do: 

```python

for c in myhand.all_of_suit("H"):
    print(c)

```

For this to work, a *CardHand* should be able to function like a range or a list and `all_of_suit` should behave similarly but constrained to one suit. 

In programming, we call objects that manage and enable iteration an **iterator**.  The simplest way to build such an object in Python is to create a **generator**. For ADTs that contain collections of sequences of data, we can implement the `__iter__` method and enable for loops that iterate over the entire collection like the first example above. You can see an example of this in `positional_list.py`. The `all_of_suit` method would work the same way, but simply constrain the generation to a subset of the collection. 

The operation that enables generators in python is `yield`.  You can think of this as a *return, save, and pause*.  It will return the yielded value, save the current state of the function, and pause operation. The next time a value is requested within a loop (or some other iterative context), the function will resume and yield again. Section 1.8 of the text gives some great simple examples of functions that would produce a list of values along side their generator equivalents. Between these and the positional list example, you should have a good place to start with *CardHand*'s `__iter__` and `all_of_suit` methods. 