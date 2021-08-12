#Overloading

a = 5
b = 6

c = 'Python'
d = 'Class'

print(a+b)
print(int.__add__(a, b))		#integer add
print(c+d)
print(str.__add__(c, d))		#string concatination

#print(a+c)
