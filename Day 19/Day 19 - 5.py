# ques hi ques 2.15		check if its part of fibonacci series


def check_fibonacci(num):
	a = 0
	b = 1
	c = a + b
	if num == a or num == b or num == c:
		print(num, 'is a part of fibonacci sequence')
		return

	while c <= num:
		a = b
		b = c
		c = a + b
		if num == c:
			print(num, 'is a part of fibonacci sequence')
			return
	print(num, 'is not a part of fibonacci sequence')
	return 
	



check_fibonacci(0)
check_fibonacci(2)
check_fibonacci(1)
check_fibonacci(15)
check_fibonacci(13)


