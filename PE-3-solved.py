# Project Euler Problem #3
# Largest prime factor
# What is the largest prime factor of the number 600851475143?

# Variables
primelist = []
n = 1

def sieve(x):
    for i in range (2, x - 1):
        if x % i == 0:
            return False
    return True
    

while n < 775147:
    n += 1
    if 600851475143 % n == 0:
        if n % 2 != 0:
            if sieve(n) == True:
                primelist.append(n)

print (max(primelist))
