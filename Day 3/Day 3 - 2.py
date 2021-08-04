#sequence of fibbonaci
num = int(input("enter a number greater than 0: "))
if num == 1:
	print(0)
elif num == 2:
	print(0, 1)
elif num > 2:
	a = 0
	b = 1
	c = a + b
	print(a, b, c, end=' ')
	while c < num-2:
	
		print(c, end=' ')
		a = b
		b = c
		c = a + b	
