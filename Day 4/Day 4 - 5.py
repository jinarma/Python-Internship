#Dictionaries in list

studentsList = []
studentsList.append({
	'name' : 'Jinarma',
	'Section' : 'A2',
	'Transport' : 'Local'
})

studentsList.append({
	'name' : 'Rishabh',
	'Section' : 'A2',
	'Transport' : 'Bus'
})

studentsList.append({
	'name' : 'Sneha',
	'Section' : 'A2',
	'Transport' : 'Local'
})

studentsList.append({
	'name' : 'Mehak',
	'Section' : 'A1',
	'Transport' : 'Bus'
})

studentsList.append({
	'name' : 'Aryan',
	'Section' : 'A2',
	'Transport' : 'Motorcycle'
})


for i in range(len(studentsList)):
	print(studentsList[i]['name'], studentsList[i]['Section'])