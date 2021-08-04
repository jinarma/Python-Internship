#find if a number is divided by 3&4 ir not
a = int(input("Enter a number 12"))
if a%3 == 0 and a%4==0:
	print(a, "is divisible by 3 and 4", sep=" ")
else:
	print(a, "is not divisible by 3 and 4", sep=" ")
