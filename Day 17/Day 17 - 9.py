#max types of swapping 2 nums

a = -1
b = 2

a, b = b, a

a = b + a
b = a - b
a = a - b

temp = a
a = b
b = temp

print(a, b)

list1 = []
list1.append(a)
list1.append(b)
list1.reverse()
a = list1[0]
b = list1[1]
print(a, b)

str1 = ''
str1 += str(a)
str1 += str(b)
a, b = int(str1[1]), int(str1[0])
print(a, b)

a = a | b
b = a - b
a = a - b

print(a, b)

