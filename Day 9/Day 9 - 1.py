# INNER CLASSES or NESTED CLASSES

class Student:
		def __init__(self, name, rollno):
			self.name = name
			self.rollno = rollno


			self.lap = self.Laptop()		#lap is working as the object of Laptop class
			self.mob = self.Mobile()		#mob is working as the object of Mobile class

		def show(self):
			print(self.name, self.rollno)

			self.lap.show()  # lap is working as the object of Laptop class
			self.mob.show()  # mob is working as the object of Mobile class


		class Laptop:
			def __init__(self):
				self.brand = 'Dell'
				self.cpu = 'i5'
				self.ram = 16

			def show(self):
				print(self.brand, self.cpu, self.ram)


		class Mobile:
			def __init__(self):
				self.brand = 'Apple'
				self.color = 'Silver'

			def show(self):
				print(self.brand, self.color)

s1 = Student('Kamil', 23)
s2 = Student('Suvrat', 39)

s1.show()
s2.show()
s1.Laptop()

print()

s1Lap = Student.Laptop()
s1Mob = Student.Mobile()
s1Lap.show()
s1Mob.show()
#Student.Laptop.show()
