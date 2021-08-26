# pattern

# n = 6
""" 
11111
2222
333
22
1
 """

def pattern(num):
	for i in range(num-1, -1, -1):
		if i >= (num//2)+1:
			print(str(num-i)*i)
		else:
			print(str(i)*i)

pattern(6)
