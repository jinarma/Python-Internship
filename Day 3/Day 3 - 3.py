#armstrong number true or false
num = int(input("enter a number: "))
temp = num
tmp2 = num
sum = 0
count = 0
while temp>0:
	temp = temp//10
	count += 1
while num>0:
	temp = num%10
	sum = sum + temp**count
	num = num//10
if tmp2 == sum:
	print(tmp2, 'is an armstrong number')
else:
	print(tmp2, 'is not an armstrong number')