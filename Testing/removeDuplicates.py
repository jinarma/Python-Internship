def remove_dupes(string):
	list1 = list(string)
	temp=''
	for letter in list1:
		if letter not in temp:
			temp+=letter
	return temp

print(remove_dupes("111223445566677##2213Fqek2fddaaowr"))