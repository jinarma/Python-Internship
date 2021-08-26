""" 
n = 3

111
00
1

n = 4

0000
111
00
1
 """


def pattern(num):
	for i in range(num, -1, -1):
		print(str(i%2)*i)

pattern(4)