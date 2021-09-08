

def pangram_check(string):
	all_alphabets = list('qwertyuiopasdfghjklzxcvbnm')
	for i in string.casefold():
		if i in all_alphabets:
			all_alphabets.remove(i)
	if all_alphabets == []:
		print(string, '- is a pangram')
	else:
		print(string, '- is not a pangram')


pangram_check('The quick brown fox jumps over the lazy dog')
pangram_check('This sentence is obviously not a panagram')
