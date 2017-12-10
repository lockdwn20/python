#!/usr/bin/env python

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
f1000 = fib2(1000)
print(f1000)
