# Project Euler Problem #10 - Val Coppo
# Summation of primes
# Find the sum of all the primes below two million.

# Variables
primelist = []
n = 2000000
from functools import reduce

primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2,n)))


print (sum(primes)
