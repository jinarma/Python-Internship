""" 
n = 3

   A
  BAB
 CBABC

 """

def pattern(num):
	for i in range(1, num+1):
		j = 0
		print((' '*(num-i)), end="")
		print(chr(64+i))
		for j in range(i):


pattern(3)
