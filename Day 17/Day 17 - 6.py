#pattern N=3

"""     1    
	   2 2
	  3   3
	 4     4
	5       5
	 4     4 
	  3   3
	   2 2
	    1 """


def pattern(num):
	for i in range(1, num+1):
		if i <= ((num//2)+1):
			print(str(i), " "*(2*i)


count = int(input())
pattern(count)
