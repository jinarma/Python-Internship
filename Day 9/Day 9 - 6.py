# hybrid inheritance

class Anand:

	def __init__(self):
		print('This is Anand')

	def Samsung(self):
		print('Samsung phone of Anand')

	def Scooter(self):
		print('Scooter of Anand')


class Lalita():
	def __init__(self):
		print('This is Lalita')

	def Apple(self):
		print('Apple of Lalita')



class Vineeth(Anand):
	def __init__(self):
		#super().__init__()  # only runs anand init because MRO (method resolution order)
		print('This is vineeth')

	def Oneplus(self):
		print('Oneplus phone of Vineeth')

	def Bike(self):
		print('Bike of Vineeth')


class Teja(Lalita, Anand):		#if i use (Anand, Vineeth) then MRO issue, because vineeth is inherited twice, one through vineeth, one through Anand
	def __init__(self):
		print('This is Teja')

	def Apple(self):
		print('Apple of Teja')

	def Car(self):
		print('Car of Teja')


v = Vineeth()
t = Teja()

