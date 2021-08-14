class GridPoint:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return GridPoint(x, y)

	def __str__(self):
		return '{} {}'.format(self.x, self.y)



num1 = 5
num2 = 4
num3 = 9
num4 = 4

ob1 = GridPoint(num1, num3)
ob2 = GridPoint(num2, num4)

print(ob1+ob2)

print(ob1)
print(ob2)
