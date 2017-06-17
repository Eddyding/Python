#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 2
import sympy

a,b = 500,600
numbers = range(a,b)


prime_numbers=filter(sympy.isprime,numbers)
print("Prime numbers({}-{}):".format(a,b))
for prime_number in prime_numbers:
	 print prime_number,
print



