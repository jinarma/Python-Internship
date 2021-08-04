import sympy
for i in range(1, 101):
	if sympy.isprime(i):
		print(i)
	else:
		continue