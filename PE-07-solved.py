# Project Euler #7 - Val Coppo
# 10001st Prime Number
# What is the 10 001st prime number?

# Variables
count = 0
prime_list = []
number = 0

def prime_check(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range (2, x - 1):
            if x % i == 0:
                return False
        return True

while count <= 10001:
    
    if prime_check(number):
        prime_list.append(number)
        count += 1
    number +=2


    
print (max(prime_list))
