#remove consonants and print only vowels from a string, is case sensitive
#also try using a check string

def vowel_string(string):
	vowel_list = 'aeiou'
	for char in string:
		if char.lower() in vowel_list:
			print(char, end='')

def vowel(string):
	check_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
	for letter in string:
		if letter in check_list:
			print(letter, end='')


vowel('Academy')
vowel_string('Academy')
