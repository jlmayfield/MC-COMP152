---
layout: page
title: COMP151 - Project 1 - Monoalphabetic Substitution Ciphers
permalink: /teaching/COMP152/projectst/monocipher
mathjax: true
---

For this project you'll be developing a Command-Line Interface (CLI) program that
carries out several basic, pre-computer era cryptography tasks. Our high-level learning goal
is to carry out this project using lots of python's built-in functionality, namely
things like *dictionaries*, *comprehensions*, and *sequence slices*. By doing so, we can experience
the end product of the study of data structures and algorithms: efficient, easy-to-use
programming tools.

The remainder of this webpage includes important dates for the project, a brief
introduction to the type of cryptography we'll be exploring with our project, and,
of course, the project requirements and grading rubric. Refer back to this page often and do not
hesitate to ask for clarification on project requirements or on our cryptographic system.

# Important Dates

The project spans roughly two weeks and will utilize two lab periods. *Plan to put
in a fair amount of time into this project outside of lab.*

| <u>Date</u> | <u>Event</u> |
| :---: | :---: |
|  Tues. 3/22 | Project Lab Assignment Due (see section *Project Lab Assignment*) |
|  Tues. 3/29 | Open Work Time in Lab |
|  Mon. 4/4  | **PROJECT DUE by 8am** |


# Monoalphabetic Substitution Cipher Systems

All cryptographic systems work by transforming a message, called the *plaintext*, into an obscured, or *encrypted* message called the *ciphertext*.  This transformation is carried out using a program-like method that either *substitutes* parts of the *plaintext* for something else or that rearranges, or *transposes*, the order of some or all of the *plaintext*.  The encryption method uses a secret *key* to determine what parts of the plaintext get substituted or moved and how those substitutions and transpositions should be carried out. If you know the key, then carrying out and reversing the encryption is easy. Without the key, undoing the encryption is, or at least should be, hard or near impossible.

Our cryptographic system of choice is called a *monoalphabetic, uniliteral substitution cipher*.  It is based purely on substitution and works by replacing individual letters in the plaintext with a different letter, hence the *uniliteral substitution* part of the name. The correspondence between plaintext letters and ciphertext letters can be described by a single arrangement, or *permutation* of the 26 letters of the alphabet, hence the *monoalphabetic* part of the name. This alphabetic sequence acts as the system's key.

What follows is a bare-bones introduction to monoalphabetic, uniliteral substitution and cryptography more generally. It's only meant to get you through this project. You can read a lot more about these systems, similar systems, and how to break these systems without knowing the key in some now classic documents on pre-computer era cryptographic systems. The
[Army Cryptanalysis Field Manual on Basic Cryptanalysis](https://www.globalsecurity.org/intell/library/policy/army/fm/34-40-2/index.html) is a quick and to the point discussion of cryptographic systems and how to break them. [William Friedman's Cryptography Book](https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/friedman-documents/publications/FOLDER_238/41748889078809.pdf) focuses on encrypting and decrypting more than it does breaking them. [Friedman](https://en.wikipedia.org/wiki/William_F._Friedman) and his wife [Elizabeth](https://en.wikipedia.org/wiki/Elizebeth_Smith_Friedman) are significant figures in the history of modern cryptography. I highly recommend the book about Elizabeth's life and  cryptographic exploits titled *[The Woman Who Smashed Codes](https://www.amazon.com/Woman-Who-Smashed-Codes-Outwitted/dp/0062430483)* by Jason Fagone.


## Keys and Key Generation

The key to understanding a cryptographic system is understanding the system's key. For our system of choice, a key is a one to one association between letters in the plaintext document and letters in the ciphertext document. To avoid confusion, we write plaintext letters in lowercase and ciphertext letters in uppercase. Here we see a key that we'll use to carry out an example encryption later.

```
plain:  abcdefghijklmnopqrstuvwxyz
cipher: GFDBATCEJORPZYXWVUSQNMLKIH
```

This key is what we'll call the *encryption key*. The letters are listed in alphabetical order according to the plaintext sequence. Encryption keys are meant to aid encryption. They let you easily find a ciphertext letter for a given plaintext equivalent. The *decryption* key is just what you get when you rearrange this key such that the ciphertext sequence is in order. It aid decryption in the same way the encryption key aids decryption.

```
cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain: edgchbazyixwvujltksfrqponm
```

From a security standpoint, the ideal key is a randomly ordered alphabetical sequence, also known as a *random permutation*.  Such a sequence is easy enough to work with for computers, but hard for humans. A human-powered cryptographic system would instead employ an easy to remember process for generating a cipher sequence starting from the standard, ordered alphabetical sequence. This leads to a basic key generation process:

1. Start with ABCDEFGHIJKLMNOPQRSTUVWXYZ
2. Rearrange the letters of (1) based on simple rules.
3. Align the result of (2) with abcdefghijklmnopqrstuvwxyz to get an encryption key

We'll look at three common techniques for carrying out step two of this process. These techniques are typically combined in order to add a bit more randomness to the process.

### Key Sequence Transformation: Reversal, Shifting, and Keywords

The easiest key sequence generation technique to use and understand is to reverse the sequence. This results in the the following key. From here on we'll forgo labeling plain and cipher sequences as it should be clear which is which based on the letter case.
```
abcdefghijklmnopqrstuvwxyz
ZYXWVUTSRQPONMLKJIHGFEDCBA
```
The limits of this are pretty clear and the security it affords is pretty low. To spice things up a bit more there is another simple, and classic (it's literally a *classic*. it comes from [Julius Caesar](https://en.wikipedia.org/wiki/Caesar_cipher#History_and_usage)) technique: shifting. A shift is carried out by effectively moving letters around as if they were on a circular track and thereby changing their position in the sequence. A positive shift indicates moving letters to the right where a negative shift moves them left. For example, here you see two keys. The first generated by shifting the standard sequence 5 and the second by shifting it -7.

```
(shift 5)
abcdefghijklmnopqrstuvwxyz
VWXYZABCDEFGHIJKLMNOPQRSTU

(shift -7)
abcdefghijklmnopqrstuvwxyz
HIJKLMNOPQRSTUVWXYZABCDEFG
```

Shifting suffers one of the same key weaknesses of reversing and doesn't afford much more security. You can at least generate several different keys by shifting different amounts where reversal alone only allows for a single possible key.

Our final key generation technique gives us a clever way to mix up the sequence and reorder at least some of the letters. We start by picking a keyword. From this keyword you generate a sequence using  the following process:

1. remove all duplicate letters from the keyword
2. remove all the letters in the modified keyword from the standard sequence.
2. Construct a sequence by appending (2) to (1).

Let's look at an example. Say your keyword is *WENDNESDAY*, then the sequence corresponding to this keyword is *WEDNSAYBCFGHIJKLMOPQRTUVXZ*. We get *WEDNSAY* from step 1 and *BCFGHIJKLMOPQRTUVXZ* from step two. This leads to the following encryption key.

```
abcdefghijklmnopqrstuvwxyz
WEDNSAYBCFGHIJKLMOPQRTUVXZ
```

Keywords and shift amounts are easier to remember than random permutations of 26 letters. By combining these key generation techniques and, if possible, developing a system where new keys are generated for different messages, then users of this cryptographic system can strike a balance between security and ease of use.

## Encryption and Decryption

Encryption and decryption are relatively straight forward. Most of the work is
substituting the letters based on the encryption or decryption key. To improve security a tiny bit and to stave off human error, there are some document preparation steps that we'll do as well. Let's dive right into a full, "real world", example that goes from plaintext, to key generation, to ciphertext, and back again to plaintext.

### A Fully Worked Example:

Alice want to secretly transmit the following message to her friend Bob so that their shared enemy Eve cannot read it.
```
This project should be a lot of fun. It's worth ten percent of your final grade.
You have two weeks to do it. Lab time is not enough to get it done.
Do not over-procrastinate. Please.
```
Alice and Bob have previously agreed on a key generation scheme such that this message should use the following key generation process: start from a keyword sequence that uses the keyword *project*, then shift -12, and then reverse. From this they get the following keys. The steps of key generation are shown as well.
```
keyword: project
sequence:  PROJECTABDFGHIKLMNQSUVWXYZ
shift -12: HIKLMNQSUVWXYZPROJECTABDFG
reverse:   GFDBATCEJORPZYXWVUSQNMLKIH

Encryption Key:
abcdefghijklmnopqrstuvwxyz
GFDBATCEJORPZYXWVUSQNMLKIH

Decryption Key:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
edgchbazyixwvujltksfrqponm
```

Prior to encryption, Alice strips the message of anything that's not a letter and converts all letters
to lower case. From this string she can more easily use the encryption key to carry out the necessary substitutions. This results in the following prepared plaintext and its subsequent ciphertext:
```
thisprojectshouldbealotoffunitsworthtenpercentofyour
finalgradeyouhavetwoweekstodoitlabtimeisnotenoughtoget
itdonedonotoverprocrastinateplease

QEJSWUXOADQSEXNPBFAGPXQXTTNYJQSLXUQEQAYWAUDAYQXTIXNUT
JYGPCUGBAIXNEGMAQLXLAARSQXBXJQPGFQJZAJSYXQAYXNCEQXCAQJQ
BXYABXYXQXMAUWUXDUGSQJYGQAWPAGSA

```
Finally, Alice breaks the ciphertext into blocks to hide any
sense of the structure of a human-to-human message. No word boundaries, no obvious sentences nor paragraphs. Just blocks of letters.

```
QEJSW UXOAD QSEXN PBFAG PXQXT
TNYJQ SLXUQ EQAYW AUDAY QXTIX
NUTJY GPCUG BAIXN EGMAQ LXLAA
RSQXB XJQPG FQJZA JSYXQ AYXNC
EQXCA QJQBX YABXY XQXMA UWUXD
UGSQJ YGQAW PAGSA
```
This message is now safely be sent to Bob. Once he receives it,
he can use the decryption key, which he'll generate on his own the same way that Alice did)
they can generate on their own, to decrypt the message. A decryption results in the following plaintext:
```
thisp rojec tshou ldbea lotof
funit swort htenp ercen tofyo
urfin algra deyou havet wowee
kstod oitla btime isnot enoug
htoge titdo nedon otove rproc
rasti natep lease
```
All that's left for Bob to do is to read through that, find the actual words, and retrieve the original message.

## Cryptanalysis via Frequency Analysis

What if Eve intercepts Alice and Bob's ciphertext? She doesn't know the key, but she knows they
use monoalphabetic, uniliteral substitution. Is there anything she can do to decipher their message? Yes! This kind of encryption is incredibly weak. The original message, and potentially all of the key can be reconstructed from the ciphertext alone. The process of analyzing and breaking a cryptographic system like this is called *cryptanlysis*. An
essential task in this process is collecting the frequency of letters and groups of letters  in the ciphertext.

English is not a random language. Certain letters and combinations of letters are used more frequently than others. Human languages have a predictable statistical fingerprint. While working at Google, the computer scientist Peter Norvig repeated a classic statistical analysis of the English
language using the entirety of Google Books. [His report](https://norvig.com/mayzner.html) highlights the statistical fingerprint in English writing. Certain letters, words, and groups of letters appear more often than others. Alice and Bob's cryptographic system is just shifting those statistics to different letters. It doesn't change the statistics and the kind of distributions they produce. All Eve needs to do is follow the frequencies.

Let's look at the results of a single letter frequency count of Alice's ciphertext. Compare this to the single letter frequency of English as reported by Norvig. To make this comparison a bit easier, I've listed the ciphertext letter and its plaintext equivalent below.

```
Total Letters: 140
Unique Letters: 23

Cipher/Plain Frequency
X/o           19
Q/t           18
A/e           17
Y/n           9
J/i           8
U/r           8
G/a           8
S/s           7
E/h           5
N/u           5
P/l           5
B/d           5
W/p           4
T/f           4
D/c           3
L/w           3
C/g           3
F/b           2
I/y           2
M/v           2
O/j           1
R/k           1
Z/m           1
```

After doing a quick letter count, Alice can probably start guessing which letters represent
the top seven letters in English. From here she can start to find words and work out other
parts of the key.  Using double and triple letter frequencies can further help by exposing
common multi-letter patterns.

# Project File Formats

Your cryptographic program will do it's work through files. Plaintext, keys, and ciphertext will be written to or read from a file. The results of frequency analysis will also be written to a file to
aid someone in cryptanalysis. All these files will have very specific formats and because they act as the end points to your project, let's start by describing each file format.  A full set of example files will be provided with the project and displayed below.

## Key Sequence Files

Keys will be saved to a file by writing the ciphertext sequence on a single line. The key used in the worked example above would look like this:

```
GFDBATCEJORPZYXWVUSQNMLKIH
```

## Cipher Text Files

Ciphertext files will conform to the format used in our example above. It contains all uppercase letters, written in blocks of five letters separated by spaces, with five blocks per row. If the total number of letters is not a multiple of twenty-five, then the last row will have fewer than five blocks. If the number of letters is not a multiple of five, then the last block will have fewer than five letters. Alice's ciphertext file would look like this:

```
QEJSW UXOAD QSEXN PBFAG PXQXT
TNYJQ SLXUQ EQAYW AUDAY QXTIX
NUTJY GPCUG BAIXN EGMAQ LXLAA
RSQXB XJQPG FQJZA JSYXQ AYXNC
EQXCA QJQBX YABXY XQXMA UWUXD
UGSQJ YGQAW PAGSA
```

## Plain Text Files

Plaintext files come in two flavors: pre-encryption and post-decryption. If the file has not be encrypted, then it's just a standard English document. This includes punctuation and word spacing. Alice's initial plaintext would look something like this:
```
This project should be a lot of fun. It's worth ten percent of your final grade.
You have two weeks to do it. Lab time is not enough to get it done.
Do not over-procrastinate. Please.
```

If the file plaintext is the result of a decipherment, then the file has the same structure as a cipher text file (five letter blocks, five blocks per row), but letters are lowercase to indicate that it's plain text, not cipher text. The plaintext file that Bob generates from his decryption would look like this:
```
thisp rojec tshou ldbea lotof
funit swort htenp ercen tofyo
urfin algra deyou havet wowee
kstod oitla btime isnot enoug
htoge titdo nedon otove rproc
rasti natep lease
```

## Cryptanalysis Files

The last type of file you'll produce is the result of a frequency analysis. The analysis can be done in terms of a number of letters. We'll refer that that sequence as a *gram*. In the analysis that Eve did, the gram was a single letter. It could also be two letter, three letter, or *n* letter sequences.

The first line of the analysis file has two numbers on it: total number of *grams* and the total number of unique grams seen in the cipher text.  Every other line of the file lists the counts for each gram by first giving the gram, then it's count/frequency. Grams should be listed in most to least frequent order. Eve's single letter frequency report would look like this:
```
140 23
X 19
Q 18
A 17
Y 9
J 8
U 8
G 8
S 7
E 5
N 5
P 5
B 5
W 4
T 4
D 3
L 3
C 3
F 2
I 2
M 2
O 1
R 1
Z 1
```

That means there were 140 letters in the ciphertext and only 23 of the 26 letters in the alphabet
were seen. What follows is the frequency for each of those letters.

# To Do: Labs and Versioning

There's a lot for you to do in this project. To manage the complexity of all that programming,
you'll be breaking the work up in to discrete, bite-sized steps or *versions*. Each version adds to or builds on the prior version. Completing a version results in a complete, executable program that completes some of the programs desired features but not necessarily all of them. They must be done in order. Before launching into the versions proper, you'll do a warm-up lab designed to get you thinking
in terms of functions and to get your brain into the cryptographic head space. Below is a description of and the requirements for each version and the lab assignment.

## Project Lab Assignment - From Key File to Dictionary

Don't forget to use any python built-in functions and in particular, try to make good use of list and dictionary comprehensions when possible. Hint: It is possible to write each of these function without writing any loops.

For this lab you should complete the following four functions. Stubs and tests for these are included with the project on replit

1. Write and test a function named `build_encrypt_key` that takes one string, the name of a file containing a key sequence, and returns a dictionary suitable for encryption where keys are the plaintext letters and the associated values are the ciphertext equivalents.
2. Write and test a function named `to_decrypt_key` that takes a dictionary that represents an encryption key (the output of `build_encrypt_key`) and returns a dictionary suitable for decryption. where keys are the ciphertext letters and the associated values are the plaintext letters. Notice that this can be accomplished by swapping the keys and values of the encryption key dictionary.
3. Write and test a function named `prepareplaintext` that takes a single string, removes anything that is not a letter, and converts all the remaining letters to lowercase. The resultant string is then returned.
4. (Optional) Write and test a function named `blocktext` that takes a string and splits it into a list of 5 character groups. If the string's length is not a multiple of 5, then the last group can and should be the remaining 1 to 4 letters.

## Project Versioning

Develop your project by completing each of these versions in numerical order. Be sure each version is fully functioning and well tested before moving on to the next version. When starting new versions you can and should add or modify the code for the previous version but should not remove or break any of the functionality of the prior program. In the end you are developing one program total, not one program per version.

### Version 0 - Decipher

The first version of your program should be capable of decrypting ciphertext given that text and a key. The resultant plaintext will be written to a file.  To use this program, the use launches the program with the `-d` option, then provides the filenames like the example below.
```Bash
$ python3 monocipher.py -d cipher.txt key.txt plain.txt
```
In general, any file names will do, but the order matters. The names must be listed in ciphertext, key, then plaintext order. It's worth noting that key files are encryption oriented. This is why you wrote the function `to_decrypt_key` as part of the starter lab exercises.

If the user tries to use the program with anything other than the `-d` option, then your program should report some kind of error. Help text is ideal.  You do not need to worry about them passing filenames in the wrong order. If they do that, then you can expect and allow python to crash and generate an exception.  If they give you `-d` as an option but not enough filenames, then you should have your program report an error. Again, help text with the error is ideal.

### Version 1 - Encipher

The next version of your program adds the encryption option `-e`. The command looks the same as the decryption option but the file order is reversed so that the input files (plaintext and key) come before the output file (ciphertext).

```Bash
$ python3 monocipher.py -e plain.txt key.txt cipher.txt
```

All version 0 functionality should still work. A complete version 1 program should be capable of both encryption and decryption. Apply the same kind of CLI error handling to `-e` that you did to `-d`.

### Version 2 - Key Generation

Version 2 adds key generation to your encryption and decryption program. This version enables shifting and reversing only. To generate a key, the user passes the `-k`, followed by the name of the file they'd like the key written to, followed by some shift and reverse options. Users can one shift and one reversal. They do not need to do both. The order they pass the option to the command is the order in which the operations should be performed. Here are a few examples to illustrate all the possibilities.

```Bash
$ python3 monocipher.py -k key.txt -s 4
```
The above command will generate a key by performing a shift to the right by 4 places.

```Bash
$ python3 monocipher.py -k key.txt -r
```
This command does a sequence reversal.

```Bash
$ python3 monocipher.py -k key.txt -s 4 -r
$ python3 monocipher.py -k key.txt -r -s 4
```
The above two command show generations that involve both shifting and reversals. The first example
does a shift before the reversal. The second does the reversal before the shift.

Again, the user is only allowed at most one shift and one reversal. The above four examples cover all the possibilities that your program provide to the user for key generation. Remember, the program should maintain the functionality of all previous versions. At this point, that means encryption (`-e`), decryption (`-d`), and key generation (`-k`).

### Version 2.5 - Expanded Key Generation

You'll now add keyword based sequence generation to the program. Keyword sequence generation can be combined with shifting and reversals, but the keyword sequence generation must come before any shifts or reversals. To generate a keyword sequence, users add the `-kw` option followed by the keyword to the key generation option as seen in the example below.

```Bash
$ python3 monocipher.py -k key.txt -kw Douglas
```

Alice and Bob would have used the following command to generate their key in our worked example:

```Bash
$ python3 monocipher.py -k key.txt -kw project -s -12 -r
```

Upon completion of Version 2.5, your program provides all the tools that Alice and Bob
would need to share secret messages. They can generate keys using keywords, shifts, and reversals. They
can encrypt plaintext using a key, and they can decrypt ciphertext using a key. Your program should do a good job of catching CLI inputs that are completely out of bounds for the above tasks and should also catch commands that use the right options but are perhaps missing some required arguments, i.e. not enough file names or no filename. It need not be perfect, but some good effort should be made to at least catch obvious problems.

### Version 3 - Single Letter Frequency Analysis

Now that our program full supports the needs of Alice and Bob, it's only fair that we
offer up some features to Eve.  This version adds the cryptanalysis option `-a`.  This option
is followed by the name of a ciphertext file and the name of the file in which it should
write the result of a *single letter frequency analysis*. Assuming Alice's ciphertext message
were stored in the file `cipher.txt`, Eve would use the following command to perform her
frequency analysis.

```Bash
$ python3 monocipher.py -a cipher.txt cryptanalysis.txt
```

As always, do not break or remove features from prior versions of the program and make good efforts
to error check the `-a` arguments.

### Version 3.5 - Multi-letter Frequency Analysis

The final version of the program expands the cryptanalysis option to allow the user to specify
the size of the gram by giving a positive integer after the `-a`. The example below would carry out
a two letter frequency analysis of the ciphertext in cipher.txt.

```Bash
$ python3 monocipher.py -a 2 cipher.txt cryptanalysis.txt
```

To make things a bit easier for you, this version can break the previous version by requiring
the number along with the `-a`. That mean's for this version of the program, Eve would need to run `$ python3 monocipher.py -a 1 cipher.txt cryptanalysis.txt` rather than `$ python3 monocipher.py -a cipher.txt cryptanalysis.txt` to perform a single letter frequency analysis. If you want, you can attempt to allow both the version 3, no number option, and the version 3.5 numbered option. It's up to you.

# Version-Based Grading Rubric

Fully completing a version, *which includes the versions proceeding it*, will determine
the overall range in which your project grade will fall according to the table below.


| <u>Version</u> | <u>Grade Range</u> |
| :---: | :---: |
| 0 | 60-69  |
| 1 | 70-79  |
| 2 | 80-84  |
| 2.5 | 85-89 |
| 3  | 90-93  |
| 3.5 | 94-100 |

The only reason your program should crash is because of user error (wrong file order, sneaky-bad inputs, etc.). If the program crashes on a version 1 command but runs successfully on version 2, then it's still considered version 1. So, be certain to have a habit of testing new and previously completed
commands with each new version to ensure you have not broken something that perviously functioned without error. A version is not complete if the features associated with that version and all previous versions cannot be run from the CLI using basic commands like those shown above. Turning in code that only does the analysis features of version 3 is not the same as completing version 3. If you turn in such a program, then you should expect a grade similar to that of a project that only completed version 0 or 1.


The clarity and quality of your code as well as the overall design you've employed will determine where you fall within that range. Good design means making good use of functions and writing functions that have clear, singular purpose. Code with a high degree of clarity and quality code *documentation, good variable and function names, and is well organized*. 
