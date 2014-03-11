#!/usr/bin/env python

# any non-zero integer value is true; zero is false
# anything with a non-zero length is true; empty sequences are false

a, b = 0, 1            # multiple assignment
while b < 10:
    print b,           # suppresses newline
    a, b = b, a+b 

print

x = int(raw_input("Please enter an integer: "))
if x < 0:
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'

words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)

for w in words[:]:   # Loop over a slice copy of the entire list
    if len(w) > 6:
        words.insert(0, w)
print words

# The range function

print range(10)
print range(5, 10)
print range(0, 10, 3) # increment by 3
print range(-10, -100, -30)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]

# see also enumerate(), and Looping Techniques

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else: # else clause begins to the for loop
        # loop fell through without finding a factor
        print n, 'is a prime number'

# for more on try, see Handling Exceptions

for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num

# while True:
#    pass # Busy-wait for keyboard interrupt
