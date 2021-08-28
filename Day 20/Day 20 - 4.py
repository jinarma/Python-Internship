""" 
A famous company is going to select a new Managing Director. All the eligible candidates are waiting in the meeting room. Everyone is seated in a random order linearly. Everyone are cunning and want's to become the Managing Director. If the founder of that company tell's a person name directly definitely that is going to become a serious problem. But the founder already have a person on his mind. But he was thinking for a creative idea to convey the same. Suddenly he notices a pattern follows and he find a way to tell who is the new MD.
He say's "the next MD of this company is the person who haves the age greater than all the other person to his right side."
Write the program to find the new MD of that company where you are provided with the n persons age in order similar to their seating arrangement. In case if the founder couldn't find the next MD print, "The promotion stands cancelled".

Note: There will be at least 2 person waiting in the meeting room.
 """


def select_MD(persons_list):

	for i in range(0, len(persons_list)-1):
		if persons_list[i] == max(persons_list[i:]):
			print(i, persons_list[i])
			return
	print('The promotion stands cancelled')
	return


select_MD([3, 2, 3, 2])
		

	


