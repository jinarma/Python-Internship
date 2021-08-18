# Circular Linked list

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class Circular_SLL(Node):

	def __init__(self):
		self.head = None
		self.last = None

	def insert_at_end(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
		else:
			t = self.head
			while t.next is not self.head:
				t = t.next
			t.next = new_node
		new_node.next = self.head

	def insert_at_begin(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
			self.last = new_node
			new_node.next = self.head
		else:
			new_node.next = self.head
			self.last.next = new_node
			self.head = new_node

	# insert at pos, and all delete methods


	def display(self):
		if self.head is None:
			print('List empty')
		else:
			t = self.head
			while t.next is not self.head:
				print(t.data)
				t = t.next
			print(t.data)


a = Circular_SLL()

a.insert_at_end(10)
a.insert_at_end(20)
a.insert_at_end(30)
a.insert_at_end(40)
a.insert_at_end(50)
a.insert_at_end(60)

a.display()