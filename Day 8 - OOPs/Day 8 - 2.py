class Computer:
	def __init__(self, cpu, ram):			#initial method, constructor
		self.cpu = cpu
		self.ram = ram
		print(self.cpu, self.ram, self)		#self gives address and type
	
	def config(self):
		print('yo')

comp1 = Computer('i5', 16)
comp2 = Computer('ryzen', 8)

print(hex(id(comp1)))		#id is used for address in decimal
print(hex(id(comp2)))
