# ques7.png

def check_anagram(string):
	string = string.casefold()
	s1, s2 = string.split(',')
	print(s1, s2)
	list1, list2 = s1.split(), s2.split()
	dict1, dict2 = [{}]
	for i in range(len(list1)):
		dict1.append(({list1[i]: i}))

	print(dict1)

check_anagram('Hello, there')