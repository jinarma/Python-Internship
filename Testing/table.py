num = int(input('Enter the number for table: '))
count = int(input('End at: '))

for i in range(count):
	print('{} x {} = {}'.format(num, i+1, num*(i+1)))

