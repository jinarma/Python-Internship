# stack using SLL

class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack(Node):

	def __init__(self):
		self.head = None
		self.size_of_stack = 0

	
	def Push(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
			print(new_node.data, 'is pushed')
		else:
			new_node.next = self.head
			self.head = new_node
			print(new_node.data, 'is pushed')
		self.size_of_stack += 1

	def Pop(self):
		if self.head is None:
			print('Stack empty')
		else:
			print('Popped', self.head.data)
			self.head = self.head.next
		self.size_of_stack -= 1

	def Display(self):
		t = self.head
		while t is not None:
			print(t.data)
			t = t.next

	def Peek(self):
		if self.head is None:
			print('Stack empty')
		else:
			print(self.head.data)

	def Size(self):
		print(self.size_of_stack)

a = Stack()

a.Push(10)
a.Push(20)
a.Push(30)
a.Push(40)
a.Push(50)
a.Push(60)
a.Push(70)
print()
a.Display()
print()
a.Pop()
a.Pop()
print()
a.Display()
print()
a.Peek()
a.Size()