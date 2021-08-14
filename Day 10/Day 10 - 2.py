#overriding


class A:
	def show(self):
		print('I am class A')

# if class B show is commented out with a pass, the it overrides
class B(A):
	def show(self):
		print('I am class B')

a1 = B()
a1.show()