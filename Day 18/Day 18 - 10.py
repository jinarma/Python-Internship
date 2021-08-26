# display biggest sum (either even sum or odd sum) from digits of a given number

def biggest_sum(num):
	even_sum = 0
	odd_sum = 0
	temp = 0
	while num:
		temp = num%10
		if temp%2 == 0:
			even_sum += temp
		elif temp%2 != 0:
			odd_sum += temp
		num = num//10
	
	if even_sum - odd_sum >= 0:
		print('Even digit sum', str(even_sum))
	else:
		print('Odd digit sum', str(odd_sum))

biggest_sum(int(input()))

