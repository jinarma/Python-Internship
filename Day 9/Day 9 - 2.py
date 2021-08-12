# multilevel nesting

class Student:

	def __init__(self, name):
		self.name = name
		self.lap = self.Laptop()

	def	show(self):
		print(self.name)
		self.lap.show()

	class Laptop:
		def __init__(self):
			self.brand = 'Asus'
			self.cpu = 'Ryzen'
			self.ram = 8
			self.py = self.Python()

		def show(self):
			print(self.brand, self.cpu, self.ram)
			self.py.show()

		class Python:
			def __init__(self):
				self.trainer = 'Vineeth'

			def show(self):
				print(self.trainer)


s1 = Student('Shubhankar')
s1.show()

s1_py = Student.Laptop.Python()
s1_py.show()