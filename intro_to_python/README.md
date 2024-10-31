# Week 1: Intro to Python

## Weekly Learning Outcomes

> - Set up resources for running a Python environment (MLO 2)
> - Identify the syntactical differences between Java and Python (MLO 1)
> - Select and apply the appropriate constructs for simple programming solutions using the Python language (MLO 2)

<details><summary><h2>Reading for this Week</h2></summary>

### Core Reading

#### Lesson 1

Chapter 1 for setting up the coding environment

Chapter 2 for Python programming basics

#### Lesson 2

PEP 8 for further tips on writing good quality Python code.

#### Lesson 4

Chapter 3 - Sections 3.1 and 3.2 for data structures and defining functions

### Further Reading

Other optional sources are given throughout the lessons to support learning and gain a broader understanding of the topics covered.

#### Lesson 1

Chapter 2 - pp 39-61

Lee K. D. (2014) Python Programming Fundamentals. 2nd Ed. Undergraduate Topics in Computer Science. Springer, Cham.

Chapter 3 - pp 63-89

Lee K. D. (2014) Python Programming Fundamentals. 2nd Ed. Undergraduate Topics in Computer Science. Springer, Cham.

#### Lesson 3

Chapter 7 - pp 137-174

Padmanabhan T. R. (2016) Programming with Python. Undergraduate Topics in Computer Science. Springer, Cham.

#### Lesson 4

Chapter 1 - pp 1-36

Beazley. D., Jones B. K.  (2013) Python Cookbook. 3rd Ed.  O'Reilly Media

pp 49-60 and 61-67

Stephenson B. (2014) The Python Workbook. A Brief Introduction with Exercises and Solutions. Springer, Cham.

#### Lesson 5

Chapter 5 - pp 115-143

Lee K. D. (2014) Python Programming Fundamentals. 2nd Ed. Undergraduate Topics in Computer Science. Springer, Cham.

Chapter 8 -  pp 39-47

Stephenson B. (2014) The Python Workbook. A Brief Introduction with Exercises and Solutions. Springer, Cham.

#### Lesson 6

Chapter 4 pp 91-113

Chapter 7 pp 163-188

Lee K. D. (2014) Python Programming Fundamentals. 2nd Ed. Undergraduate Topics in Computer Science. Springer, Cham.

</details>

## Lesson 1: Getting Started

I don't want to sound arrogant but I've been using Python a little while, and can deal with the basics of Python as a language, so here's a bit about Anaconda and Jupyter, since these are relatively new to me

### Anaconda

An environment management tool that manages your environments (no way!) YES WAY! It's actually pretty cool in this respect. You can launch loads of different apps from the Anaconda Navigator that will all come loaded with the packages that you've got installed on your environment. Let's say you have an environment for your data mining project, you can install Jupyter and launch it from there with data mining packages in the environment. You can also, at the same time, launch another instance of Jupyter from your Web App environment with a bunch of other packages installed!

Anaconda also comes pre-packaged with a useful command line interface that's good for installing packages in the same way you would for pip in native Python. You can specify different sources like conda-forge and install R packages as well!

Environment management is a really useful thing to be able to do.

### Jupyter Notebooks

Jupyter Notebooks is a tool for running interactive Python (or R) scripts on your local machine as a server. Python is run in cells that you can run individually. This is really useful if you have a long script that you don't want to run the entirety of.

Cells can also have markdown and plain text in them which is really what makes this a Notebook - you can, and should, be using these cells as notes and headers and separators and stuff. Great stuff.

## Lesson 2: Best Practice

This one is all about [PEP 8](https://peps.python.org/pep-0008/) - one of the lovely style guides for writing Python code. One of the guiding principles for writing code is "code is read more often than it is written", highlighting the need for well-written, beautiful looking code :)

### Naming Conventions

Lots of people complain about Python's naming conventions, but I say bah I hate anything that isn't snake_case (actually a lie, I kinda like camel case, I just don't like the languages that use it).

snake_case is a naming convention that means we name our variables and functions using lowercase, with underscores separating meaningful words or phrases.

Other languages might declare a variable `aGoodLookingVariable`, while Python would call it `a_good_looking_variable`. Same goes for functions, though I personally think they should be something different to variable names. There's a whole load of caveats involved like underscores and types of variables (not types of data) like covariants and contravariants (whatever they are).

Names are really important. We'd like to keep names short and simple, yet descriptive, but in the case that we're developing with an intuitive IDE like VS Code, autofill means we can create variables with name length as long as we need them to be. Particularly useful in testing suites that require very specifically descriptive function names.

### Layout and Whitespace

Layout is a really important part of Python as a language. PEP 8 includes guidelines for indentation (structurally meaningful in code execution), how long a line should be, where to include whitespaces, even how to import things beautifully.

Of course, these are all guidelines and most of these suggestions don't actually affect how the code is run. For example, PEP 8 says:

> ```python
> # Correct
> spam(1)
> ```
>
> ```python
> # Incorrect
> spam (1)
> ```

Despite the fact that both are syntactically correct. We obviously can tell that one looks horrible and the other does not.

### PEP 0

[PEPs](https://peps.python.org/pep-0000/) (Python Enhancement Protocols) are Python's version of best standards, written by Guido van Rossum (the original Python dude) and a few others. They outline how Python *should* be used as well as how it *must* be used. PEP 8 is probably the most referenced PEP of them all. PEP 0 is the index of all PEP pages.

## Lesson 3: String and I/O

### Strings

Strings are one of the many data types in Python. they're pretty cool. Essentially, they're just lists of characters, but they're immutable so maybe they're more like tuples? Anyway, I'll preface this with saying there are no primitive data types in Python. Every data type is a subclass of Python Objects.

Back to strings. Strings are simple. When declaring a variable a string, you just enclose some text in quotes. What's cool is that there are 4 different ways of doing this:

```python
'single quotes'
"Double quotes"
"""triple quotes"""
`backticks`
```

Because there are four of them, they can be used in conjunction with each other without having to escape the other as with an escape character. Interestingly, triple quotes serve a purpose as docstrings. These are multi-line strings that are used to describe a method, variable or even a module.

Strings also come with a series of methods for string manipulation like `.upper()`, `.lower()`, `.split()`, `.count()` and `.title()`. They're simple, but effective. Another good one is `.join()`. This one concatenates a string delimiter with items in a list-like object (including other strings):

```python
' + '.join(['a', 'b', 'c'])
>>> 'a + b + c'
```

#### String Formatting

There comes a time where you need to place variables in strings. This becomes very cumbersome to do if you have data types that *can be* implicitly cast to string (like numbers) but don't get cast in contatenation. For example:

```python
x = 3.14
y = "Pi is roughly " + x + "."
```

will throw a `TypeError`, because x hasn't been cast to string (`str(x)` would fix this). Instead, we can place them inside the string using `.format()` or f-strings.

```python
x = 3.14

y1 = "Pi is roughly {}".format(x)

y2 = f"Pi is roughly {x}"
```

Both will cast `x` to string and place it in the string appropriately.

We can also decide how it should be formatted. For example, let's say we have the irrational number $\sqrt{2}$. We want to place it in a string without too many decimal places. We can do this as follows:

```python
x = math.sqrt(2)

y = f"Root 2 to 2 decimal places is: {x:.2f}"
```

OMG actual exercises now! Have a look at
