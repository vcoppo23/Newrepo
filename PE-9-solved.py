# Project Euler problem 9 - Val Coppo
# Special Pythagorean triplet
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


# Variables
upper = 999
lower = 200
for a in range(lower,upper):
    for b in range(lower, upper):
        for c in range(lower, upper):
            if a < b and b < c:
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        print ("the triplets are",a,b,c,"the product is:", a * b * c)
             
