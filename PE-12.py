# Project Euler Problem #12 - Val Coppo
# Highly divisible Triangle Number
# What is the value of the first triangle number to have over five hundred divisors?


# Variables
from functools import reduce
from math import sqrt
add = 0
i = 0

factors = lambda n: {f for i in range(1, int(n**0.5)+1) if n % i == 0 for f in [i, n//i]}

def tri_num(m):
    t = m*(m+1)/2
    return len(factors(t))

def tri_num_check(b):
    return b*(b+1)/2


while tri_num(add) < 500:
    tri_num(add)
    add += 1
print (tri_num_check(add))
