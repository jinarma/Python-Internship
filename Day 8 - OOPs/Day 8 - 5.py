g = 56

class Car:
	print(g)
	global g
	g = 89
	print(g)
	wheels = 4		#class(static) variable
	def __init__(self):
		self.mil = 18		#instance variable
		self.brand = 'Toyota'

	def config(self):
		self.ram = 8
		print(self.ram)

car1 = Car()
car2 = Car()

car2.mil = 20
Car.wheels = 5
car1.wheels = 4

print(car1.mil, car1.brand, car1.wheels)
print(car2.mil, car2.brand, car2.wheels)

car1.config()
print(g)