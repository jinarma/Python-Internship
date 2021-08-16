class Sample:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	""" Whenever object is passed in the print() function, it returns a string representation of the object """
	
	""" def __str__(self):
		return '{} {}'.format(self.x, self.y) """



class Sampool:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	""" If __str__ method is not encountered, then the object falls back to __repr__ (representation) method for string representation """
	def __repr__(self):
		return '{} {}'.format(self.a, self.b)




sample = Sample(10, 20)
sampool = Sampool(30, 40)

print(sample)		# return to __str__ method for explainaton
print(sampool)		# return to __repr__ method for explainaton
print(repr(sample))		# explicitly calls the __repr__ method, but no implementation is detected, so address and type are returned
print(repr(sampool))	# explicity calls the __repr method
