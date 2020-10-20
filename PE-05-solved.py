# Project Euler Problem #5 - Val Coppo
# Smallest Multiple
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

#variables
a = True
x = 2520      # smallest multiple of 1-10

while a == True:
    if x % 19 == 0 and x % 18 == 0 and x % 17 == 0 and x % 16 == 0 and x % 15 == 0 and x % 14 == 0 and x % 13 == 0 and x % 12 == 0 and x % 11 == 0:
        print (x)
        a = False

    x += 2520     # we can iterate by this because all answers must also be divisible by 1-10, speeds up program a lot
