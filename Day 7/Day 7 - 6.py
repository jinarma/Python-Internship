# decimal to binary w function

def binaryConverter(decimalNum):
	temp = 0
	list1 = []


	while decimalNum != 0:
		temp = decimalNum % 2
		list1.append(temp)
		decimalNum = decimalNum//2

	return list1[::-1]

print(binaryConverter(int(input('enter a decimal: '))))