---
layout: page
title: COMP151 - Project 1 Prep Lab
permalink: /teaching/COMP152/labs/labp1p
mathjax: true
---

For this lab you'll be cutting your teeth on some *toy problems* designed to get
you familiar with some key mechanics involved in your first project:
1. The Command-line Interface (CLI)
2. File I/O
3. Python Dictionaries

# Task 1: The CLI in Python

Before we get into the task itself, let's do a quick CLI crash course.

#### Quick CLI Crash Course

In replit you have a tab called **Shell** on the right hand side of the screen. We've used it to run unittests.  This tab gives
you access to the command-line for the virtual computer that is running your python
code. The computer is a Linux based machine and the interface is the same as you'd
use on standard Linux machines and on the MAC-OS. You can learn more about that at
[this wonderful site](https://linuxcommand.org/). Windows has a couple of command-line
systems as well as some ways to use the Linux system on top of Windows. Our interest is
not the whole world of the CLI in all its glory. We only want to learn how to develop
Python programs that run at the CLI.

To run a python program from the replit shell you first type python3 followed by the name
of the file containing the program. This will typically look like this:

```Bash
~/Project-1-Prep-Lab$ python3 main.py
```
The `~/Project-1-Prep-Lab$` part of the line is called the prompt.  It is telling
you your current working directory, `~/Project-1-Prep-Lab` followed by a general prompt
symbol `$`.  The main command is `python3`, which launches the python3 interpreter program. the first **argument** to the command is the name of the file containing the program to be executed, `main.py`.  This filename can be anything at all, but in the replit environment we're usually dealing with `main.py`.

Python files like `main.py` can be used in two ways: (1) they are imported in another file using `import` or (2) they are executed as the main program in what's called *top-level code environment*. When you execute `~/Project-1-Prep-Lab$ python3 main.py`, then `main.py` is run in the top-level code environment and as a result the global variable `__name__` is assigned the value of `"__main__"` by the python interpreter. For this reason we typically see the following in a python file meant to be run in top-level environment:

```Python
if __name__ == '__main__':
  # Code here
```
The code you put at `#Code here` is exactly what gets run when you run your program using the CLI. In replit, hitting the *Run* button is more or less equivalent to running `$python3 main.py`.

Sometimes your user needs to pass some starting information to the program. These are called the program's **arguments**. They are effectively the inputs to the program and are given by listing them after the name of the python script file with each argument separated by a space.

This command,
```Bash
~/Project-1-Prep-Lab$ python3 main.py 5 10 -e dog
```
could be translated into something more English like as, "Computer, run the python3 program with the following arguments: main.py, 5, 10, -e, and dog."  Python3 scoops up all 5 of these arguments and packages them *as strings* in a list called **sys.argv**.  The *sys* part of the name refers to the *sys*, or system, pacakage where this is defined in python. The *argv* part of the name comes from the C programming language tradition and stands for *argument values*. To access this list you must import the *sys* package into your program. You can then interact with it like a globally defined list. In the case of our example, we can just imagine that when the program was launched at the shell, the python interpreter injected the following line into our code:
```Python
sys.argv = ['main.py','5', '10', '-e', 'dog']
```

It's important to note that `sys.argv` always contains at least one thing: the name of the file being executed.  Everything above and beyond that is optional and only has an effect on the program execution if the programmer decides to do something with them.

Let's see this in action, in the lab file `main.py` you'll see the following code (plus some other stuff you should ignore right now).
```Python
import sys

def main0():
  print('Hello Main0!')
  for a in sys.argv:
    print(a)

if __name__ == '__main__':
  main0()
```

First things first, notice the design of this program. Rather than tuck a lot of code into the conditional at the bottom, we're defining a zero argument function to act as our "main program function".  The job of the conditional is simply to kick start the program with the main function. This design lets you keep your code tucked away into functional units and helps maintain complexity as the program grows.

Now, **run this code at the shell by doing `python3 main.py`**. You should see `Hello Main0!` followed by `main.py`. The first line comes from the `print` statement on the first line of `main0`. The second line comes from the loop which goes through each item in `sys.argv` and prints it.

Now, **run this code again but add some more arguments**.  Any number of arguments will do. Notice that each of the things your separate by a space is printed on it's own line by the loop in `main0`.

That's really all there is to it. When the user runs the program at the CLI, the arguments are pre-packaged into *sys.argv* as strings for the programmer to do with them what they want.  There in lies the rub. You, the programmer, will need to decide how to interpret these arguments and how to make your program react differently based on different arguments.

## Task 1 - For Real Now

Typically your program will do different things based on the number and/or values passed as arguments. Let's get this working with the simple problems.   First, replace `main0()` in the conditional with `main1()` so that your program executes `main1()`. Now, modify the definition of `main1` so that it does the following:
* If the user passes 3 arguments in addition to the program filename, then print `Friday!`.
* If the user passes 2 arguments in addition to the program filename, then print each of them individually, on one line, but do not use a loop to do the printing.
* If the user passes 1 argument in addition to the program filename and if that argument is a number, then construct a list containing that many occurrences of the given number and print it. For example, if the user passed `5`, then you'd construct `[5, 5, 5, 5, 5]` and print it.
* If none of the above is true, print `Goodbye!`

The second to last case is complicated by the fact that what you presume is a number will be given to you as a string. You'll need to check if the string represents a number, then if it does proceed by converting it.  You have two options for this:
1. Use the string method [isdigit]9https://docs.python.org/3/library/stdtypes.html#str.isdigit) to check the string before converting with `int`.
2. Attempt the conversion within a `try` block and use the corresponding `except` to handle things if the argument is not something that can convert to an integer. Exception handling is covered in section 1.7.

# Task 2: File I/O

We now turn our attention to reading and writing data from a file. The basics of file input and ouput (I/O) are covered in section 1.6.2 of the text but it's very brief. You should also check out the [python tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files). We'll only need the most basic features: read a whole file into a string and write a whole string to a file.

Let's build up our CLI skills and make another CLI program. This one should go in the definition for `main2`. Don't forget to swap `main1()` in the conditional for `main2()`. Your program should do the following:

* If the user passes two arguments in addition to the program filename and if the first one is `-r` then the the second argument is interpreted as the name of a file. That file should be opened and read to a string. The string should be [split](https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split) into words by splitting on whitespace. Finally, print the word count of the file by printing the length of the list that results from splitting the string. I've given you the complete text of *Alice's Adventures in Wonderland* in the file, `aaiw-lc.txt`. Running `$python3 main.py -r aaiw-lc.txt` should print 29594.
* If the user passes two arguments in addition to the program filename and if the first one is `-2` then the the second argument is interpreted as the name of a file. That file should be opened for writing. You should write the uppercase alphabet to that file. That alphabet can be quickly accessed by using `string.ascii_uppercase`. The program prints nothing. You should, however see a new file created when you run it. Running `python3 main.py -w upper.txt` should create a file named `upper.txt` with the alphabet in it. If you've already created that file, then running that command again will just replace that file with a duplicate file. No new files would be created.
* Any other argument combination should cause the program to print `Goodbye!`

# Task 3 - Dictionary as Code book.

Your last task will give you some practice using the python Dictionary class. There is some brief discussion of these in the book but you'll want to refer to the [official tutorial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) for more help and examples.

For your project you'll be substituting individual letters in a secret message in order to uncover that message. This is called a *cipher*. Another way to create secret messages is with a *code*. These messages work by replacing full words with other words. Not every word need be replaced. For example, "The crow flies at midnight", could mean "The suspect gets home at midnight" if "crow" is a code word for "suspect" and "flies" is a code word for "gets home".

In the file `secret.txt` you'll find an encoded message.  In the file `codebook.txt` you'll find the code words for that message. Each line of the file is the code word followed by what should replace it in the actual message. Let's use some file I/O again, but we can skip the CLI. Your task is to complete a definition for `main3` such that it does the following:

* Open the secret message from the file `secret.txt`, read it to a string, and split it up into words by splitting on whitespace.
* Build a dictionary listed in `codebook.txt` by hand, i.e. code it out explicitly rather than try to convert the file into a dictionary. The code words should be the keys of the dictionary and the rest of the line that starts with the codeword should be the value associated with that key.
* Decode the secret message using the codebook and write the result to a file named `revealed.txt`.

The example code for dictionaries given in the python tutorial has everything you need in terms of the dictionary. The first command shows you how to construct a dictionary from known keys and values. The fourth command shows you how to access a value using a key. The last two lines show you how to check to see if a key is in the dictionary.

The last thing I want to draw your attention to here is the construction of the decoded message. The string split function should give you a list of words. The right approach here is to replace any code word with it's associated decoded word. After that you just need to recombine each word into a message and place a space between each word. The right way to do this is to use the `join` method as discussed in section 5.4.2 of the text.  **Do not use the += or + operators**. The result is an $O(n^2)$ process ($n$ being the length of the final string). Using `join` achieves the same result in $O(n)$ time. This is an important Python programming idiom and one you should start adopting into your programming in string-heavy applications.
