# single inheritance

class Anand:

	def __init__(self):
		print('This is Anand')

	def Samsung(self):
		print('Samsung phone of Anand')

	def Scooter(self):
		print('Scooter of Anand')

class Vineeth(Anand):
	def __init__(self):
		super().__init__()			#self doesnt work, y tho #update, it does, in the form of super()
		print('This is vineeth')
	def Oneplus(self):
		print('Oneplus phone of Vineeth')

	def Bike(self):
		print('Bike of Vineeth')

class Arjun(Vineeth):
	def __init__(self):
		super().__init__()
		print('This is Arjun')

	def Cartoy(self):
		print('car toy of Arjun')

a = Anand()
v = Vineeth()

# v.Samsung()
# v.Oneplus()
# v.Scooter()

ar = Arjun()


ar.Cartoy()
ar.Oneplus()
ar.Bike()
ar.Samsung()