num = "123456"
my_list = list(map(int, num))

sum1 = my_list.pop(0) + my_list.pop()
sum2 = 0
while my_list:
	sum2 += my_list.pop()
print(sum1, sum2)

