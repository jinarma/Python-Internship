


def check_eligible_password(string):
	passwords_list = string.split(',')
	print(passwords_list)		# this split works
	comma_sep_passwords = ''
	last = len(passwords_list) - 1
	for i, password in enumerate(passwords_list):
		password = password.strip()		# used to remove leading and trailing whitespaces, also password.replace(' ', '') could be used.
		# for when we continue the code
		flag = 0
		if len(password) >= 6 and len(password) <= 12:
			for j in password:
				if j.isdigit():
					flag += 1
					break
			for j in password:
				if j.islower():
					flag += 1
					break
			for j in password:
				if j.isupper():
					flag += 1
					break
			for j in password:
				if j in ['$', '#', '@']:
					flag += 1
					break
			if flag == 4 and i is not last:
				comma_sep_passwords = comma_sep_passwords + password + ', '

			elif flag == 4 or i is last:
				comma_sep_passwords = comma_sep_passwords + password
				return comma_sep_passwords



print(check_eligible_password('Ruby1sgre@t, 123djdnq, asjfn23, sanf,finsad5, BreakD@nc3'))

