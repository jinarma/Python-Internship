

def election_results(a, b, c, d):
	dict1 = {a:'A', b:'B', c:'C', d:'D'}
	maximum = max(dict1.keys())
	maximum_index = dict1.pop(maximum)
	second_maximum = max(dict1.keys())
	second_maximum_index = dict1.pop(second_maximum)
	if second_maximum * 2 < maximum:
		print(maximum_index, maximum)
	else:
		print(maximum_index, maximum, '|', second_maximum_index, second_maximum)


print(election_results(7, 4, 5, 15))
