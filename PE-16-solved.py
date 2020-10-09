# Project Euler Problem #16 - Val Coppo
# What is the sum of the digits of the number 2**1000?

number = 2**1000

sum_of_digits = 0
for digit in str(number): 
    sum_of_digits += int(digit)
print(sum_of_digits)
