# Project Euler Problem #35- Val Coppo
# Circular primes
# How many circular primes are there below one million?

import math
count = 2
total = 0
def prime_check(x):
    if x % 2 == 0:
        return False
    
    for i in range(2, x - 1):
        if x % i == 0:
            return False

    return True
    
while count < 1000000:
    if prime_check(count) == True:
        total += 1
        count += 1
    else:
        count += 1

print (total)
