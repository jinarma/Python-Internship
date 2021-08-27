# ques 11

def days_check(num):
	year, week, day = 365, 7, 1
	year_inc, week_inc, day_inc = 0, 0, 0


	if num >= year:
		while num >= year:
			num -= year
			year_inc += 1
		
		if num >= week:
			while num >= week:
				num -= week
				week_inc += 1

			if num >= day:
				while num >= day:
					num -= day
					day_inc += 1
		print(year_inc, week_inc, day_inc, sep='\n')
	elif num < year:
		print(0)



days_check(373)
days_check(366)
days_check(367)
days_check(1140)

	




	
