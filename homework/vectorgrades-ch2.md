---
layout: page
title: COMP152 - Homework - Chapter 2 - Vectorized Grade Calculator
permalink: /teaching/COMP151/homework/vectorgrades
mathjax: true
---

At its core, this assignment calls upon you to extend the `Vector` class discussed in section 2.3.3
of the text by completing a series of reinforcement problems from the end of the chapter. But, before you charge off and start these problems, we'll setup a real-world problem that would benefit from the vector class and some of the changes you'll make as part of doing these problem. As a result we'll also add a few more practice problems to the assignment based on the application described below. So, be sure to read on before hopping down to the to do section at the end of this page.

## Grade Calculations as Vector Math

Vector mathematics is incredibly important in science and engineering and is the backbone of machine learning and computer graphics.  In programming we can use *vectorized* code to leverage optimized and parallelized hardware and software that supports vector mathematics operations. In short, classes like the the `Vector` class we're creating here see a wide array of uses in modern computing. The [NumPy](https://numpy.org/) package for Python is a perfect example of this.

While vectors can be found all over modern computing, it's entirely possible that you yourself have not yet encountered vector mathematics in your studies. If that's the case, then the `Vector` class and all of these additions we're making lack any real context and these problems are probably esoteric. That means this assignment might not motivate you much beyond getting some practice with python classes. Even if you're familiar with vectors, it can be really hard to develop general purpose classes such as `Vector` without a concrete application in mind. Such an application grounds the work and lets you, the class designer, test your design choices against real-world use cases.

To give our `Vector` class and the homework problems a bit of meat and to give us a problem for which `Vector` objects might be a good solution, we need look no further than the syllabus for this very course.

### Your Homework Grade is an Average

Your overall homework, exam, lab, and project grade for this course is calculated as the average of all the assignment grades in that category. Let's look specifically at homework. You can then apply the techniques used on your homework grade to all the other assignment categories (exams, labs, and projects).

Assume you've completed three homework assignments with the following scores: 45/50, 35/35, and 65/80. To compute your current overall homework grade you would need to average these three scores as follows:

$$ \frac{ \frac{45}{50} + \frac{35}{35} + \frac{65}{80}}{3} = \frac{.9+1+.8125}{3} \approx .9042 $$

As you can see, your current homework grade would be about 90%, or an A-. That kind calculation should be  relatively familiar to you, it's a standard average calculation. If it's not, then that's OK too because either way we're going to turn it on its head and re-envision it as a vector mathematics problem.

#### A Vectorized Homework Grade Calculation

First let's tease out two vectors: your individual assignment scores and their relative weights. The score vector is pretty straight forward. It contains the number of points you earned on each the assignment. Let's call this vector $g$ and write out what it looks like for our fictional scenario using he same syntax used by the `Vector` class `__str__` function.

$$ g = \langle 45, 35, 65 \rangle $$

The weight vector takes a bit more creativity. For it we need the multiplicative inverse of the maximum possible points for each assignment. That's 1 divided by the maximum possible points for the assignment. So, for an assignment with 50 possible points, the associated weight is 1/50. Thus, for our ongoing example this gives us the weight vector $w$ as,

$$ w = \left\langle \frac{1}{50}, \frac{1}{35}, \frac{1}{80} \right\rangle \approx \langle .02, .02857 , .0125 \rangle $$

Now, using vectors $g$ and $w$ we can proceed to compute your homework grade. First we get the numerator of our average by multiplying each score by the corresponding weight and then adding those values together like so,

$$
\begin{array}{rcl}
g_0*w_0 + g_1*w_1 + g_2*w_2 & = & (45*.02) + (35*.02857) + (65*.0125) \\
&\approx& .9 + 1 + .8125 \\
&\approx & 2.7125
\end{array}
$$


It turns out that this operation is **exactly** the `__mul__` operation as described in problem R-2.14 and is known as the *vector dot product*. For $n$ dimensional vectors $g$ and $w$, the dot product $g*w$ is defined as,

$$ g*w = \sum_{i=0}^{n-1} g_i*w_i $$

When applied to our example problem we get,

$$
\begin{array}{rcl}
g*w &=& \sum_{i=0}^{2} g_i*w_i \\
&=& g_0*w_0 + g_1*w_1 + g_2*w_2 \\
&\approx& 45*.02 + 35*.02857 + 65*.0125 \\
&\approx& .9 + 1 + .8125  \\
&\approx& 2.7125
\end{array}
$$

So, once you've computed $g*w*, all that's left to get your overall grade is to divide the result of $g*w$ by 3. But wait! It turns out that we can vectorize this step as well by rethinking the division as multiplication by the inverse.

$$
\frac{g*w}{3} = \frac{1}{3}*g*w
$$

In vector mathematics, the multiplication by 1/3 can be done before or after the dot product! If you do it before, then you're just using `__rmul__` as described in problem R-2.13 to perform *scalar multiplication*. In this case each element of $g$ is multiplied by 1/3. It actually doesn't matter when we do the scalar multiplication. As they say in mathematics, it's associative and commutative.

$$
\frac{1}{3}*(g*w) = \left( \frac{1}{3}*g\right) *w = g* \left( \frac{1}{3}* w \right)
$$

We can now look at computing our desired average as a combination of scalar multiplication and the vector dot product, both operations we can overload into `__mul__` or `__rmul__` as part of our `Vector` class.

#### Vector Math to Vector Class

To carry out grade calculations we need to outfit our Vector class with the modifications to multiplication described in R-2.13 and R-2.14. If we also add to this the enhanced constructor described in R-2.15, then we can use the Vector class to compute your homework grade with as little as three lines of code!

First, you construct your grade and weight vector. Then, you can compute the grade with a single line expression. The complexity of the vector mathematics, all the loops and arithmetic, is handled by the Vector class implementation and hidden from the code used to compute the actual grade. If your concern is the grade and not the calculation of the grade, then this kind of code let's you focus on grade-level details rather than calculation-level details.

```python
g = Vector([45,35,65])
w = Vector([(1/50),(1/35),(1/80)])
hwkgrade = (1/3) * g * w
```

## Final Grades: More of the Same

In the syllabus you can find the weights associated with your homework, labs, projects, and exams. Given these weights and your final assignment category grades, your final grade is computed by a single dot product! No final average is needed because that's already built into the weights.

For example, if your final homework grade is .9, your lab grade is .95, your exam grade is .82, your project grade is .85, and you get full points for participation, then your final grade is just the dot product of those grades and their associated weights.

$$
\begin{array}{rcl}
g*w &=& \langle .9, .95, .82, .85, 1.0 \rangle * \langle .16, .1, .49, .2, .05 \rangle \\
 &=& .8608
\end{array}
$$

The end result in this example is an 86%, or a B. All of that can be computed with a few lines of Python *if* we take the time to flesh out a Vector class.

It's worth noting that computing your current grade in the middle of the semester takes a bit more work. The weights in the syllabus are based on the total number of assignments for each type of assignment. Calculating your current grade needs takes this into account and come up with different weights than those used above. Have no fear. This too can be vectorized. We'll leave that bit of math for another day because at this point we have at least a little bit of real-world work to groud our `Vector` class development.

#### An Opportunity for Code Reuse

But, wait! There's more! I'm going to ask you to build two functions in this assignment: one for assignment categories like homework and one for the final grade. Remember how the last step of the homework grade calculation, the multiplication by 1/3, could be done before or after the dot product? Well, because of this, we can rethink the homework calculation as a special case of the final grade calculation. In programming terms, we can use the final grade calculation computation as the basis for the category grade computation. Put another way, the category grade calculation function should just prepare vectors then call to the final grade calculation function to get the end result.

To see how this works recall this relationship.
$$
\frac{1}{3}*(g*w) = \left( \frac{1}{3}*g\right) *w = g* \left( \frac{1}{3}* w \right)
$$

Both $\left( \frac{1}{3}* w \right)$ and $\left( \frac{1}{3}*g\right)$ produce a vector. When developing our category grade calculation function we can first compute vector $g^{\prime} = \left( \frac{1}{3}*g\right)$ then pass vectors $g^{\prime}$ and $w$ to the final grade calculation function to get $g^{\prime} * w$, the category grade.

# To Do

Now let's get down to brass tacks. Here's what you need to do. We'll start with the grade calculation work.

Do each of the following. Create new unit tests for the changes you've made. Automatic tests can and should be run, but think of them not as your only tests but a series of tests that verifies your code and your own tests.
1. R-2.12 (`__mul__`)
2. R-2.13 (`__rmul__`)
3. R-2.14 (updates to `__mul__`)
4. R-2.15 (updates to `__init__`)

With these problems complete, you can implement the grade calculation functions. *These should be done in `main.py` but unit tests for these functions can be added to `vectortests.py`. Use the exact names described below or pre-written assignment tests will not pass.*

5. Use what's described in the section *Final Grades: More of the Same* to design, implement and test a function called `finalgrade` that takes in two vectors, the scores and weights, and returns the associated final grade.
6. Use what's described in the section *Homework Average* to create a function called `categorygrade` that takes two vectors, the scores and weights for an assignment category, and returns the current grade for that category based on the values in these vectors. Use the code reuse idea described in the section above titled *An Opportunity for Code Reuse*.

Now for a bit more practice do the following (code and unit tests!). Hint: There's an Opportunity for code reuse with these two.

7. R-2.10 (`__neg__`)
8. R-2.9 (`__sub__`. subtraction here acts like addition. you subtract by corresponding location rather than add.)


In case it's not clear, you should write unit tests for every method and function you write in the file `vectortests.py`. The assignment also comes with tests for all of these methods and functions. These tests help you verify that your tests are good and might catch any cases you missed. Both sets of tests should pass when you complete the assignment.
