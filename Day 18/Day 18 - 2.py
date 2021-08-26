#check spaces in string

def check_space(string):
	count = 0
	for letter in string:
		if letter.isspace():
			count += 1
	print('o/p =', count)

check_space('oaouufn siaofnw  asdunf')