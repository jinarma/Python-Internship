class Calculator:

	def add(self, num1, num2):
		return num1 + num2

	def sub(self, num1, num2):
		return num1 - num2

class AdvancedCalculator(Calculator):
	
	def mul(self, num1, num2):
		return num1 * num2

	def div(self, num1, num2):
		return num1 // num2

a = 10
b = 2
ob1 = AdvancedCalculator()

print('Addition:', ob1.add(a, b))
print('Subtraction:', ob1.sub(a, b))
print('Multiplication:', ob1.mul(a, b))
print('Division:', ob1.div(a, b))

