""" English is a weird language full of exceptions, so could make it work fully, e.g. play doesn't work """


""" s1 = 'struggle'
print(s1[len(s1)-2::1])
print(s1[len(s1)-2:-1])
print(s1[-2]) """


def make_ing_form(string):
	new_string = ""
	vowel = 'aeiou'

	# for when word ends with 'ie'
	if string[len(string)-2::1] == 'ie':
		new_string = string[:-2:1] + 'ying'

	# for when word ends with just 'e'
	elif string[-1] == "e":
		new_string = string[:-1:] + "ing"

	# for when an 'r' is encountered
	elif 'r' == string[-1] and string[-2] in vowel:
		new_string = string + 'ing'
				
	# for when a CVC is encountered 
	elif string[-2] in vowel and string[-1] not in vowel and string[-3] not in vowel:
		new_string = string + string[-1] + 'ing'

	else:
		new_string = string + 'ing'
	print(new_string)


make_ing_form("fire")
make_ing_form("lie")
make_ing_form("encounter")
make_ing_form("steer")
make_ing_form("letter")
make_ing_form("bed")
make_ing_form("play")


