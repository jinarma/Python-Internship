# exception


fuel = input('Enter quantity: ')

try:
	if fuel.lower() != 'null':
		print('Petrol Quantity =', fuel)
	else:
		raise ValueError
except ValueError:
	print('There is no fuel in the bike')