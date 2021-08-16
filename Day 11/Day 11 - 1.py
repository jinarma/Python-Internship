

'''
passing fucntion as an argument
'''

def student():
	print('He is a student')


def vineeth(func):
	a = func()
	print('vineeth')

vineeth(student)