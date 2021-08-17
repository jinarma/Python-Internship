""" single inheritance """

class University:

	def __init__(self, name, state):
		self.name = name
		self.state = state
		self.clas = 'University'

	def show_Uni(self):
		print(self.name, self.state)

class College(University):
	
	def __init__(self, c_name, c_state, c_uni):
		super().__init__(c_uni, c_state)			# if super() is removed, then college.show_Uni() would result in an error because a University class object is not instanciated with College class object
		""" Thus University instance methods being available in College class """
		self.c_name = c_name
		self.c_state = c_state
		self.c_uni = c_uni

	def show_Col(self):
		print(self.c_name, self.c_state, self.c_uni)


college = College('miet', 'jammu', 'jammu university')
college.show_Col()

# university = University('Jammu university', 'Jammu')

# university.show_Uni()
college.show_Uni()

print(college.clas)
