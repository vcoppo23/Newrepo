# Project Euler #7 - Val Coppo
# 10001st Prime Number
# What is the 10 001st prime number?

# Variables

primelist = []
import math
y = 1
n = 0

# Prime checker
def sieve(x):
    
    sqrt = int(math.sqrt(x))
    for i in range (2, sqrt):
        if x % i == 0:
            return False
    return x

# Checks prime checker and then adds to list if true
while n <= 10005:
    
    if sieve(y) != False:
        primelist.append(sieve(y))
        n += 1
    y += 2
    
print (primelist[10001])
