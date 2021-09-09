# ceaser cipher

def encoder(rotation, message):
	first_half = 'abcdefghijklm'
	last_half = 'nopqrstuvwxyz'
	encoded_message = ''
	for letter in message:
		if letter.casefold() in first_half:
			encoded_message += chr(ord(letter)+rotation)
		elif letter.casefold() in last_half:
			encoded_message += chr(ord(letter)-rotation)
		else:
			encoded_message += letter	
	return encoded_message


def decoder(rotation, code):
	first_half = 'abcdefghijklm'
	last_half = 'nopqrstuvwxyz'
	decoded_message = ''
	for letter in code:
		if letter.casefold() in first_half:
			decoded_message += chr(ord(letter)+rotation)
		elif letter.casefold() in last_half:
			decoded_message += chr(ord(letter)-rotation)
		else:
			decoded_message += letter
	return decoded_message
	

print(encoder(13, 'My name is'))
print(decoder(13, 'Zl anzr vf'))
print(decoder(13, 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))
