#check ques.png in downloads (completed)


class Item:
	
	def __init__(self, price):
		self.price = price

class Customer:

	def __init__(self, product_name, quantity):
		self.product_name = product_name
		self.quantity = quantity

class Bill(Customer, Item):

	def __init__(self, product_name, price, quantity):
		Customer.__init__(self, product_name, quantity)
		Item.__init__(self, price)
	
	def display_cost(self):
		print(self.price * self.quantity)


product_name = input()
price = int(input())
quantity = int(input())

ob = Bill(product_name, price, quantity)
ob.display_cost()