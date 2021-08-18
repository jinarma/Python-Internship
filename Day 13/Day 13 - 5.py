# queue

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class Queue(Node):

	def __init__(self):
		self.head = None
		self.size_of_queue = 0

	def Enqueue(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
			print(new_node.data, 'enqueued')
		else:
			new_node.next = self.head
			self.head = new_node
			print(new_node.data, 'enqueued')
		self.size_of_queue += 1

	def Dequeue(self):
		if self.head is None:
			print('Queue empty')
			exit()
		elif self.head.next is None:
			print(self.head.data, 'dequeued')
			self.head = None
		else:
			t = self.head
			while t.next.next is not None:
				t = t.next

			print(t.next.data, 'dequeued')
			t.next = None
		self.size_of_queue -= 1

	def Display(self):
		t = self.head
		if self.head is None:
			print('Queue empty')
		while t is not None:
			print(t.data)
			t = t.next


	def Size(self):
		print('Size', self.size_of_queue)


a = Queue()

a.Enqueue(10)
a.Enqueue(20)
a.Enqueue(30)
a.Enqueue(40)
a.Enqueue(50)
a.Enqueue(60)
a.Enqueue(70)
a.Size()
print()
for i in range(4):
	a.Dequeue()
a.Size()
a.Display()

