#pattern
#n = 3
""" 1
	2*2
	3*3*3
	2*2
	1 """


def pattern(num):
	for i in range(1, num+1):
		for j in range(1, i+1):
			if j != i:
				print(str(i)+'*', end='')
			else:
				print(str(i))
	
	for i in range(num-1, -1, -1):
		for j in range(1, i+1):
			if j != i:
				print(str(i)+'*', end='')
			else:
				print(str(i))



count = int(input())
pattern(count)
