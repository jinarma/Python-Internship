# ques hi ques 2.12

def function(num):
	sum1 = 0
	sum2 = 0
	for i in range(2):
		if i == 0:
			temp = num%10
			sum1 += temp
			num = num//10
		else:
			s1 = str(num)
			s1 = s1[::-1]
			num = int(s1)
			temp = num%10
			sum1 += temp
			num = num//10
		
	
	for i in range(len(str(num))):
		temp = num%10
		sum2 += temp
		num = num//10

	if sum1 >= sum2:
		print(sum1)
	elif sum1 < sum2:
		print(sum2)



function(31458)