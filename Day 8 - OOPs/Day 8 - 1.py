class Computer:
	def config(self):		#self basically tells what instance we use 
		print('i5 16GB 1TB')

comp = Computer()

a = 5

print(type(a))
print(type(comp))
comp.config()
Computer.config(comp)		#here self is replaced by comp