string1 = [2, 5, 8, 9]
flag = 0
i = 0
counter = 1
lcm = 1
compare = string1[i]
temp = compare
while flag != len(string1):
	if temp%string1[i] == 0:
		flag += 1
		i += 1
		counter = 1
		lcm = lcm * temp
	else:
		counter += 1
		temp = compare*counter
print(lcm)


print(string1[::1])