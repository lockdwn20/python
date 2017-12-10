#!/usr/bin/env python
#squares
#Example 1
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
#Example 2
squares = list(map(lambda x: x**2, range(15)))
print(squares)
#Example 3
squares = [x**2 for x in range(12)]
print(squares)

#sorting
#Example 1
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
#Example 2
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

#Tuples
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])
# the tuple must be parenthesized, otherwise an error is raised
#print([x, x**2 for x in range(6)])
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

#Complex Expressions
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

#Nested list
#Example 1
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in range(4)])
#Example 2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
#Example 3
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
#Example using pre-built function
print(list(zip(*matrix)))
