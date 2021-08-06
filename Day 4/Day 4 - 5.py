#Dictionaries in list

studentsList = []
studentsList.append({
	'name' : 'Jinarma',
	'Section' : 'A2',
	'Transport' : 'Motorcycle'
})

studentsList.append({
	'name' : 'Rishabh',
	'Section' : 'A2',
	'Transport' : 'Bus'
})

for i in range(len(studentsList)):
	print(studentsList[i]['name'])