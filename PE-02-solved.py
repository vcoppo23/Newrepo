# Project Euler Problem #2 - Val Coppo

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

# Variables
x = 0
y = 1
ans = 0

while x <= 4000000:
    
    y = x + y     #Fibinachi Formula
    x = y - x

    if y % 2 == 0: #checks if even term
        ans += y
print ("The sum of even valued Fibonacci numbers up to 4 million is:\n", ans, sep = "")
