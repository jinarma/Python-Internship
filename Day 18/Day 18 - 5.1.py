# ques hi ques 7

import sympy

start = int(input())
end = int(input())
for i in range(start, end+1):
	if sympy.isprime(i):
		print(i, end=' ')

