# reverse DLL H.W.
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
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def reverse(self):
		
		if self.head is None:
			print('DLL is empty')
			return
		temp = None
		t = self.head
		while t is not None:
			temp = t.prev
			t.prev = t.next
			t.next = temp
			t = t.prev
		if temp is not None:
			self.head = temp.prev

	def diplay(self):
		if self.head is None:
			print('DLL is empty')
		else:
			t = self.head
			while t is not None:
				print(t.data)
				t = t.next

	



a = DLL()

a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)
a.insert(50)

a.diplay()
print()

a.reverse()

a.diplay()
