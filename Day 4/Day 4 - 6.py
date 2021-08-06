# dictionaries effective

studentList = []
for i in range(5):
	tempDict = {}
	tempDict['name'] = input('Name: ')
	tempDict['Section'] = input('Section: ')
	tempDict['Transport'] = input('Transport: ')
	studentList.append(tempDict)

for i in range(len(studentList)):
	print(studentList[i]['name'], studentList[i]['Transport'], sep='\t\t')