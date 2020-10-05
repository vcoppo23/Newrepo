# Project Euler Problem #6 - Val Coppo
# Sum Square Diffrence
# Find the difference between the sum of the squares of the first-
# -one hundred natural numbers and the square of the sum.

#VARIABLES & LISTS
n = 0
x = 0
sumlist = []
sqrlist = []


while n <= 100:
    
    sumlist.append(n)
    x = n**2
    sqrlist.append(x)
    n += 1

print (sum(sumlist)**2 - sum(sqrlist))


