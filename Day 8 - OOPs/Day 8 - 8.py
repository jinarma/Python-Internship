
z = 10
class Students:
	#global z
	print(z)
	z = 8
	def __init__(self):
		pass

ob = Students()
print(z)