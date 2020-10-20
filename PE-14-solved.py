# Project Euler Problem #14 - Val Coppo
# Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?

# Variables

x = 1
coltezlist = []


# Functions

def bookie(func):   #Bookie function just keeps track of number of iterations of the collatz function
     func.count += 1

def coltez(n):         # This it the Collatz function, it does the bulk of the work
    bookie(coltez)
    if n == 1:
        return 1
    if n % 2 == 0:

       # print (n)
        return coltez(n // 2)
        
    elif n % 2 != 0:
        
        #print (n)
        return coltez((3*n)+1)

# Checker

while x <= 1000000:      #checks every number below 1,000,000
    coltez.count = 0
    coltez(int(x))
    coltezlist.append(coltez.count)
    x += 1
    
coltezlist.insert(0,0)   #inserts to the start of the list to make the count right
m = max(coltezlist) 
t = [i for i, j in enumerate(coltezlist) if j == m]
t = t[0]
print (t, coltezlist[t])


