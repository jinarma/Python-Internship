#swastika pattern
# row = 5, col = 5

""" 
*   * * *
*   *
* * * * *
	*   *
* * *   *
 """


def swastika(row, col):
	for i in range(1, col+1):
		if i == 1:
			print('*', ' '*((row//2)-1), '*'*((row//2)+1), end='')
		elif i <= ((row//2)+1):
			print('*', '*'*((row//2)+1), end='')


swastika(5, 5)
