# ques 12

def cinema_day_check(day, month, year, student_num):

	if (day+month+year)%12 == 0 and student_num > 50 and student_num < 100:
		print('Cinema Day')
	else:
		print('Not a Cinema Day')

cinema_day_check(3, 3, 1914, 76)
cinema_day_check(27, 10, 1995, 50)