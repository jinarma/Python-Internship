import math

def num_atoms(grams_of_element, atomic_weight_of_element):
	temp = grams_of_element/atomic_weight_of_element * 6.022e+23
	print(math.floor(temp), 'atoms')

num_atoms(112, 12.001)