# prime number


def prime_checker(num):
	for i in range(2, ((num//2)), 2):
		if num%i == 0:
			return num/2
		else:
			continue
	return num**2


print(prime_checker(17))
print(prime_checker(15))
print(prime_checker(20))