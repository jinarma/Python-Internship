#operator overloading


class Student:
	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

	def __add__(self, other):		#magic operators __add__, __mul__
		a = self.m1 + other.m1
		b = self.m2 + other.m2
		t = Student(a, b)
		return t
		#return a, b		#gives tuple, when we dont want it


	def __gt__(self, other):
		a = self.m1 + self.m2
		b = other.m1 + other.m2

		if a>b:
			return True
		else:
			return False


	def __str__(self):		#check how this works
		return '{} {}'.format(self.m1, self.m2)

	def __int__(self):
		x = self.m1
		y = self.m2
		return x, y


s1 = Student(78, 96)
s2 = Student(86, 84)

print(s1)		# __str__ is called as a constructor without explicitly calling it
print(str(s1))		# implementation in __str__(self)

t = s1+s2
#print(s1)
# print(s1+s2)
# print(s1>s2)
