# shorter

def days_check(num):
	year, week, day = 365, 7, 1
	year_inc, week_inc, day_inc = 0, 0, 0

	if num // year == 0:
		print(0)
	else:
		year_inc = num // year
		num = num - year*year_inc
		week_inc = num // week
		num = num - week*week_inc
		day_inc = num
		if week_inc == 0:
			print(year_inc, week_inc, 0, sep='\n')
			return
	print(year_inc, week_inc, day_inc, sep='\n')
	


days_check(373)
days_check(366)
days_check(367)

	




	
