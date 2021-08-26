#try without sympy

def prime_check(num):
	flag = 0
	for i in range(2, num):
		if num%i == 0:
			flag += 1
	if flag == 0:
		return num
	else:
		return None


def twin_prime(num_list):
	for i in num_list:
		temp = 0
		if prime_check(i):
			temp = i+2
			if prime_check(temp):
				print(i, 'and', temp)


twin_prime(list(range(1, 51)))
