num_list = list(range(3, 51))
twin_prime_list = []


def twin_prime(num_list):
	for num in num_list:
		flag = 1
		j = num + 2
		if num > 2:
			for i in range(2, num):
				if (num % i == 0 or j % i == 0):
					flag = 0
					break
			if flag == 1:
				twin_prime_list.extend([[num, j]])
	if twin_prime_list is None:
		print("No Twin Primes found in the given list")
	else:
		for i in twin_prime_list:
			print(i, end=" ")


twin_prime(num_list)
