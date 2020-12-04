# Project Euler Problem #11 - Val Coppo
# Largest product in a grid
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally in the 20×20 grid?


# Variables
matrix = """08 02 22 97
49 49 99 40
81 49 31 73
52 70 95 23
"""
print (matrix)
line = matrix.splitlines()

def check(x,y):
    number_box = line[y].split(" ")
    print(number_box[x])
    



