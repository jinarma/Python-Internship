list1 = list(range(2000, 3201))
string = ''
for i in range(len(list1)):
	if list1[i]%5 == 0:
		continue
	elif list1[i]%7 == 0:
		if i < len(list1)-1:
			print(list1[i], ',', sep='', end=' ')
		else:
			print(list1[i])
