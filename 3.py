__author__ = 'kelly'
import math

#finds largest prime factor of 600851475143

factors = []

def isPrime(y):
    for x in xrange(2 , y-1):
        if y % x == 0:
            return False

    return True

for x in xrange (1, (int)(math.sqrt(600851475143))):
    if 600851475143 % x == 0:
        if isPrime(60085147513/x):
            factors.append(600851475143/x) #bigger of factor pair
        if isPrime(x):
            factors.append(x) #smaller in pair

factors.sort() #ascending order

print factors[-1] #last element