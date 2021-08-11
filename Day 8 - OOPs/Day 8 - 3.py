class Computer:
	def __init__(self, cpu, ram, brand):  # initial method, constructor
		self.cpu = cpu
		self.ram = ram
		self.brand = brand
		#print(self.cpu, self.ram)  # self gives address and type

	def config(self):
		print('yo')
	
	def update(self):
		self.brand = 'hp'


comp1 = Computer('i5', 16, 'dell')
comp2 = Computer('ryzen', 8, 'dell')

comp1.cpu = 'i7'
comp1.update()

print(comp1.cpu, comp1.ram, comp1.brand)
print(comp2.cpu, comp2.ram, comp2.brand)
