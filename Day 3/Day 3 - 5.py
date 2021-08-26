num = [1, 2, 3, 4]
stg = ['python', 'language', ['easy']]
num.extend(stg)		#extend adds elements from the iterable for one level; takes multiple inputs as args
num.append([8, 19])	#takes only one input whether one iterable of multiple elements or just one element and adds it to the end of the list
#num += stg
num.insert(4, 'good')
print(num)