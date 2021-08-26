#special string reverse ques4.png
# abc@cd test string


""" string1 = input('Enter string: ')
list1 = list(string1)
index = []

for i in range(len(temp_list)):
	if not temp_list[i].isalnum():
		index.append(i)

print(index) """

		

#### isalnum important!
### ''.join(list), coverts the the list to a string for that instance

# their code

s = input()
d = dict()

rev = ''
for i in range(len(s)):
	if not s[i].isalnum():
		d.update({i:s[i]})
	else:
		rev += s[i]
print(d, rev)
rev = list(rev[::-1])
for i, j in d.items():
	rev.insert(i, j)
print(''.join(rev))