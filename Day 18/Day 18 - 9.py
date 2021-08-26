#ques hi ques 6


def perfect_num(num):
	sum = 0
	for i in range(1, num):
		if num%i == 0:
			sum += i
	if sum == num:
		return print('{} is a Perfect number'.format(num))
	else:
		return print('{} is not a Perfect number'.format(num))

perfect_num(6)
perfect_num(10)
perfect_num(28)
perfect_num(69)
perfect_num(496)