#!/usr/bin/env python
#Example 1
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print('jack')
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)

#Example 2
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

#Example 3
print({x: x**2 for x in (2, 4, 6)})

#Example 4
print(dict(sape=4139, guido=4127, jack=4098))
