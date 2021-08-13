#int function()
def function(num):

	print(num)
	if num == 1:
		return 1

	return function(num-1) + num

'''
num = 4
function(4)
return function(4-1) + 4

num = 3
function(3)
return function(3-1) + 3

num = 2
function(2)
return function(2-1) + 2

num = 1
function(1)
return 1

'''



# int main()
x = 4
print(function(x))
print('hello')
