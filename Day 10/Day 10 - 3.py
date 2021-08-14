# Abstraction
from abc import ABC, abstractmethod

class Student(ABC):
	@abstractmethod
	def name(self):
		# print('am not abstract')
		pass


	def age(self):
		print('age = 22')

class Firstyear(Student):
	def name(self):
		print('Conroe')


class Secondyear(Student):
	def name(self):
		print('Skipper')


class Thirdyear(Student):
	def name(self):
		print('KL Rahul')



s = Student()
s.name()
s.age()

