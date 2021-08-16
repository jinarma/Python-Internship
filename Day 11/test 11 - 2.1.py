# multilevel decorator (modifying behaviour of functions)

def student():
	def vineeth():
		def course():
			print('course')

		print('vineeth')
		return course
	print('student')
	return vineeth


a = student()
b = a()
b()