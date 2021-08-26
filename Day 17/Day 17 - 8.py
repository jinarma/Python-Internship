""" 
n = 4

4321
321
21
1
 """


def pattern(num):
	for i in range(num, -1, -1):
		j=i
		print()
		while j:
			print(j, end='')
			j -= 1


pattern(5)
