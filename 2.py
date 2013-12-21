__author__ = 'kelly'

#Finds sum of even-values Fibonacci terms up to 4 million

prev2 = 1
prev1 = 2
term = 0
sum = 2

while (prev1 + prev2) <= 4000000:
    term = prev1 + prev2
    if term % 2 == 0:
        sum+= term
    prev2 = prev1
    prev1 = term

print sum