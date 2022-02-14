# rotate a linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SLL:
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

	def rotate(self, pos):
		if pos == 0:
			return
		
		temp = self.head
		count = 1

		while count<pos and temp is not None:
			temp = temp.next
			count += 1

		if temp is None:
			return

		new_first = temp

		while temp.next is not None:
			temp = temp.next

		temp.next = self.head
		self.head = new_first.next
		new_first.next = None

	def display(self):
		t = self.head
		while t is not None:
			print(t.data)
			t = t.next

a = SLL()
a.insert_at_end(10)
a.insert_at_end(20)
a.insert_at_end(30)
a.insert_at_end(40)
a.insert_at_end(50)
a.insert_at_end(60)
a.insert_at_end(70)

a.display()
print()
a.rotate(3)
a.display()
