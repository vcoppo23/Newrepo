# Project Euler Problem #3
# Largest prime factor
# What is the largest prime factor of the number 600851475143?
import math
primelist = []
n = 1

while n < 775147:
    n += 1
    m = int(math.sqrt(n))
    if 600851475143 % n == 0:
        if n % 2 != 0:

            for i in range(2, m + 1 ):

                if n % i == 0:
                    break
                else:
                    primelist.append(n)
                    print (n)
                    break


print (max(primelist))
