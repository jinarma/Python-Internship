# decimal to binary w/out function

decimalNum = 37
temp = 0
list1 = []


while decimalNum != 0:
	temp = decimalNum%2
	list1.append(temp)
	decimalNum = decimalNum//2

print(list1[::-1])