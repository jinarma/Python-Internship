# display biggest sum (either even sum or odd sum) from digits of a given number
# now for even or odd POSITION digits

def biggest_sum(num):
	even_sum = 0
	odd_sum = 0
	temp = 0
	num_list = list(str(num))
	print(num_list)
	flag = 0
	for i in num_list:
		if flag == 0:
			odd_sum += i
			flag = 1
		else:
			even_sum += i
			flag = 0
	
	if even_sum - odd_sum >= 0:
		print('Even digit sum', str(even_sum))
	else:
		print('Odd digit sum', str(odd_sum))

biggest_sum(int(input()))

