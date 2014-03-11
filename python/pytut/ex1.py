#! /usr/bin/env python

x = y = z = 0
x = 1j * 1J # equals (-1+0J)
x = 1j * complex(0,1)
a = 1.5 + 0.5j
print a.real
print a.imag
print "abs(a): ", abs(a)

# in interactive mode, the last printed expression is assigned to _ 

print 'spam eggs'
print 'doesn\'t'
print "doesn't"
print '"Yes," he said.'
print "\"Yes,\" he said."
print '"Isn\'t," she said.'

hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."

print hello

print """
Usage: thingy [OPTIONS]
     -h                      Display this usage message
     -H hostname             Hostname to connect to
"""

hello = r"This is a rather long string containing\n\
several lines of text much as you would do in C."

print hello

word = 'Help' + 'A'
print word
print '<' + word*5 + '>'
print 'hel' 'lo' # prints 'hello' -- only works for string literals


print word[4]
print word[0:2]
print word[2:4]

print word[:2]
print word[2:]

# Python strings cannot be changed
# word[0] = 'x' results in an error

# creating a new string with the combined content is easy:
print 'x' + word[1:]

print word[:2] + word[2:] # the same as word

# degenerate slices:
print word[1:100] # an index that is too large is replaced by string size; prints 'elpA'
print word[10:]   # an upper bound smaller than the lower bound returns empty string
print word[2:1]

# indices may be negative numbers, to start counting from the right
print word[-1]  # the last character
print word[-2]  # the second to last character
print word[-2:] # the last two characters
print word[:-2] # everything but the last two chars

# out of range negative slices are truncated
print word[-100:]

#  +---+---+---+---+---+
#  | H | e | l | p | A |
#  +---+---+---+---+---+
#  0   1   2   3   4   5
# -5  -4  -3  -2  -1
# the slice from i to j consists of all characters between the edges labeled i and j

# the built-in function len() returns the length of a string

# see also:
# Sequence types: str, unicode, list, tuple, bytearray, buffer, xrange
# String Methods
# String Formatting
# String Formatting Operations

# Unicode Strings

print u'Hello\u0020World!'
# See also: raw unicode strings and unicode() and .encode()
