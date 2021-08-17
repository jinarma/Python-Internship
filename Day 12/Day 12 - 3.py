# DLL reverse traversal
# Homework

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DLL(Node):

	def __init__(self):
		self.head = None
		self.last = None

	def insert(self, x):
		new_node = Node(x)
		
		if self.head is None:
			self.head = new_node
			self.last = None
		else:
			t = self.head
			while t.next is not None:
				t = t.next
			t.next = new_node
			new_node.prev = t
			self.last = new_node

	def display(self):
		if self.head is None:
			print('List is empty')
		else:
			t = self.head
			while t.next is not None:
				print(t.data)
				t = t.next
			print(t.data)
	
	def reverse(self):
		if self.last is None:
			print('No list')
		else:
			t = self.last
			while t.prev is not None:
				print(t.data)
				t = t.prev
			print(t.data)



a = DLL()

a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)

a.display()
print()
a.reverse()