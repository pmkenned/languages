#!/usr/bin/env python

# Functions

# def introduces a function definition
def fib(n):
    """Print a Fibonaci series up to n.""" # an optional string literal, the docstring
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

fib(100)

# All variable assignments in a function store the value in the local symbol table.
# global variables cannot be directly assigned a value within a function
# (unless named in a global statement)

# variable references look:
# 1. first in the local symbol table
# 2. then in the local symbol tables of enclosing functions
# 3. then in the global symbol table
# 4. finally in the table of built-in names

# parameters to a function call are introduced in the local symbol table of the called function when it is called
# arguments are passed using call by value (where the value is always an object reference, not the value of the object)

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print
print f100

# default argument values

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

# in tests whether a certain value is in a sequence
# the default values are evaluated at the point of function definition in the defining scope
# Thus,
i = 5

def f(arg=i):
    print arg

i = 6
f() # prints 5

# warning: default value is evaluated only once
def g(a, L=[]):
    L.append(a)
    return L
print g(1) # prints [1]
print g(2) # prints [1, 2]
print g(3) # prints [1, 2, 3]

# to avoid this:
def g2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# TODO: keyword arguments

# arbitrary list arguments

def write_multiple_items(file, separator, *args) # arguments are wrapped up in a tuple
    file.write(separtor.join(args))

# unpacking list arguments

args = [3, 6]
range(*args) # * unpacks the arguments from a list or tuple

# lambda forms
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print f(0)
print f(1)

# Coding style
# See PEP 8
