# encapsulation

class Shape:
	def __init__(self):
		# pass
		self.__show()

	def __show(self):
		print('am in show')

class Rectangle(Shape):
	pass

a = Shape()
# a.__show()		#error because private
b = Rectangle()
# b.__show()		#error because	private
