# Project Euler Problem #3
# Largest prime factor
# What is the largest prime factor of the number 600851475143?
import math
primelist = []
n = 1

while n < 775147:
    n += 1
    if 600851475143 % n == 0:
        if n % 2 != 0:
            if n % 71 != 0:
                primelist.append(n)

print (primelist)

