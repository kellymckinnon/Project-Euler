__author__ = 'kelly'

#Finds largest palindrome made from product of 2 3-digit numbers

def isPalindrome(num):
    numAsString = str(num)
    for x in xrange(0, len(numAsString)/2):
        if numAsString[x] != numAsString[len(numAsString)-x-1]:
            return False
    return True

palindromes = []

for x in xrange(100,999):
    for y in range(100,999):
        product = x*y
        if isPalindrome(product) and not palindromes.__contains__(product):
            palindromes.append(product)

palindromes.sort()
print palindromes[-1]