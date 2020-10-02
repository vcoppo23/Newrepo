number = 5235
lstrip = []
import sys 
number = sys.argv[1] 
number = str(number).lstrip("0") 
print (str(number)[::-1]) 
