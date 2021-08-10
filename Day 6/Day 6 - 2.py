# lcm



def lcm_function(number_list):
	
	comparision_list = []
	comparision_set = set()
	lcm = 1
	flag = 0
	for num in number_list:
		for i in range(2, num+1):
			if num % i == 0 and i != num:
				comparision_list.append(i)
				flag += 1
			if flag == 0 and i == num:
				comparision_list.append(i)
				flag = 0

	comparision_set.update(comparision_list)
	for element in comparision_set:
		lcm = lcm * element

	print(comparision_list)
	print(comparision_set)
	return lcm
				
				

number = int(input('How many numbers for lcm: '))
number_list = []

for i in range(number):
	temp = int(input('Num {}: '.format(i+1)))
	number_list.append(temp)

print(number_list)

print(lcm_function(number_list))
