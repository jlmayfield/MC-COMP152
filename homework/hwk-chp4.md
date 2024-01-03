---
layout: page
title: COMP151 - Homework 4 - No-Slice Recursion
permalink: /teaching/COMP151/homework/homework4
mathjax: true
---

In lab we practiced designing and implementing basic recursive functions. In class we learned that while Python slices make a lot of these functions easier to implement, they come at a cost. For homework we'll explore was to remove this cost and other techniques for optimizing recursive functions.

### From Sequence Slices to Index Ranges

A basic recursive function has a structure similar to what we see below.

```Python
def foo(S):
  if len(S) == 0:
    return ...
  else:
    ... S[0] ... foo(S[1:]) ...
    return ...
```

The general idea is to incrementally peel away the first item in the sequence, `S[0]`, while recursing on the rest of the sequence, `S[1:]`. This continues until we've sliced the sequence down to nothing, `len(S) == 0 `. The problem is that slicing adds $O(n^2)$ overhead because of the repeated copying of each slice.

To get rid of the overhead we need to leave the sequence `S` intact but retain the spirit of the recursion. To accomplish this we do something a bit paradoxical. We re-imagine our problem as something more general. Let's turn to a concrete example. In class we came up with the following recursive function for finding palindrome strings.

```Python
def ispalindrome(S):
  """ Determine if string S is a palindrome """
  if len(S) <= 1:
    return True
  else:
    if S[0] != S[-1]:
      return False
    else:
      return ispalindrome(S[1:-1])
```

The problem we're solving here is framed in terms of an entire string: "Is the string S a palindrome?". To generalize the problem we can instead ask: "Is a particular region of a string a palindrome?". For this we might use the following signature:

```Python
def ispalindrome(S,start,stop):
  """
  Determine if S[start:stop] is a palindrome or not

  S    a string
  start  number index where the checked region starts
  stop   number index right after the end of the checked region.
  Return  True if S[start:stop] is a palindrome, False otherwise

  ...
```

How is this a generalization of `ispalindrome(S)`?  If you were to make the function call `ispalindrome(S,0,len(S))` then you'd be doing the same thing as the original `ispalindrome(S)`, check to see if all of `S` is a palindrome. Put another way, the action of `ispalindrome(S)` is a specific instance of `ispalindrome(S,start,stop)`.

This generalized signature for `ispalindrome` lets us avoid slicing by changing the range instead of slicing the string. In the original `ispalindrome` our recursive call was `ispalindrome(S[1:-1])`. This recursive call worked with everything but first and last letter of `S`.  We can get the same effect by incrementing and decrementing `start` and `stop` and making the following recursive call `ispalindrome(S,start+1,stop-1)`. No slice needed.

We now turn our attention to the rest of `ispalindrome`. The original function worked with the first and last letter of `S`, or `S[0]` and `S[-1]` respectively. In our general problem we want the first and last of the region bounded by `start` and `stop`. That would be `S[start]` and `S[stop-1]` respectively.  Finally, the non-recursive case occurred when the string was empty or contained a single letter, i.e. `len(S) <= 1`. Now that we are not actively slicing the string, this will never happen. We need to instead check to see if the region is empty or contains just one item. In general, the region between `start` and `stop` has `stop-start+1` numbers in it. So, we can check if `(stop-start+1) <= 1`. Alternatively, we can observe that when `start >= stop`, then the region is empty. So a region of 1 or fewer items occurs when `start >= (stop +1)`.  Let's put this all together and finish `ispalindrome(S,start,stop)`.

```Python
def ispalindrome(S,start,stop):
  """
  Determine if S[start:stop] is a palindrome or not

  S    a string
  start  number index where the checked region starts
  stop   number index right after the end of the checked region.
  Return  True if S[start:stop] is a palindrome, False otherwise
  """
  if (stop-start+1) <= 1:
    return True
  elif S[start] != S[stop-1]:
    return False
  else:
    return ispalindrome(S,start+1,stop-1)
```

If we still want to be able to check whole strings by making function calls like `ispalindrome('racecar')` that skip specifying values for `start` and `stop`, then we can use default values for our function arguments (see pages 26 in the text). In this design, the default value for `start` would be 0. For `stop` we'd want the length of `S` to be the default. Unfortunately we need to do a bit of dance to accomplish this as we can only use literal values for defaults, not values determined at runtime. The trick here is to give `stop` a default of `None` and then use a condition to set it to `len(S)` when `stop` is `None`. The end result looks like this:

```Python
def ispalindrome(S,start=0,stop=None):
  """
  Determine if S[start:stop] is a palindrome or not

  S    a string
  start  number index where the checked region starts
  stop   number index right after the end of the checked region.
  Return  True if S[start:stop] is a palindrome, False otherwise
  """
  if stop == None:
    stop = len(S)
  if (stop-start+1) <= 1:
    return True
  elif S[start] != S[stop-1]:
    return False
  else:
    return ispalindrome(S,start+1,stop-1)
```

With default values set for `start` and `stop`, we can now use keyword arguments (see page 27 in the text) whenever we want to check regions use just one of the defaults. For example, `ispalindrome(S,stop=10)` would check `S[0:10]` to see if it's a palindrome and `ispalindrome(S,start=5)` would check `S[5:]`.

# To Do

1. Re-visit all the book problems from lab 6 *(C-4.9, C-4.16, C-4.18, and C-4.20)* and redo them in the no-slice style described above. Include default parameters. Place your definitions in `main.py`. Solutions to the problems using slice-based recursion are available on replit if you need or want to consult with them. **For each of the functions, write unittests in `test.py`.**
