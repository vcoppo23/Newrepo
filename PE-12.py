# Project Euler Problem #12 
# Highly divisible Triangle Number
# What is the value of the first triangle number to have over five hundred divisors?


# Variables
import math
add = 0
i = 0


def multiple_counter(n):
    x = 0
    for i in range(1,int(math.sqrt(n))):
        if n % i == 0:
            x += 1
    return x + 3


def tri_num(m):
    t = m*(m+1)/2
    return multiple_counter(t)

def tri_num_check(b):
    return b*(b+1)/2


while tri_num(add) < 100:
    #print (tri_num(add), tri_num_check(add))
    tri_num(add)
    add += 1
print (tri_num_check(add))
print (multiple_counter(64))
