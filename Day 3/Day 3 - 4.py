#strong numbers, (sum of factorials of digits of a number)
num = int(input("enter a number: "))
num2 = num
temp = 0
sum_inside = 1
sum = 0
while num>0:
	temp=num%10
	for i in range(1, temp+1):
		sum_inside*=i
	sum += sum_inside
	num=num//10
	sum_inside = 1

if sum == num2:
	print(sum, 'is a strong number')
else:
	print(sum, 'is not a strong number')
