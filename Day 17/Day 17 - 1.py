#pattern N=3

"""     *    
	   * *
	  * * *
	 * * * *
	* * * * *
	 * * * * 
	  * * *
	   * *
	    * """

def pattern(num):
	for i in range(1, num+1):
		print((' '*(num-i)), end="")
		print('*'*i, '*'*(i-1), sep='')

	for i in range(num-1, -1, -1):
		print((' '*(num-i)), end="")
		print('*'*i, '*'*(i-1), sep='')


count = int(input())
pattern(count)
