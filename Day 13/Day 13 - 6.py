# reverse DLL H.W. (incomplete)

class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DLL(Node):

	def __init__(self):
		self.head = None
		self.last = None

	def insert(self, data):
		new_node = Node(data)
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

	def reverse(self, t):
		if self.head is None:
			print('Empty DLL')
			exit()
		else:
			if t.next is None:
				temp = t.next
				t.next = t.prev
				t.prev = temp
				#self.head = t
				print('check')
				return t
			else:
				print('check 2')
				t = self.reverse(t.next)
				print('check 3')
				temp = t.next
				t.next = t.prev
				t.prev = temp
				return t

	def diplay(self):
		if self.head is None:
			print('DLL is empty')
		else:
			t = self.head
			while t.next is not None:
				print(t.data)
				t = t.next
			print(self.last.data)

	



a = DLL()

a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)
a.insert(50)

a.diplay()
print()

#a.reverse(a.head)

a.diplay()