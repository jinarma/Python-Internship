

def chinese_puzzle(heads, legs):
	chickens, rabbits = 0, 0
	rabbits = (legs/2) - heads
	chickens = heads - rabbits
	if chickens%1 != 0 and rabbits%1 != 0:
		print('Invalid')
		return
	print(int(chickens), 'chickens,', int(rabbits), 'rabbits')

chinese_puzzle(35, 94)
chinese_puzzle(38, 95)
chinese_puzzle(38, 94)

