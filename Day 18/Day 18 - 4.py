#ques10.png


def first_last(string):
	if len(string) < 2:
		print('Empty String')
		return
	elif len(string) == 2:
		print(string*2)
	else:
		print(string[:2], string[len(string)-2:], sep='')

first_last('w3')
first_last('w')
first_last('w3ervlwe')