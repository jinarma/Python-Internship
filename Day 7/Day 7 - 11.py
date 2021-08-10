# exception

try:
	age = int(input())
	if age < 18:
		raise ValueError
	else:
		print("he is eligible")
except ValueError:
	print("he is Underaged")