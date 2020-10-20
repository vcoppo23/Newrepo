#Project Euler #1 - Val Coppo
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Variables
n = 1
res = 0

while n <= 1000:
    if n % 3 == 0 or n % 5 == 0:
        res = res + n
        n += 1
    else:
        n += 1

print ("The sum of every multiple of 3 and 5 below 1000 is", res)
