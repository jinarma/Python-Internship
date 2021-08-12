#duck typing

class Student:
	def studentnames(self):
		print('kaaliya')
		print('jojo')
		print('Astinos')
		print('Ricardo')

class Thirdyear:
	def section(self, other):
		other.studentnames()


stu = Student()
third = Thirdyear()

third.section(stu)