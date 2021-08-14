# multilevel test protected access

class A:
	def __init__(self):
		_length = '_length'
		_breadth = 20
	def show(self):

class B(A):
	def show(self):


class C(B):
	def show(self):


obA = A()
obB = B()
obC = C()

obA.show()
obB.show()
obC.show()
