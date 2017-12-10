#!/usr/bin/env python
#Delete
#Example 1
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
#Example 2
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a
print(a)
