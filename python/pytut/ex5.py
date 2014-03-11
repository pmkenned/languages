#!/usr/bin/env python

a = [66.25, 333, 333, 1, 1234.5]
x = 5
L = [1, 2, 3]
i = 2

print 'a:', a
a.append(x)
print 'append:\n',a
a.extend(L)             # Extend list by appending all the items in the given list. Equiv to a[len(a):] = L
print 'extend:\n', a
a.insert(i, x)          # Insert an item at a given position.
print 'insert:\n',a
a.remove(x)             # Remove first item from list whose value is x. Error if no such item exists.
print 'remove:\n',a
print 'pop: ', a.pop(i) # Remove an item at the given position and return it.
print a
print 'index:', a.index(x)        # return the index of the first item whose value is x. Error if no such item exists.
print 'count:', a.count(x)        # return number of times x appears
a.sort()                # sort in place
print 'sort:\n', a
a.reverse()             # reverse elements in place
print 'reverse:\n', a

# using lists as stacks

# .apppend()
# .pop()

# using lists as queues

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print queue.popleft();
print queue.popleft();
print queue

# functional programming tools

# filter(), map(), and reduce()

# filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true

def f(x): return x % 2 != 0 and x % 3 != 0

a = filter(f, range(2, 25))
print a

# map(function, sequence) calls function(item) for each of the sequence's items and returns a list of the return values

def cube(x): return x*x*x

a = map(cube, range(1, 11))
print a

# reduce(function, sequence) returns a single value constructed by calling the binary function on the
# first two items of the sequence, then on the result and the next item, and so on
# if there is only one item, it is returned; if zero, an error is raised

def add(x, y): return x+y

x = reduce(add, range(1,11))
print x

# a third argument can be passed to indicate the starting value
# the starting value is returned for an empty sequence
# the function is applied to the starting value and the first item

def my_sum(seq):
	def add(x, y): return x+y
	return reduce(add, seq, 0)

x = my_sum(range(1, 11))
print x

# there is a built-in function called sum that works just like this

# list comprehensions

squares = []
for x in range(10):
	squares.append(x**2)

print squares

squares = [x**2 for x in range(10)] # same result as above, but more compact

print squares

z = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print z

# TODO: nested list comprehensions

# the del statement

a = [1, 2, 3, 4, 5, 6]
print a
del a[0]
print a
del a[2:4]
print a
del a[:]
print a
del a
# a no longer exists

# TODO: tuples and sequences

# TODO: sets

# TODO: dictionaries

# TODO: looping techniques
