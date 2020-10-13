# Project Euler #7 - Val Coppo
# 10001st Prime Number
# What is the 10 001st prime number?

# Variables

primelist = []
import math
x = 10001
n = 1


def prime_check(n):
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt - 1):
        if n % i == 0:
            return None
            break
    return True

print (prime_check(10))
while x > 0:
    if prime_check(x) == False:
        pass
