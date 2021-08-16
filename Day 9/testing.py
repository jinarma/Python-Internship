# multilevel test protected access

class A:
	def __init__(self):
		self._length = '_length'
		self.__breadth = 20
	def show(self):
		print('class A')
		print(self._length)
		print(self.__breadth)
		print()

class B(A):
	def show(self):
		print('class B')
		print(self._length)		# protected variable is accesible in inherited class
		# print(self.__breadth)		# private variable is NOT accesible in inherited class
		print()

class C(B):
	def show(self):
		print('class C')
		print(self._length)		# protected variable is accesible in inherited class
		# print(self.__breadth)		# private variable is NOT accesible in inherited class
		print()


obA = A()
obB = B()
obC = C()

obA.show()
obB.show()
obC.show()

print(obA._length)		# protected variable is accesible through base class outside that class
# print(obA.__breadth)		# private variable is NOT accesible outside the class
print()

print(obB._length)		# protected variable is accesible outside the base class through a derived class
# print(obB.__breadth)		# private variable is NOT accesible outside the class
