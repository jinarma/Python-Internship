#split string in equal halves

def split_string(string):
	count = len(string)
	s1, s2 = '', ''
	if count%2 == 0:
		s1, s2 = string[0: (count//2)], string[(count//2): ]
	else:
		s1, s2 = string[0: (count//2)+1], string[(count//2)+1:]
	print(s1, s2)

split_string('Engine')
split_string('Enginey')

