#tuple duplication, slicing and check if mutable
tuple1 = ("spiders", 'are', 'scary')*3

print(tuple1)
print(tuple1[3:])
print(tuple1[3:5])

tuple2 = ('spiders', 'not', 'scary')*3

tuple3 = tuple1+tuple2

print(tuple3)

tuple4 = ('is', 'this', 'the', 'best', 'you', 'got')

print(tuple4)

# tuple4.append('boi')	#this line ends in error