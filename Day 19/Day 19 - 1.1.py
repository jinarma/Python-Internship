

num = input("Enter the number : ")
num_list = list(map(int, num))

print(num_list[0]+num_list[len(num_list)-1])
temp = 0
for i in num_list[1:len(num_list)-1]:
	temp += i
print(temp)
