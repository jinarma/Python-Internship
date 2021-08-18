# circular DLL


class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None



class CDLL(Node):

	def __init__(self):
		self.head = None
		self.last = None

	def insert_at_end(self, x):
		new_node = Node(x)

		if self.head is None:
			self.head = new_node
			new_node.prev = new_node
		else:
			t = self.head
			while t.next is not self.head:
				t = t.next
			t.next = new_node
			new_node.prev = t
		new_node.next = self.head
		self.last = new_node
		self.head.prev = new_node

	# complete for other methods
	
	def display(self):
		if self.head is None:
			print('List empty')
		else:
			t = self.head
			while t.next is not self.head:
				print("node.prev=", hex(id(t.prev)), "node.data=", t.data, "node address=", hex(id(t)), "node.next=", t.next)
				t = t.next
			print("node.prev=", hex(id(t.prev)), "node.data=", t.data, "node address=", hex(id(t)), "node.next=", t.next)


a = CDLL()

a.insert_at_end(10)
a.insert_at_end(20)
a.insert_at_end(30)
a.insert_at_end(40)
a.insert_at_end(50)
a.insert_at_end(60)

a.display()
