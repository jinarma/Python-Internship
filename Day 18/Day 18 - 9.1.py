def perfect_num(count):
	num_list = list(range(1, count+1))
	for i in num_list:
		sum = 0
		for j in range(1, i):
			if i % j == 0:
				sum += j

		if i == sum:
			print(i, end=' ')
	

perfect_num(230581)
