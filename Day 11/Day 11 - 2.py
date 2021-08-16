# decorators

def student(text):
	def vineeth():
		print(text, 'vineeth')

	return vineeth			# when calling functions in return statememnt

a = student('this is a')

a()