# ques hi ques 2.14 armstrong

def armstrong_check(num):
	num_list = list(map(int, str(num)))		#important technique
	power = len(num_list)
	sum = 0
	for i in num_list:
		sum += i**power

	if num == sum:
		print(num, 'is an armstrong number!')
	else:
		print(num, 'is not an armstrong number!')




armstrong_check(12345)
armstrong_check(371)