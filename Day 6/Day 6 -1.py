#user defined fibbonacci function

def fib(num):

	if not isinstance(num, int):
		print('Please enter an integer')
		quit()

	fib_list = []
	a=0
	b=1
	if num<0:
		return 'Invalid choice!'
	elif num==0:
		return 'No Fibbonacci'
	elif num>0:
		if num==1:
			fib_list.append(a)
			return fib_list
		elif num==2:
			fib_list.append(a)
			fib_list.append(b)
			return fib_list
		else:
			fib_list.append(a)
			fib_list.append(b)
			c=a+b
			for i in range(num-2):
				fib_list.append(c)
				a=b
				b=c
				c=a+b
		return fib_list


print(fib(3))