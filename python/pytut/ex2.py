#!/usr/bin/env python

# Lists

a = ['spam', 'eggs', 100, 1234]
print a

print a[0]
print a[3]
print a[-2]
print a[1:-1]
print a[:2] + ['bacon', 2*2]
print 3*a[:3] + ['Boo!']

print a[:] # returns a shallow copy of the list

# Unlike strings, which are immutable, it is possible to change individual elements of a list
a[2] = a[2] + 23
print a

a[0:2] = [1, 12]             # Replace some
print a
a[0:2] = []                  # Remove some
print a
a[1:1] = ['bletch', 'xyzzy'] # Insert some
print a
a[:0] = a                    # Insert a copy of itself at the beginning
print a
a[:] = []                    # Clear the list (a = [] also works)
print a

# The built-in function len() also applies to lists
print len(a)

# It is also possible to nest lists
q = [2, 3]
p = [1, q, 4]
print len(p)
print p[1]
print p[1][0]
p[1].append('xtra') # See section 5.1
print p
print q
