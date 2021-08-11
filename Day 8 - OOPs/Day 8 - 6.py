class Students:
	
	school = 'random school'
	def __init__(self, c, java, python):
		self.c = c
		self.java = java
		self.python = python

	def avg(self):
		return (self.c+self.java+self.python)/3

	def get_c(self):		#accessor or getter method (type of instance method)
		return self.c

	def set_c(self, c):		#mutator or setter method (typr of instance method)
		self.c = c
		return c

	@classmethod		#decorator
	def nameofschool(cls):
		return cls.school

	@staticmethod
	def info():
		return 'This school belongs to no one'

stu1 = Students(78, 87, 93)
stu2 = Students(78, 59, 73)

print(stu1.get_c())
print(stu1.set_c(10))

print(stu1.avg())
print(stu2.avg())

print(Students.nameofschool())
print(Students.info())

stu1.info()		#bounded
Students.info(stu1)		#unbounded