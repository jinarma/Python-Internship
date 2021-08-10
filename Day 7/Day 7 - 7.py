# reverse string using recursion w/out slicing

def reverseString(string1):
	if len(string1) == 0:
		return string1
	else:
		return(string1[1:])+string1[0]

string = str(input())
print(reverseString(string))