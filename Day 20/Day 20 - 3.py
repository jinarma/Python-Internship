## complete


""" Since he is pushing the pendulum to his right always. He wanted to store that distance in the right extreme of the arrangement. And the pendulum will move towards the extreme left at that time he want that value to be stored in the left most extreme in the arrangement. And this continues till the pendulum stops. He is also sure that the distance reached at that oscillation will always be lesser than the previous oscillation towards that particular end.Write a program to arrange the distance as i

Bob is doing a research in Pendulum. He is just pushing the pendulum aside and the pendulum started moving in to-and-fro motion. Bob will push the pendulum always towards his right side to start the oscillation. Bob wanted to calculate the distance between extreme position and the centre position of pendulum for each oscillations. He somehow calculated all the possible distance. Since he is busy in this research he is giving the task to his assistant who needs to arrange the values as instructed
Since he is pushing the pendulum to his right always. He wanted to store that distance in the right extreme of the arrangement. And the pendulum will move towards the extreme left at that time he want that value to be stored in the left most extreme in the arrangement. And this continues till the pendulum stops. He is also sure that the distance reached at that oscillation will always be lesser than the previous oscillation towards that particular end.Write a program to arrange the distance as i
Sample Input:
5
1 3 2 5 4
Sample Output:
4 2 1 3 5
Explanation:
The maximum distance in the given data is 5 hence that is placed in the right most end
The next maximum element is 4 which is placed in the left most end. Again the pendulum oscillates towards right to cover a distance of 3 and this continues.
 """


def pendulum_data(num, num_list):
	print(num, num_list)
	temp_list = num_list
	left_list, right_list = [], []
	flag = 1
	while num_list:
		
		if flag == 1:
			# pops max element and stores it in temp_list
			right_list.insert(0, num_list.pop(num_list.index(max(num_list))))
			flag -= 1
		else:
			# pops max element and stores it in temp_list
			left_list.insert(len(num_list)//2, num_list.pop(num_list.index(max(num_list))))
			flag += 1

	num_list = left_list+right_list
	print(num_list)




pendulum_data(5, [1, 3, 2, 5, 4])
