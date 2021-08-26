#ques5.png
# 12ksdk552af*
# learn about itertools module

string1 = input()

list1 = str(string1)
temp = []
largest_even_num = ''

""" takes out all the integers from the list """
for i in list1:
	if i.isdigit():
		temp.append(int(i))

		
print(set(temp))

""" converts the list to set to remove duplicates then converts it back to list 
sorts in descending order """
list1 = list(set(temp))
list1.sort()

""" traverses the list to find an even number
if encountered bring it to the front of list
if no even number is found then print -1 and exit """
for i in list1:
	if i%2 == 0:
		list1.insert(0, list1.pop(list1.index(i)))
		break
	elif i%2 != 0 and i == list1[len(list1)-1]:
		print(-1)
		exit()

""" Reverses the list """
list1 = list(reversed(list1))
print(list1)

""" Converts the list to string and prints it """
for i in list1:
	largest_even_num += str(i)
print(largest_even_num)


