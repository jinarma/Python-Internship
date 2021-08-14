# encapsulation getter setter

class Shape:
	def __init__(self, a):
		self.__a = a
		
	def get_a(self):
		return self.__a

	def set_a(self, a):
		self.__a = a
		return self.__a



class Rectangle(Shape):
	pass



a = Shape(5)
# print(a.__a)		#error because private
print(a.get_a())
a.set_a(6)
print(a.get_a())
# a.__show()		#error because private
# b = Rectangle()
# b.__show()		#error because	private
