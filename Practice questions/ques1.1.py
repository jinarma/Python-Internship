

def phrase_palindrome_check(string):
	phrase_list = []
	for i in string:
		if i.isalpha():
			phrase_list.append(i.casefold())
	if phrase_list[::-1] == phrase_list:
		print(string, '- palindrome')
	else:
		print(string, '- not palindrome')

phrase_palindrome_check('Go hang a salami i\'m a lasagna hog')
phrase_palindrome_check('Was it a rat I saw?')
phrase_palindrome_check('Was it a mouse I saw?')