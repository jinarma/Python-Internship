# reversing SLL

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class SLL(Node):
	
	def __init__(self):
		self.head = None

	def insert(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
		else:
			t = self.head
			while t is not None:
				""" if t.next is None:
					t.next = new_node """
				t = t.next
			t = new_node

	def display(self):
		if self.head is None:
			print('Empty SLL')
		else:
			t = self.head
			while t is not None:
				print(t.data)
				t = t.next



a = SLL()

a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)
a.insert(50)

a.display()
