#ques2.png in downloads (completed)
# 3, 2, 6, 5, 1, 4, 8, 9 <--- input
# complete
import math


list1 = list(map(int, input().split(',')))
num1 = sum(list1[:list1.index(5)]+list1[list1.index(8)+1:])
print(num1)
num2 = ''
temp = list1[list1.index(5):list1.index(8)+1]
print(temp)

for i in temp:
	num2 += str(i)

print(num2)

print(num1+int(num2))

