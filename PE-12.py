# Project Euler Problem #12 - Val Coppo
# Highly divisible Triangle Number
# What is the value of the first triangle number to have over five hundred divisors?


# Variables
import math
add = 1
multiples = []





def factors(x):
    for n in range(1, x + 1):
        if x % n == 0:
            return x
        else:
            return None
for i in range(7):
    add += i
    print (add - 1)
    multiples.append(factors(add))
    print(multiples)
