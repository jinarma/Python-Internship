# DLL (Doubly linked list)

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DLL(Node):

	def __init__(self):
		self.head = None
		self.last = None

	def insert_at_end(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
		else:
			t = self.head

			while t.next is not None:
				t = t.next
			
			t.next = new_node
			new_node.prev = t

	def insert_at_begin(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def DeleteatEnd(self):
		t = self.head
		if self.head is not None:
			while t.next.next is not None:
				t = t.next
			t.next = None

	def DeleteatBegin(self):
		if self.head is None:
			print('No elements')
		else:
			self.head = self.head.next
			self.head.prev = None

	## make insert_at_pos, delete_at_end, delete_at_begin and delete_at_pos methods

	def delete_at_pos(self, pos):
		if self.head is None:
			print('no elements')
			return
		elif pos == 1:
			self.head = self.head.next
		else:
			t = self.head
			while pos-2:
				t = t.next
				pos -= 1
				if t.next is None:
					print('Out of range')
					return

			t.next = t.next.next
			t.next.prev = t


	def display(self):
		t = self.head
		while t.next is not None:
			print(t.data)
			t = t.next
		print(t.data)


a = DLL()
a.insert_at_end(10)
a.insert_at_end(20)
a.insert_at_end(30)
a.insert_at_end(40)
a.insert_at_end(50)
a.insert_at_end(60)
a.insert_at_end(70)

a.display()
