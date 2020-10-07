# Project Euler Problem #12 - Val Coppo
# Highly divisible Triangle Number
# What is the value of the first triangle number to have over five hundred divisors?


# Variables

add = 0
z = True
y = True
while y == True :
    divisor = 0
    for i in range(1, 100000000):
        add += i
        print (add)
        #print (i, z, add, divisor)
        if add / i == int(add / i):
           divisor += 1

        if divisor == 500:
            print (i)
            y = False
                
                
