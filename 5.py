__author__ = 'kelly'

#finds smallest positive number that is evenly divisible by 1-20

divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

for x in xrange(2520, 999999999, 20):
    if all(x % y == 0 for y in divisors):
        print x
print None
