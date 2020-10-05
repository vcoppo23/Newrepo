# Project Euler #7 - Val Coppo
# 10001st Prime Number
# What is the 10 001st prime number?

# Variables

primelist = []

x = 10001
n = 1

while x > 0:
    
    if n >= 1:  
       for i in range(2, n//2): 
           if (n % i) == 0: 
               break
       else: 
           primelist.append(n)
           x -= 1
  
    else: 
       pass 
    n += 2
    
print (primelist[-1])

