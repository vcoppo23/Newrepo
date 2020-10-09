# Project Euler Problem #12 
# Highly divisible Triangle Number
# What is the value of the first triangle number to have over five hundred divisors?


# Variables
import math
add = 0
i = 0
divisors = [0]

def multiple_counter(n):
    x = 0
    for i in range(1,int(math.sqrt(n))):
        if n % i == 0:
            x += 1
    if x > 4:
        x = 0
        for b in range (int(n//2)):
            if n % i == 0:
                 x += 1
        else:
            return False
                
        return x + 2
print (multiple_counter(3))
def tri_num(m):
    t = m*(m+1)/2
    #print (t)
    return multiple_counter(t)
    
for i in range (50000):
    #print (tri_num(i), i)
    
    if tri_num(i) >= 10:
        print (tri_num(i), i*(i+1)/2)
        break



#while max(set(divisors)) < 500:

  #  i += 1
   # add = add + i
   # divisors = []
   # divisors.append(multiple_counter(add))
    #print( max(set(divisors)),  add, i) # this is my debugger

#print (add,max(set(divisors)))

