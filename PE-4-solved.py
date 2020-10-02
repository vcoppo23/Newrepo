# Project Euler Problem #4 - Val Coppo
# Largest palindrome product
# Find the largest palindrome made from the product of two 3-digit numbers.


# Variables

palist = []

for x in range(500,1000):
    for y in range (500, 1000):
        num = x * y
        rev = str(num)    # Reverses the number
        rev = rev[::-1]
        rev = int(rev)
        if rev == num:
            palist.append (num)
        y += 1
        
    x += 1
print (max(palist)) 

