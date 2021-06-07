# Project Euler #25 - Val Coppo
#Fibanachi number with 1000 digits

x = 0
y = 1
count = 1
tracker = []

while len(str(y)) <= 999:
    
    # Fib formula 
    y = x + y
    x = y - x
    count += 1
    tracker.append(y)
    tracker.append(count)
print (tracker[-1])
