

import sympy


for i in range(1, 51):
	twin_prime = []
	temp = 0
	if sympy.isprime(i):
		temp = i+2
		if sympy.isprime(temp):
			print(i, 'and', temp)



