#!/usr/bin/env python

#sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

#Demonstrate set operations on unique letters
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

#Set Comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
